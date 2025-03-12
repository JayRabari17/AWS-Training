import boto3
import json

# Set up the Amazon Bedrock client
bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

# Define the model ID
model_id = "amazon.nova-lite-v1:0"

# Prepare the input prompt
prompt = "Tell me a joke!"

# Create the request payload
body = { 
    "inferenceConfig": {
      "max_new_tokens": 2048,
      "temperature": 0.9,
      "top_k": 250,
      "top_p": 1,
    },
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "text": prompt
          }
        ]
      }
    ]
}

# print(json.dumps(body))

# Invoke the Amazon Bedrock model
response = bedrock_client.invoke_model(
    modelId=model_id,
    body=json.dumps(body)
)

# Process the response
result = json.loads(response["body"].read())
# print(result)
generated_text = "".join([output["text"] for output in result["output"]["message"]["content"]])
print(f"Response: {generated_text}")