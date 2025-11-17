# S3 → Lambda Categorizer

This project stores incoming files in S3 and triggers a Lambda function to process and categorize them.

## How it works
1. Create an S3 bucket.
2. Upload a file to the bucket.
3. S3 triggers the Lambda function.
4. Lambda reads the file and performs simple categorization.

## AWS Services Used
- Amazon S3
- AWS Lambda
- IAM
