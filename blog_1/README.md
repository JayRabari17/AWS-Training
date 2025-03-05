# Building Generative AI Applications with Amazon Bedrock Using Boto3

## Prerequisites
To follow along with this guide, ensure you have the following:

- An AWS account with access to Amazon Bedrock models (`amazon.titan-text-micro-v1:0`) in the `us-east-1` region.
- An IAM user with the necessary permissions to access and invoke the model.
- [AWS CLI](https://awscli.amazonaws.com/AWSCLIV2.msi) installed and configured with your IAM user’s access key and secret key.
- Python 3.8 installed along with an IDE of your choice.
- The latest version of the Boto3 library.

## Setting Up the Environment

### Install Boto3
Install Boto3 using `pip` to interact with AWS services in Python:

```bash
pip install boto3
```

## Writing the Python Script

Create a Python file (e.g., `blog_1.py`) and add the following code to interact with Amazon Bedrock.

```python
# Import necessary libraries
import boto3
import json

# Set up the Amazon Bedrock client
bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

# Define the model ID
model_id = "amazon.nova-micro-v1:0"

# Prepare the input prompt
prompt = "Hello, how are you?"

# Create the request payload
body = { 
    "inferenceConfig": {
      "max_new_tokens": 2048
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
```

## Running the Script
Execute the Python script with the following command:

```bash
python blog_1.py
```

## Expected Output
```bash
"Hello! I'm here and ready to assist you with any questions or information you need. How can I help you today?"
```

This script demonstrates how to use Amazon Bedrock with Boto3 to generate AI-powered responses using the `amazon.titan-text-micro-v1` model.

