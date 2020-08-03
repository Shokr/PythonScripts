import boto3
from key import *

s3 = boto3.client(
    "s3",
    region_name="us-east-1",
    aws_access_key_id=AWS_KEY_ID,
    aws_secret_access_key=AWS_SECRET,
)

s3.upload_file(Filename="upload/allah.png",
               Bucket="shokr-1862020",
               Key="testing.png")

# Set ACL to 'public-read'

s3.put_object_acl(Bucket="shokr-1862020", Key="testing.png", ACL="public-read")

# Upload le with 'public-read' ACL

s3.upload_file(
    Bucket="shokr-1862020",
    Filename="upload/moi.csv",
    Key="mx.csv",
    ExtraArgs={"ACL": "public-read"},
)
