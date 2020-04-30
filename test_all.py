import os
from subprocess import check_call
access_key_id = os.environ.get('ACCESS_KEY_ID')
access_key_secret = os.environ.get('ACCESS_KEY_SECRET')
if access_key_id and access_key_secret:
    cur_path = os.path.abspath('.')
    path_list = []
    for ret in os.walk(cur_path):
        root_path = ret[0]
        root_path_list = root_path.split('\\')
        if root_path_list[-1].startswith('aliyun-python-sdk'):
            path_list.append(root_path)

    os.environ.__setitem__('PYTHONPATH', ';'.join(path_list))

    check_call(
        'coverage run --branch --source="./aliyun-python-sdk-core/aliyunsdkcore" -m pytest python-sdk-functional-test/',
        shell=True)

def test_coverage():pass
