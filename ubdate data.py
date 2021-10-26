import boto3
dynamodb = boto3.resources('dynamodb')
table = dynamodb.Table('DemodataBase')
table.update_item(
    Key={
        'ID': '004',
        'phone': '9113266608'
    },
    UpdateExpression='name = :string1',
    ExpressionAttributeValues={
        ':string1': 'ashok kumar'
    }
)
response = table.get_item(
    Key={
        'ID': '004',
        'phone': '9113266608'
    }
)
item = response['Item']
print(item)