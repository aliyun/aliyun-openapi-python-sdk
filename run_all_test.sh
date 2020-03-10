
export PYTHONPATH=$PYTHONPATH:`ls | grep aliyun-python-sdk- | xargs | sed 's/ /:/g'`
for i in `ls | grep aliyun-python-sdk-`; do
    echo "Adding $i to PYTHONPATH ..."
    export PYTHONPATH=$PYTHONPATH:`pwd`/$i > /dev/null
done

python --version
pip --version
coverage run -a --source="./aliyun-python-sdk-core/aliyunsdkcore" --branch -m pytest python-sdk-functional-test
