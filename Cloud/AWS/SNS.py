from key import *

import pprint as pp
import boto3

sns = boto3.client('sns', region_name = 'us-east-1',
                   aws_access_key_id = AWS_KEY_ID,
                   aws_secret_access_key = AWS_SECRET)

response = sns.create_topic(Name = 'fast_alerts')
topic_arn = response['TopicArn']

pp.pprint(topic_arn)

response = sns.list_topics()
pp.pprint(response['Topics'])

sns.delete_topic(TopicArn = 'arn:aws:sns:us-east-1:052844596419:ShokrSNS')

# Creating an SMS subscription.

response = sns.subscribe(
    TopicArn = 'arn:aws:sns:us-east-1:052844596419:fast_alerts',
    Protocol = 'SMS',
    Endpoint = '+201289859363'
)

pp.pprint(response)

# Creating an email subscription

response = sns.subscribe(
    TopicArn = 'arn:aws:sns:us-east-1:052844596419:fast_alerts',
    Protocol = 'email',
    Endpoint = 'mohammedshokr2014@gmail.com'
)

pp.pprint(response)

# Listing subscriptions

response = sns.list_subscriptions_by_topic(
    TopicArn = 'arn:aws:sns:us-east-1:052844596419:fast_alerts'
)

pp.pprint(response)

response = sns.list_subscriptions()['Subscriptions']
pp.pprint(response)

# Deleting subscriptions

sns.unsubscribe(
    SubscriptionArn = 'arn:aws:sns:us-east-1:052844596419:fast_alerts:b0483383-5c13-4c5c-8621-cfe4e564bf0e'
)

# Publishing to a Topic

MyName = 'SHOKR'

response = sns.publish(
    TopicArn = 'arn:aws:sns:us-east-1:052844596419:fast_alerts',
    Message = 'Hello {}, Body text of SMS or e-mail'.format(MyName),
    Subject = 'Subject Line for Email'
)

pp.pprint(response)

response = sns.publish(
    PhoneNumber = '+201274881880',
    Message = 'You get one life, so do it all.'
)

pp.pprint(response)
