import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    return json.dump(my_obj,)
d = to_json_string(5)
print(d)