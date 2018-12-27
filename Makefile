
test-all: lint test

lint:
	pycodestyle aliyun-python-sdk-core/  --max-line-length=100 --ignore=W391,E121,E123,E126,E226,E24,E704,W503,W504 --exclude=DescribeEndpointsRequest.py,vendored
	pycodestyle python-sdk-functional-test/  --max-line-length=100 --ignore=W391,E121,E123,E126,E226,E24,E704,W503,W504

test:
	coverage run --branch -m pytest aliyun-python-sdk-core/tests/
	coverage report --include="aliyun-python-sdk-core/aliyunsdkcore/*" --omit="aliyunsdkcore/vendored/*"
	coverage html --include="aliyun-python-sdk-core/aliyunsdkcore/*" --omit="aliyunsdkcore/vendored/*"

functional-test:
	cd python-sdk-functional-test; bash -e run_all_test.sh
