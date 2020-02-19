from __future__ import print_function # Python 2/3 compatibility
import boto3, pprint

# create the resource we need to connect.
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

# get the table object
table = dynamodb.Table("MyTable")  # Substitute your table name for MyTable

# get the table limits from the table object
response = table.meta.client.describe_limits()

pprint.pprint(response)