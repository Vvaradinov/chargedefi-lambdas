from pymongo import MongoClient
from pprint import pprint
from utils import default_serializer
import json
from datetime import datetime


client = MongoClient("")
db = client.chargedefi
lp_table = db.boardroom_lp
single_token_table = db.boardroom_charge


def main(event, context):
    if event['queryStringParameters']["wallet_address"]:
        is_single_token = event['queryStringParameters']['is_single_token']
        wallet_address = event['queryStringParameters']['wallet_address']

        if is_single_token == 'True':
            data = json.dumps(list(single_token_table.find({"wallet_address": wallet_address})), default=default_serializer)
            return {
                'statusCode': 200,
                'body': data,
                "headers": {"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Methods": "GET, OPTIONS"}
            }

        data = json.dumps(list(lp_table.find({"wallet_address": wallet_address})), default=default_serializer)
        return {
            "statusCode": 200,
            "body": data,
            "headers": {"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Methods": "GET, OPTIONS"}
        }
