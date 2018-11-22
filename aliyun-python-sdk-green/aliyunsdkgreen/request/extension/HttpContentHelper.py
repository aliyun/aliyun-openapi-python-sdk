# coding=utf-8
import json
import sys

def toValue(jsonObject):
    # 用于python2
    if sys.version_info[0] == 2:
        return bytearray(json.dumps(jsonObject), 'utf-8')
    # 用于python3
    return json.dumps(jsonObject)
