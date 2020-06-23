from key import *

import pprint as pp
import boto3

s3 = boto3.client('s3', region_name = 'us-east-1',
                  aws_access_key_id = AWS_KEY_ID,
                  aws_secret_access_key = AWS_SECRET)

bucket = s3.create_bucket(Bucket = 'shokr-1862020')

bucket_response = s3.list_buckets()
buckets = bucket_response['Buckets']
pp.pprint(buckets)

response = s3.delete_bucket(Bucket = 'shokr-1862020')


s3.upload_file(
    Filename='upload/allah.png',
    Bucket='shokr-1862020',
    Key='1.png')


response = s3.list_objects(Bucket='shokr-1862020')

response = s3.head_object(Bucket='shokr-1862020', Key='1.png')

pp.pprint(response)

s3.download_file(Filename='download/ALLAH.png', Bucket='shokr-1862020', Key='1.png')

s3.delete_object(Bucket='shokr-1862020', Key='1.png')