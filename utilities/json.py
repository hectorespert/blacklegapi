from json import JSONEncoder, dumps
from datetime import date

__author__ = 'Blackleg'


class ExtendedJsonEncoder(JSONEncoder):
    def default(self, obj):
        """if isinstance(obj, (datetime.datetime,)):
            return {"val": obj.isoformat(), "_spec_type": "datetime"}
        elif isinstance(obj, (decimal.Decimal,)):
            return {"val": str(obj), "_spec_type": "decimal"}
        else:"""
        if isinstance(obj, date):
            return obj.isoformat()
        else:
            return super().default(obj)


def parseObjectToJson(object):
    if isinstance(object, dict):
        return dumps(object, cls=ExtendedJsonEncoder)
    else:
        return parseObjectToJson(object.__dict__)


