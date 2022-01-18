import datetime

def default_serializer(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

