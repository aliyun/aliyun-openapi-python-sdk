
test-all: lint test functional-test

lint:
	pycodestyle --statistics aliyun-python-sdk-core/  --max-line-length=100 --ignore=W391,E121,E123,E126,E226,E24,E704,W503,W504 --exclude=DescribeEndpointsRequest.py,vendored
	pycodestyle --statistics python-sdk-functional-test/  --max-line-length=100 --ignore=W391,E121,E123,E126,E226,E24,E704,W503,W504

test:
	coverage run --branch -m pytest aliyun-python-sdk-core/tests/
	coverage report --include="aliyun-python-sdk-core/aliyunsdkcore/*" --omit="aliyun-python-sdk-core/aliyunsdkcore/vendored/*,aliyun-python-sdk-core/aliyunsdkcore/compat.py"
	coverage html --include="aliyun-python-sdk-core/aliyunsdkcore/*" --omit="aliyun-python-sdk-core/aliyunsdkcore/vendored/*,aliyun-python-sdk-core/aliyunsdkcore/compat.py"

functional-test:
	cd python-sdk-functional-test && bash -e run_all_test.sh
