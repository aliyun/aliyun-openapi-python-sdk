cd ..

for i in `ls | grep aliyun-python-sdk-`; do
    echo "Adding $i to PYTHONPATH ..."
    export PYTHONPATH=$PYTHONPATH:`pwd`/$i > /dev/null
done

cd -

PYTHON_VERSION=`python --version 2>&1 | cut -d ' ' -f 2 | cut -d . -f 1,2`
if [ $PYTHON_VERSION == '2.6' ]; then
    echo "Using unittest2 for functional test ..."
    coverage run --branch -m unittest2 discover -s . -p "*_test.py"
else
    echo "Using unittest for functional test ..."
    coverage run --branch -m unittest discover -s . -p "*_test.py"
fi
