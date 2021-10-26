import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DemidataBase')
table.delete_item(
   key={
        'ID': '004',
        'phone':'9113266608'
    }
)
