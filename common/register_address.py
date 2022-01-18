from pymongo import MongoClient
from datetime import datetime


def main(wallet_address):
    client = MongoClient("")
    db = client.chargedefi
    users = db.users
    address = users.find_one({"wallet_address": wallet_address})
    if not address:
        users.insert_one({"wallet_address": wallet_address, "date": datetime.utcnow()})


# if __name__ == '__main__':
#     main()