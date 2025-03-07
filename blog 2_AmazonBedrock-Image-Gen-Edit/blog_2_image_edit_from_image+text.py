"""Getting image from S3 and then editing it and then finally storing it in S3 bucket manually."""
import boto3
import json
import base64
# import io
# from PIL import Image
import random
import uuid


# Set up the Amazon Bedrock client
bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

s3_client = boto3.client('s3')
bucket_name = "jay-blog2-image"
prev_image = "de203f85-fa62-11ef-a16c-5800e380d2a8"
file_path = f'images_from_sdk/{prev_image}'

prev_image = s3_client.get_object(Bucket=bucket_name, Key=file_path)
# File is already coming in bytes format
prev_image_body = prev_image["Body"].read() 
# print(type(prev_image_body))
# To check if prev_image_body is in base 64 format.
# print(base64.b64encode(base64.b64decode(prev_image_body)) == prev_image_body) => False which means we have to encode it in base64!
prev_image_str = base64.b64encode(prev_image_body).decode('utf-8')
# print(type(prev_image_str))
# image = Image.open(BytesIO(prev_image_body))
# image.show()

# Define the model ID
model_id = "amazon.titan-image-generator-v2:0"

# Prepare the input prompt
prompt = "change this image to a 1 human playing football with 1 alien"

random_seed = random.randint(0,100)

# Create the request payload for modification by using In-Painting, you can use image_variation for creating another variations of image.
body = json.dumps({
    "taskType": "INPAINTING",
    "inPaintingParams": {
        "image": prev_image_str,                         
        "text": prompt,     
        "maskPrompt": "identify one alien which you have to replace with a human",                      
    },                                                 
    "imageGenerationConfig": {
        "quality": "standard",
        "numberOfImages": 1,
        "height": 512,
        "width": 512,
        "cfgScale": 8.0,
        "seed": random_seed
    }
    })
# body = json.dumps(
#     {
#      "taskType": "IMAGE_VARIATION",
#      "imageVariationParams": {
#          "text": prompt,
#          "images": [prev_image_str],
#          "similarityStrength": 0.2,  # Range: 0.2 to 1.0
#      },
#      "imageGenerationConfig": {
#          "quality": "standard",
#          "numberOfImages": 1,
#          "height": 512,
#          "width": 512,
#          "cfgScale": 5.0
#      }
#     }
# )

accept = "application/json"
content_type = "application/json"

# Invoke the Amazon Bedrock model
response = bedrock_client.invoke_model(
    modelId=model_id,
    body=body,
    accept=accept, 
    contentType=content_type
)

# Process the response
result = json.loads(response["body"].read())

base64_image = result.get("images", None)[0]
base64_bytes = base64_image.encode('ascii')
image_bytes = base64.b64decode(base64_bytes)
# image = Image.open(io.BytesIO(image_bytes))
# image.show()

image_name  = f'edit_images_from_sdk/{uuid.uuid1()}'

s3_client.put_object(Bucket=bucket_name, Key=image_name, Body=image_bytes, ContentType='image/png')

presigned_url = s3_client.generate_presigned_url('get_object', Params={'Bucket': bucket_name, 'Key': image_name}, ExpiresIn=86400)

print(presigned_url)