# Generate and Evaluate Images in Amazon Bedrock

This project follows the AWS blog post on [Generating and Evaluating Images in Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/generate-and-evaluate-images-in-amazon-bedrock-with-amazon-titan-image-generator-g1-v2-and-anthropic-claude-3-5-sonnet/). It sets up an API to generate images using Amazon Titan Image Generator G1-V2 and evaluates them using Anthropic Claude 3.5 Sonnet.

## Requirements
- AWS account with access to Amazon Bedrock models.
- IAM user with the required permissions.
- AWS CLI installed and configured.
- Python 3.8 or later with Boto3 installed.

## Setup Instructions

### 1. Deploy the CloudFormation Template
1. Upload the CloudFormation YAML file to AWS CloudFormation.
2. Provide necessary parameters like S3 bucket names and API token.
3. Deploy the stack and wait for completion.

### 2. Invoke the API
- Use the API Gateway endpoint to send a POST request with a text prompt.
- Select Test section to send api request.
- Now, go to body sub-section and write the prompt request.
- The API returns an image URL (pre-signed URL) and evaluation details.
## Example Request in 'Test' section of API Gateway endpoint 'POST' request
```json
{
  "prompt": "A futuristic city skyline at sunset"
}
```

## Example Response
![alt text](API_Gateway-Test-o_p.png)
```json
{
  "url": "https://bog-images-meet-7.s3.amazonaws.com/image-gen-eval/e1fk3l2fhe.png?AWSAccessKeyId=ASIA6D6JBWOZIV3IMD2P&Signature=zoTePCIN%2FKorQLvnzJbjjDR8%2Frw%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCICLoU197TyUGH90ir22mVnrNXq03OQd1%2BMMGudwusZWUAiEA0iGMjdeF4uc%2BRZfa8yhOQ3z2PwSc5gA1Dtom6OxMhQwqjwMIEBAAGgw5NzA1NDczNzcwNzQiDB2Ia4g7OStawxX0zirsAnwFLeyjFW17rZU%2BX20tv0uOOTeIlk3IA4AJ8MWxeO4D1X0057Onyda0ZNfeScMJpMnsSVwUow0uHvV2vAr4OeKIU91YWvrDKs%2BhP%2FcmTWjq6l%2B2rNuVQMWkxZ7xyg2aXF2CcC8E2j3d5Hgj3qW%2B8CQ%2Fcv2fulQd9jx5aPbKOOsoGbly%2FPMOhfwnacZ9G09I90gQRSUBisaGJhjicq%2FgDzCVONltBPdUyKOkN%2FZZSSzyQcldAnKGrjAAer24sDHnmKZBJY9SFrcjHvspYJUx9QxnH1DqZHmbIIs9iKfQS%2FKlC5YjUMqAvwOMa22I0bSlHwM9SfXZdgkC2k%2B%2Fx%2BJgE9jsZhWxMIS7vc%2B%2BixCGpPtZ1NIjz5HZmuXjzY8U4H%2F%2F%2FrsT1mboTlz3wkBvYv4dHs3RY%2F6B7Qk4z0lPWmhzFVFeaeBpGJhXanNf2PB8MXV3vu%2BL7xEw%2FN120xGIgoKzpca4X9ZxdBf9ZL3bS6owyuOfvgY6nQHxZgJiUL1UMy4i%2BPRmuqyCniJrtQ0xPNChkfclz28JrLIQM4pHfa3G3UhFVxCbPdYI5K%2Bn9h58bUwh%2B67ViZtM3RfLIHZLM85ZfJX0SJdJSBC27bNijY%2FckR25ggXMuLi4nfeoM18q0K%2FdUmZ0eaTUZ3WK4s3rEyRgBTOS3tyLonGLqrebO4svJsDwlkOD9dapzf3YAqzvreB6znNo&Expires=1741160613",
  "evaluation_data": {"description": "A vibrant red apple with a stem on a wooden surface against a dark teal background.", "score": "10", "reason": "The image perfectly captures a realistic, high-quality representation of an apple with excellent detail and lighting.", "suggestions": "The image already perfectly fulfills the prompt. No improvements are necessary to better attain the original request."}
}
```

