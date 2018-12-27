cd ..

for i in `ls --color=never | grep aliyun-python-sdk-`; do
    echo "Adding $i to PYTHONPATH ..."
    export PYTHONPATH=$PYTHONPATH:`pwd`/$i > /dev/null
done

cd -
 
if python -m unittest base.SDKTestBase; then
    python -m unittest discover -s . -p '*_test.py'
else
    echo "WARN: Test Env not available, Function test Skipped."
    exit 0
fi
junmei.zjm