#!/bin/zsh
aws ec2 run-instances --image-id ami-0b0dcb5067f052a63 \
    --count 1 \
    --instance-type t2.micro \
    --key-name devops2202 \
    --region us-east-1

aws cloudformation validate-template \
    --template-body file://create-ec2.yaml

aws cloudformation create-change-set \
    --stack-name my-application \
    --change-set-name ec2-chnageset \
    --template-body file://create-ec2.yaml \
    --capabilities CAPABILITY_IAM \
    --change-set-type CREATE

aws cloudformation execute-change-set \
    --change-set-name ec2-chnageset \
    --stack-name my-application

aws cloudformation create-change-set \
    --stack-name my-application \
    --change-set-name ec2-chnageset \
    --template-body file://create-ec2.yaml \
    --capabilities CAPABILITY_IAM \
    --change-set-type UPDATE

aws cloudformation delete-stack \
    --stack-name my-application