### 3. Check Logs and Images
- Images are stored in the configured S3 bucket.
- CloudWatch logs track API usage and errors.

```log
/generate-image - POST method test results
Request
/generate-image
Latency ms
16210
Status
200
Response body
{"url": "https://bog-images-meet-7.s3.amazonaws.com/image-gen-eval/e1fk3l2fhe.png?AWSAccessKeyId=ASIA6D6JBWOZIV3IMD2P&Signature=zoTePCIN%2FKorQLvnzJbjjDR8%2Frw%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCICLoU197TyUGH90ir22mVnrNXq03OQd1%2BMMGudwusZWUAiEA0iGMjdeF4uc%2BRZfa8yhOQ3z2PwSc5gA1Dtom6OxMhQwqjwMIEBAAGgw5NzA1NDczNzcwNzQiDB2Ia4g7OStawxX0zirsAnwFLeyjFW17rZU%2BX20tv0uOOTeIlk3IA4AJ8MWxeO4D1X0057Onyda0ZNfeScMJpMnsSVwUow0uHvV2vAr4OeKIU91YWvrDKs%2BhP%2FcmTWjq6l%2B2rNuVQMWkxZ7xyg2aXF2CcC8E2j3d5Hgj3qW%2B8CQ%2Fcv2fulQd9jx5aPbKOOsoGbly%2FPMOhfwnacZ9G09I90gQRSUBisaGJhjicq%2FgDzCVONltBPdUyKOkN%2FZZSSzyQcldAnKGrjAAer24sDHnmKZBJY9SFrcjHvspYJUx9QxnH1DqZHmbIIs9iKfQS%2FKlC5YjUMqAvwOMa22I0bSlHwM9SfXZdgkC2k%2B%2Fx%2BJgE9jsZhWxMIS7vc%2B%2BixCGpPtZ1NIjz5HZmuXjzY8U4H%2F%2F%2FrsT1mboTlz3wkBvYv4dHs3RY%2F6B7Qk4z0lPWmhzFVFeaeBpGJhXanNf2PB8MXV3vu%2BL7xEw%2FN120xGIgoKzpca4X9ZxdBf9ZL3bS6owyuOfvgY6nQHxZgJiUL1UMy4i%2BPRmuqyCniJrtQ0xPNChkfclz28JrLIQM4pHfa3G3UhFVxCbPdYI5K%2Bn9h58bUwh%2B67ViZtM3RfLIHZLM85ZfJX0SJdJSBC27bNijY%2FckR25ggXMuLi4nfeoM18q0K%2FdUmZ0eaTUZ3WK4s3rEyRgBTOS3tyLonGLqrebO4svJsDwlkOD9dapzf3YAqzvreB6znNo&Expires=1741160613", "evaluation_data": {"description": "A vibrant red apple with a stem on a wooden surface against a dark teal background.", "score": "10", "reason": "The image perfectly captures a realistic, high-quality representation of an apple with excellent detail and lighting.", "suggestions": "The image already perfectly fulfills the prompt. No improvements are necessary to better attain the original request."}}
Response headers
{
  "Content-Type": "application/json",
  "X-Amzn-Trace-Id": "Root=1-67c7f284-bd335200b648b2edd384d56d;Parent=397a2c413956b833;Sampled=0;Lineage=1:094f257a:0"
}
Logs
Execution log for request 3ad352c9-d207-4d23-8724-3fb995fc1650
Wed Mar 05 06:43:16 UTC 2025 : Starting execution for request: 3ad352c9-d207-4d23-8724-3fb995fc1650
Wed Mar 05 06:43:16 UTC 2025 : HTTP Method: POST, Resource Path: /generate-image
Wed Mar 05 06:43:16 UTC 2025 : Method request path: {}
Wed Mar 05 06:43:16 UTC 2025 : Method request query string: {}
Wed Mar 05 06:43:16 UTC 2025 : Method request headers: {}
Wed Mar 05 06:43:16 UTC 2025 : Method request body before transformations: { 
    "prompt": "Generate image of an apple" 
    
}
Wed Mar 05 06:43:16 UTC 2025 : Endpoint request URI: https://lambda.us-east-1.amazonaws.com/2015-03-31/functions/arn:aws:lambda:us-east-1:970547377074:function:lambda-gen-eval-image-bedrock/invocations
Wed Mar 05 06:43:16 UTC 2025 : Endpoint request headers: {X-Amz-Date=20250305T064316Z, x-amzn-apigateway-api-id=dt7ooeikdi, Accept=application/json, User-Agent=AmazonAPIGateway_dt7ooeikdi, Host=lambda.us-east-1.amazonaws.com, X-Amz-Content-Sha256=1fec15cfea7f81c2c039c481f971139f5fc4b183425fc1139c926cfe36cd3c3e, X-Amzn-Trace-Id=Root=1-67c7f284-bd335200b648b2edd384d56d, x-amzn-lambda-integration-tag=3ad352c9-d207-4d23-8724-3fb995fc1650, Authorization=*********************************************************************************************************************************************************************************************************************************************************************************************************************************************0526de, X-Amz-Source-Arn=arn:aws:execute-api:us-east-1:970547377074:dt7ooeikdi/test-invoke-stage/POST/generate-image, X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb//////////wEaCXVzLWVhc3QtMSJIMEYCIQDTEg1xqAXLjzXU+PR8VN/Svz72yqrsxY83ZibPUcx42wIhALwZ7IN/Vjs0NHtXDEJpqIPr01Ni+w [TRUNCATED]
Wed Mar 05 06:43:16 UTC 2025 : Endpoint request body after transformations: {"resource":"/generate-image","path":"/generate-image","httpMethod":"POST","headers":null,"multiValueHeaders":null,"queryStringParameters":null,"multiValueQueryStringParameters":null,"pathParameters":null,"stageVariables":null,"requestContext":{"resourceId":"mh5pln","resourcePath":"/generate-image","httpMethod":"POST","extendedRequestId":"G8LU1F3joAMFq_Q=","requestTime":"05/Mar/2025:06:43:16 +0000","path":"/generate-image","accountId":"970547377074","protocol":"HTTP/1.1","stage":"test-invoke-stage","domainPrefix":"testPrefix","requestTimeEpoch":1741156996984,"requestId":"3ad352c9-d207-4d23-8724-3fb995fc1650","identity":{"cognitoIdentityPoolId":null,"cognitoIdentityId":null,"apiKey":"test-invoke-api-key","principalOrgId":null,"cognitoAuthenticationType":null,"userArn":"arn:aws:iam::970547377074:user/Jay","apiKeyId":"test-invoke-api-key-id","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg [TRUNCATED]
Wed Mar 05 06:43:16 UTC 2025 : Sending request to https://lambda.us-east-1.amazonaws.com/2015-03-31/functions/arn:aws:lambda:us-east-1:970547377074:function:lambda-gen-eval-image-bedrock/invocations
Wed Mar 05 06:43:33 UTC 2025 : Received response. Status: 200, Integration latency: 16206 ms
Wed Mar 05 06:43:33 UTC 2025 : Endpoint response headers: {Date=Wed, 05 Mar 2025 06:43:33 GMT, Content-Type=application/json, Content-Length=1688, Connection=keep-alive, x-amzn-RequestId=7c4bda2e-d8f3-4b32-823d-670191e0dd7e, x-amzn-Remapped-Content-Length=0, X-Amz-Executed-Version=$LATEST, X-Amzn-Trace-Id=Root=1-67c7f284-bd335200b648b2edd384d56d;Parent=397a2c413956b833;Sampled=0;Lineage=1:094f257a:0}
Wed Mar 05 06:43:33 UTC 2025 : Endpoint response body before transformations: {"statusCode": 200, "body": "{\"url\": \"https://bog-images-meet-7.s3.amazonaws.com/image-gen-eval/e1fk3l2fhe.png?AWSAccessKeyId=ASIA6D6JBWOZIV3IMD2P&Signature=zoTePCIN%2FKorQLvnzJbjjDR8%2Frw%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCICLoU197TyUGH90ir22mVnrNXq03OQd1%2BMMGudwusZWUAiEA0iGMjdeF4uc%2BRZfa8yhOQ3z2PwSc5gA1Dtom6OxMhQwqjwMIEBAAGgw5NzA1NDczNzcwNzQiDB2Ia4g7OStawxX0zirsAnwFLeyjFW17rZU%2BX20tv0uOOTeIlk3IA4AJ8MWxeO4D1X0057Onyda0ZNfeScMJpMnsSVwUow0uHvV2vAr4OeKIU91YWvrDKs%2BhP%2FcmTWjq6l%2B2rNuVQMWkxZ7xyg2aXF2CcC8E2j3d5Hgj3qW%2B8CQ%2Fcv2fulQd9jx5aPbKOOsoGbly%2FPMOhfwnacZ9G09I90gQRSUBisaGJhjicq%2FgDzCVONltBPdUyKOkN%2FZZSSzyQcldAnKGrjAAer24sDHnmKZBJY9SFrcjHvspYJUx9QxnH1DqZHmbIIs9iKfQS%2FKlC5YjUMqAvwOMa22I0bSlHwM9SfXZdgkC2k%2B%2Fx%2BJgE9jsZhWxMIS7vc%2B%2BixCGpPtZ1NIjz5HZmuXjzY8U4H%2F%2F%2FrsT1mboTlz3wkBvYv4dHs3RY%2F6B7Qk4z0lPWmhzFVFeaeBpGJhXanNf2PB8MXV3vu%2BL7xEw%2FN120xGIgoKzpca4X9ZxdBf9ZL3bS6owyuOfvgY6nQHxZgJ [TRUNCATED]
Wed Mar 05 06:43:33 UTC 2025 : Method response body after transformations: {"url": "https://bog-images-meet-7.s3.amazonaws.com/image-gen-eval/e1fk3l2fhe.png?AWSAccessKeyId=ASIA6D6JBWOZIV3IMD2P&Signature=zoTePCIN%2FKorQLvnzJbjjDR8%2Frw%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCICLoU197TyUGH90ir22mVnrNXq03OQd1%2BMMGudwusZWUAiEA0iGMjdeF4uc%2BRZfa8yhOQ3z2PwSc5gA1Dtom6OxMhQwqjwMIEBAAGgw5NzA1NDczNzcwNzQiDB2Ia4g7OStawxX0zirsAnwFLeyjFW17rZU%2BX20tv0uOOTeIlk3IA4AJ8MWxeO4D1X0057Onyda0ZNfeScMJpMnsSVwUow0uHvV2vAr4OeKIU91YWvrDKs%2BhP%2FcmTWjq6l%2B2rNuVQMWkxZ7xyg2aXF2CcC8E2j3d5Hgj3qW%2B8CQ%2Fcv2fulQd9jx5aPbKOOsoGbly%2FPMOhfwnacZ9G09I90gQRSUBisaGJhjicq%2FgDzCVONltBPdUyKOkN%2FZZSSzyQcldAnKGrjAAer24sDHnmKZBJY9SFrcjHvspYJUx9QxnH1DqZHmbIIs9iKfQS%2FKlC5YjUMqAvwOMa22I0bSlHwM9SfXZdgkC2k%2B%2Fx%2BJgE9jsZhWxMIS7vc%2B%2BixCGpPtZ1NIjz5HZmuXjzY8U4H%2F%2F%2FrsT1mboTlz3wkBvYv4dHs3RY%2F6B7Qk4z0lPWmhzFVFeaeBpGJhXanNf2PB8MXV3vu%2BL7xEw%2FN120xGIgoKzpca4X9ZxdBf9ZL3bS6owyuOfvgY6nQHxZgJiUL1UMy4i%2BPRmuqyCniJrtQ0xPNChkfcl [TRUNCATED]
Wed Mar 05 06:43:33 UTC 2025 : Method response headers: {Content-Type=application/json, X-Amzn-Trace-Id=Root=1-67c7f284-bd335200b648b2edd384d56d;Parent=397a2c413956b833;Sampled=0;Lineage=1:094f257a:0}
Wed Mar 05 06:43:33 UTC 2025 : Successfully completed execution
Wed Mar 05 06:43:33 UTC 2025 : Method completed with status: 200
```

### To avoid incurring future charges, clean up all the AWS resources that you created using CloudFormation.