
all: pep8 coverage unittest functional-test

pep8:
	pep8 aliyun-python-sdk-core/ --show-source --show-pep8 --max-line-length=100
	pep8 python-sdk-functional-test/ --show-source --show-pep8 --max-line-length=100

coverage:
	cd aliyun-python-sdk-core; coverage run --branch -m pytest tests/
	cd aliyun-python-sdk-core; coverage report --include="aliyunsdkcore/*" --omit="aliyunsdkcore/vendored/*"
	cd aliyun-python-sdk-core; coverage html --include="aliyunsdkcore/*" --omit="aliyunsdkcore/vendored/*"
