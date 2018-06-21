#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import os
import boto3
from botocore.exceptions import ClientError

def main():
    """ Bootstrap a dynamodb instance for local development """

    REGION='ca-central-1'
    DYNAMODB_LOCAL_NETWORK = 'muphone-local-dev'
    PWD = os.getenv('PWD')
    ENDPOINT = 'http://localhost:8000'

    subprocess.call(['docker','container','prune','-f'])
    subprocess.call(['docker','network','prune','-f'])

    subprocess.call(['docker','network','create',DYNAMODB_LOCAL_NETWORK])

    subprocess.call(
            [
                'docker',
                'run',
                '-d',
                '-v',
                '{}:/dynamodb_local_db'.format(PWD),
                '-p',
                '8000:8000',
                '--network',
                DYNAMODB_LOCAL_NETWORK,
                '--name',
                'dynamodb',
                'cnadiminti/dynamodb-local'
            ])

    # dynamodb init
    dynamodb = boto3.resource('dynamodb', region_name=REGION, endpoint_url=ENDPOINT)

    def create_table(table_name, key_name):
        params = {
                    "TableName":table_name,
                    "KeySchema": [
                        {
                            "AttributeName":key_name,
                            "KeyType":"HASH"
                        }
                    ],
                    "AttributeDefinitions": [
                        {
                            "AttributeName":key_name,
                            "AttributeType":'S'
                        }
                    ],
                    "ProvisionedThroughput": {
                        'ReadCapacityUnits': 1,
                        'WriteCapacityUnits': 1
                    }
            }

        table = dynamodb.create_table(**params)
        table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
        return table

    def table_exists(table_name):
        """Quick check on table"""
        try:
            table = dynamodb.Table(table_name)
            if "ACTIVE" in table.table_status:
                return True
        except ClientError as error_message:
            return False


    tables = [ ('phone','number') ]

    for table_name, key_name in tables:
        if table_exists(table_name):
            print('table: {} already exists, skipping'.format(table_name))
            continue
        else:

            print('creating table: {}'.format(table_name))
            create_table(table_name, key_name)

    print('your dynamodb local instance is ready to use (specify --docker-network {} when invoking sam local)'.format(DYNAMODB_LOCAL_NETWORK))


if __name__ == '__main__':
    main()

