from key import *

import pprint as pp
import boto3

translate = boto3.client(
    'translate',
    region_name='us-east-1',
    aws_access_key_id=AWS_KEY_ID,
    aws_secret_access_key=AWS_SECRET
    )

response = translate.translate_text(
    Text='Hello, how are you?',
    SourceLanguageCode='auto',
    TargetLanguageCode='ar'
    )

pp.pprint(response['TranslatedText'])
