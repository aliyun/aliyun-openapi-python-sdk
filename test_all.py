import os
from subprocess import check_call, CalledProcessError

cur_path = os.path.abspath('.')
path_list = []
for ret in os.walk(cur_path):
    root_path = ret[0]
    root_path_list = root_path.split('\\')
    if root_path_list[-1].startswith('aliyun-python-sdk'):
        path_list.append(root_path)

os.environ.__setitem__('PYTHONPATH', ';'.join(path_list))

try:
    check_call(
        "coverage run --branch -m pytest python-sdk-functional-test/", shell=True)

except CalledProcessError as e:
    raise

