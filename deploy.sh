#!/usr/bin/env sh

cp muphone/*.py muphone/build
aws cloudformation package --template-file template.yaml --s3-bucket muphone --output-template-file packaged.yaml
aws cloudformation deploy --template-file packaged.yaml --stack-name muphone-prod --capabilities CAPABILITY_IAM
