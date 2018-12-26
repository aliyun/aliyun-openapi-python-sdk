cd ..

for i in `ls --color=never | grep aliyun-python-sdk-`; do
    echo "Adding $i to PYTHONPATH ..."
    export PYTHONPATH=$PYTHONPATH:`pwd`/$i > /dev/null
done

cd -

python -m unittest discover -s . -p '*_test.py'
