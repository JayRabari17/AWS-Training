"""Generating image and storing it in S3 bucket manually."""
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

# Define the model ID
model_id = "amazon.titan-image-generator-v1"

# Prepare the input prompt
prompt = "Generate a cartoon image of aliens playing football with humans"

random_seed = random.randint(0,100)

# Create the request payload
body = json.dumps({
        "taskType": "TEXT_IMAGE",
        "textToImageParams": {
            "text": prompt
        },
        "imageGenerationConfig": {
            "numberOfImages": 1,
            "height": 512,
            "width": 512,
            "quality": "standard",
            "cfgScale": 8.0,
            "seed": random_seed
        }
    })

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

image_name  = f'images_from_sdk/{uuid.uuid1()}'

s3_client.put_object(Bucket=bucket_name, Key=image_name, Body=image_bytes, ContentType='image/png')

presigned_url = s3_client.generate_presigned_url('get_object', Params={'Bucket': bucket_name, 'Key': image_name}, ExpiresIn=86400)

print(presigned_url)