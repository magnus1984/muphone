#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3

SNS_REGION = 'us-east-1'

def sms(mobile, message):
    sns = boto3.client('sns', region_name=SNS_REGION)
    sns.publish(PhoneNumber=mobile, Message=message)
    return
