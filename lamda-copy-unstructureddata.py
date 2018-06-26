import os
import urllib
import boto3
import ast
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    sns_message = ast.literal_eval(event['Records'][0]['Sns']['Message'])
    target_bucket = 'datalake-curated-datasets-783529447247-us-west-2'
    source_bucket = str(sns_message['Records'][0]['s3']['bucket']['name'])
    key = urllib.unquote_plus(sns_message["Records"][0]["s3"]["object"]["key"])
    copy_source = {'Bucket':source_bucket, 'Key':key}
    path = os.path.join('apache_logdata/', key)
    s3.copy_object(Bucket=target_bucket, Key=path, CopySource=copy_source)
