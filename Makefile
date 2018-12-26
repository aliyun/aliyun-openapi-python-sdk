
all: pep8 coverage functional-test

pep8:
	pycodestyle aliyun-python-sdk-core/  --max-line-length=100 --ignore=W391,E121,E123,E126,E226,E24,E704,W503,W504 --exclude=DescribeEndpointsRequest.py,vendored
	pycodestyle python-sdk-functional-test/  --max-line-length=100 --ignore=W391,E121,E123,E126,E226,E24,E704,W503,W504

coverage:
	cd aliyun-python-sdk-core; coverage run --branch -m pytest tests/
	cd aliyun-python-sdk-core; coverage report --include="aliyunsdkcore/*" --omit="aliyunsdkcore/vendored/*"
	cd aliyun-python-sdk-core; coverage html --include="aliyunsdkcore/*" --omit="aliyunsdkcore/vendored/*"

functional-test:
	cd python-sdk-functional-test; bash -e run_all_test.sh
