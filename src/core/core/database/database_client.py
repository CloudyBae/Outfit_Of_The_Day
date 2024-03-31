import logging
import os
from functools import cache
import boto3
from botocore.exceptions import ClientError

RESOURCE_ENV = os.environ['RESOURCE_ENV']
DYNAMO_TABLE_NAME = "/Ootd/{}/OotdDdbName".format(RESOURCE_ENV)

@cache
def table_name() -> str:
    return boto3.client('ssm').get_parameter(Name=DYNAMO_TABLE_NAME)['Parameter']['Value']

class DdbTable:
    def __init__(self, table_name: str):
        self.table_name = table_name
        self.table = boto3.resource('dynamodb').Table(table_name)
    
    @cache    
    def _table(self):
        return self.table   
        
    def _put_item(self, item):
        try:
            self._table().put_item(item)
            
        except ClientError as e:
            logging.error(f"Failed putting {item} into {self.table_name} table")
