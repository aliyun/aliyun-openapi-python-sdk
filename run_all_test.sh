#!/bin/bash

export PYTHONPATH="$PYTHONPATH":$(ls | grep aliyun-python-sdk- | xargs | sed 's/ /:/g')
for i in $(ls | grep aliyun-python-sdk-); do
    # Add to PYTHONPATH
    export PYTHONPATH="$PYTHONPATH":$(pwd)/"$i" > /dev/null
done

coverage run -a --source="./aliyun-python-sdk-core/aliyunsdkcore" --branch -m pytest python-sdk-functional-test
