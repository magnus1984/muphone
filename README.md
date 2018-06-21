# muphone
A phone ownership validation microservice 

## Introduction
muphone is an AWS lambda microservice that allows you to validate ownership of a 
user provided phone number. This is frequently needed in "sign up" scenarios on 
many websites. Here are the typical steps of a validation workflow:

1. A user submits a phone number through a form on your website.
2. The user is sent a generated validation code at the phone number provided.
3. The user submits the received validation code and the phone number is 
verified.

The service is RESTful and can easily integrate with any http clients 
available.

## Setup
Firt, create a local runtime environment and install all the dependencies 
in muphone/build to prepare for deployment on AWS lambda:

```bash
git clone https://github.com/magnus1984/muphone.git
cd muphone
virtualenv -p python3.6 .runtimeenv
source .runtimeenv/bin/activate
pip install -r requirements.txt -t muphone/build
cp muphone/*.py muphone/build
```

The API should now be ready for deployment.

## Deploy
The microservice uses AWS CloudFormation for automated deployment. Once you have 
completed the setup steps, you can deploy using the aws cli

```bash
aws cloudformation package --template-file template.yaml --s3-bucket <YOUR-S3-BUCKET> --output-template-file packaged.yaml
aws cloudformation deploy --template-file packaged.yaml --stack-name <YOUR-STACK-NAME> --capabilities CAPABILITY_IAM
```

Once deployed, you can get the url of your endpoint by querying the stack
```bash
aws cloudformation describe-stacks --stack-name <YOUR-STACK-NAME> --query 'Stacks[0].Outputs[0].OutputValue'
```

## Usage Examples
Example use [httpie](https://httpie.org/) for the client library

### Submit a phone number for validation
```bash
http POST https://your.url.endpoint/phone number=<YOUR-PHONE-NUMBER>
```

### Get a phone number status
```bash
http GET https://your.url.endpoint/phone number==<YOUR-E164-FORMATTED-NUMBER>
```

NOTE: the api automatically persist in a dynamodb table the phone number submitted
in the E164 format. To query the status of a previously submitted number, it is 
your responsability to convert to the E164 format.

### Validate a phone number
```bash
http POST https://your.url.endpoint/phone/validation number=<YOUR-PHONE-NUMBER> validation_code=<YOUR-VALIDATION-CODE>
```

## Live Demo
There is a live demo available here: https://cmx94tf3ee.execute-api.ca-central-1.amazonaws.com/Prod/

## Author
Jonathan Pelletier (jomagnus1984@gmail.com, jonathan.pelletier1@gmail.com)
