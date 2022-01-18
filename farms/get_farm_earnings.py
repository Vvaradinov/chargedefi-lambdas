from pymongo import MongoClient
from utils import default_serializer
import json

client = MongoClient("")
db = client.chargedefi
farms_static_table = db.farms_static
farms_charge_table = db.farms_charge


def main(event, context):
    if event['queryStringParameters']["wallet_address"]:
        farm_type = event['queryStringParameters']['farm_type']
        wallet_address = event['queryStringParameters']['wallet_address']

        if farm_type == 'static':
            data = json.dumps(list(farms_static_table.find({"wallet_address": wallet_address})), default=default_serializer)
            return {
                'statusCode': 200,
                'body': data,
                "headers": {"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Methods": "GET, OPTIONS"}
            }

        data = json.dumps(list(farms_charge_table.find({"wallet_address": wallet_address})), default=default_serializer)
        return {
            "statusCode": 200,
            "body": data,
            "headers": {"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Methods": "GET, OPTIONS"}
        }
