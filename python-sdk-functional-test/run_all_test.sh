cd ..

for i in `ls | grep aliyun-python-sdk-`; do
    echo "Adding $i to PYTHONPATH ..."
    export PYTHONPATH=$PYTHONPATH:`pwd`/$i > /dev/null
done

cd -

coverage run --branch -m pytest
