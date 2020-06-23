from key import *

import pprint as pp
import boto3

s3 = boto3.client('s3', region_name = 'us-east-1',
                  aws_access_key_id = AWS_KEY_ID,
                  aws_secret_access_key = AWS_SECRET)


response = s3.upload_file(Filename='upload/0000.jpeg', Key='texting.jpeg', Bucket='shokr-1862020')
pp.pprint(response)

################################### rekog ##################################################

rekog = boto3.client(
    'rekognition',
    region_name='us-east-1',
    aws_access_key_id=AWS_KEY_ID,
    aws_secret_access_key=AWS_SECRET)


response = rekog.detect_labels(
    Image={'S3Object': {
        'Bucket': 'shokr-1862020',
        'Name': '000000.jpeg'
        }}
    )

pp.pprint(response)

print('----------------------------------------------------------------------------------')

response = rekog.detect_text(
    Image={'S3Object':
        {
            'Bucket': 'shokr-1862020',
            'Name': 'texting.jpeg'
        }
    }
)

pp.pprint(response)
print('----------------------------------------------------------------------------------')

