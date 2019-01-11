
export PYTHONPATH=$PYTHONPATH:`ls | grep aliyun-python-sdk- | xargs | sed 's/ /:/g'`
for i in `ls | grep aliyun-python-sdk-`; do
    echo "Adding $i to PYTHONPATH ..."
    export PYTHONPATH=$PYTHONPATH:`pwd`/$i > /dev/null
done


coverage run --branch -m pytest python-sdk-functional-test
