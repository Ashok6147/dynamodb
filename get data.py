import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DemodataBase')
response = table.get_item(
    Key={
        'ID': '003',
        'name' : 'ashok'
    }
)
item = response['Item']
print(item)