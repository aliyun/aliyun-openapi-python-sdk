# Alibaba Cloud Python Software Development Kit
[中文文档](./README_zh.md)

The Alibaba Cloud Python Software Development Kit (SDK) allows you to access Alibaba Cloud services such as Elastic Compute Service (ECS), Object Storage Service (OSS), and Resource Access Management (RAM).  You can access Alibaba Cloud services without the need to handle API related tasks, such as signing and constructing your requests.

This document introduces how to obtain and call Alibaba Cloud Python SDK.

## Prerequisites

- To use Alibaba Cloud Python SDK, you must have an Alibaba Cloud account as well as an AccessKey.

	The AccessKey is required when initializing `AcsClient`. You can create an AccessKey in the Alibaba Cloud console. For more information, see [Create an AccessKey](~~53045~~).

	>**Note:** To increase the security of your account, we recommend that you use the AccessKey of the RAM user to access Alibaba Cloud services.

- To use Alibaba Cloud Python SDK to access the APIs of a product, you must first activate the product on the [Alibaba Cloud console](https://home.console.aliyun.com/?spm=5176.doc52740.2.4.QKZk8w) if required.

- Alibaba Cloud Python SDK requires 2.6.x, 2.7.x, and Python 3.x.


## Install Python SDK

Alibaba Cloud Python SDK supports Python 2.6.x, 2.7.x, and Python 3.x. Run ``python --version`` to check your version of Python.

You can install the Alibaba Cloud Python SDK using the following two methods. Regardless of which method and cloud service are used, the core library `aliyun-python-sdk-core` must be installed. You can download the product SDKs from [Python SDK resource list](~~62188~~).

- **Install with pip**

	Python SDK uses a common package management tool named `pip`. If pip is not installed, see the [pip user guide](https://pip.pypa.io/en/stable/installing/?spm=5176.doc53090.2.7.zHDiNV "pip User Guide") to install pip.

	Run the following command to install the individual libraries of Alibaba Cloud services:

	```python
	# Install the core library
	pip install aliyun-python-sdk-core
	# Install the ECS management library
	pip install aliyun-python-sdk-ecs
	# Install the RDS management library
	pip install aliyun-python-sdk-rds
```
>**Note:** If you are using Python 3.x, run the following command to install the core library:

	>`pip install aliyun-python-sdk-core-v3`

- **Install from GitHub**

	You can clone the source code to your local folder and then run `setup.py install` to install the SDK:
	```
	git clone https://github.com/aliyun/aliyun-openapi-python-sdk.git
	# Install the core library
	cd aliyun-python-sdk-core
	python setup.py install
	# Install the ECS management library
	cd aliyun-python-sdk-ecs
	python setup.py install
	```

## Use Python SDK

1. Import the required modules as follows:

	```python
  from aliyunsdkcore.client import AcsClient
  from aliyunsdkcore.acs_exception.exceptions import ClientException
  from aliyunsdkcore.acs_exception.exceptions import ServerException
  from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
  from aliyunsdkecs.request.v20140526 import StopInstanceRequest
```
2. Initialize the `AcsClient` instance:

	```python
	  client = AcsClient(
		  "<access-key-id>", 
		  "<access-key-secret>",
		  "<region-id>"
	  );

	```

	where:

	- `access-key-id` is the Accesskey ID for your account.

	- `access-key-secret` is the AccessKey secret for your account.

	- `region-id` is the ID of the region where the service is called. For a list of region IDs, see [Regions and zones](~~40654~~).

	>**Note:** The sequence of these parameters cannot be changed. 

3. Initialize a request and print response.

	```python
	  #  Initialize a request and set parameters
	  request = DescribeInstancesRequest.DescribeInstancesRequest()
	  request.set_PageSize(10)
	  # Print response
	  response = client.do_action_with_exception(request)
	  print response
	```

	##Code example

	The following example shows how to query a list of ECS instances in a specific region using [DescribeInstances](~~25506~~). Substitute the values for `your-access-key-id`, `your-access-key-secret`, and `your-region-id`.

	```python
	  # -*- coding: utf8 -*-

	  from aliyunsdkcore.client import AcsClient
	  from aliyunsdkcore.acs_exception.exceptions import ClientException
	  from aliyunsdkcore.acs_exception.exceptions import ServerException
	  from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
	  from aliyunsdkecs.request.v20140526 import StopInstanceRequest

	  # Initialize AcsClient instance
	  client = AcsClient(
		  "<your-access-key-id>", 
		  "<your-access-key-secret>",
		  "<your-region-id>"
	  );

	  # Initialize a request and set parameters
	  request = DescribeInstancesRequest.DescribeInstancesRequest()
	  request.set_PageSize(10)

	  # Print response
	  response = client.do_action_with_exception(request)
	  print response
	```