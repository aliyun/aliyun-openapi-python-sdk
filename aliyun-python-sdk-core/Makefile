
all:
	coverage run --branch -m pytest tests/
	coverage report --include="aliyunsdkcore/*" --omit="aliyunsdkcore/vendored/*"
	coverage html --include="aliyunsdkcore/*" --omit="aliyunsdkcore/vendored/*"
