# # Licensed to the Apache Software Foundation (ASF) under one
# # or more contributor license agreements.  See the NOTICE file
# # distributed with this work for additional information
# # regarding copyright ownership.  The ASF licenses this file
# # to you under the Apache License, Version 2.0 (the
# # "License"); you may not use this file except in compliance
# # with the License.  You may obtain a copy of the License at
# #
# #
# #     http://www.apache.org/licenses/LICENSE-2.0
# #
# #
# # Unless required by applicable law or agreed to in writing,
# # software distributed under the License is distributed on an
# # "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# # KIND, either express or implied.  See the License for the
# # specific language governing permissions and limitations
# # under the License.


class EndpointData():
	def __init__(self):
		self.endpoint_map = {
			"cn-shanghai-internal-test-1": "cloudpush.aliyuncs.com",
			"cn-shenzhen-su18-b01": "cloudpush.aliyuncs.com",
			"cn-beijing": "cloudpush.aliyuncs.com",
			"cn-shanghai-inner": "cloudpush.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "cloudpush.aliyuncs.com",
			"cn-north-2-gov-1": "cloudpush.aliyuncs.com",
			"cn-yushanfang": "cloudpush.aliyuncs.com",
			"cn-qingdao-nebula": "cloudpush.aliyuncs.com",
			"cn-beijing-finance-pop": "cloudpush.aliyuncs.com",
			"cn-wuhan": "cloudpush.aliyuncs.com",
			"cn-zhangjiakou": "cloudpush.aliyuncs.com",
			"us-west-1": "cloudpush.aliyuncs.com",
			"rus-west-1-pop": "cloudpush.aliyuncs.com",
			"cn-shanghai-et15-b01": "cloudpush.aliyuncs.com",
			"cn-hangzhou-bj-b01": "cloudpush.aliyuncs.com",
			"cn-zhangbei-na61-b01": "cloudpush.aliyuncs.com",
			"ap-northeast-1": "cloudpush.aliyuncs.com",
			"cn-shanghai-et2-b01": "cloudpush.aliyuncs.com",
			"ap-southeast-1": "cloudpush.aliyuncs.com",
			"ap-southeast-2": "cloudpush.aliyuncs.com",
			"ap-southeast-3": "cloudpush.aliyuncs.com",
			"ap-southeast-5": "cloudpush.aliyuncs.com",
			"us-east-1": "cloudpush.aliyuncs.com",
			"cn-shenzhen-inner": "cloudpush.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "cloudpush.aliyuncs.com",
			"cn-beijing-gov-1": "cloudpush.aliyuncs.com",
			"ap-south-1": "cloudpush.aliyuncs.com",
			"cn-shenzhen-st4-d01": "cloudpush.aliyuncs.com",
			"cn-haidian-cm12-c01": "cloudpush.aliyuncs.com",
			"cn-qingdao": "cloudpush.aliyuncs.com",
			"cn-hongkong-finance-pop": "cloudpush.aliyuncs.com",
			"cn-shanghai": "cloudpush.aliyuncs.com",
			"cn-shanghai-finance-1": "cloudpush.aliyuncs.com",
			"cn-hongkong": "cloudpush.aliyuncs.com",
			"eu-central-1": "cloudpush.aliyuncs.com",
			"cn-shenzhen": "cloudpush.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "cloudpush.aliyuncs.com",
			"eu-west-1": "cloudpush.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "cloudpush.aliyuncs.com",
			"eu-west-1-oxs": "cloudpush.aliyuncs.com",
			"cn-beijing-finance-1": "cloudpush.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "cloudpush.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "cloudpush.aliyuncs.com",
			"cn-shenzhen-finance-1": "cloudpush.aliyuncs.com",
			"me-east-1": "cloudpush.aliyuncs.com",
			"cn-chengdu": "cloudpush.aliyuncs.com",
			"cn-hangzhou-test-306": "cloudpush.aliyuncs.com",
			"cn-hangzhou-finance": "cloudpush.aliyuncs.com",
			"cn-beijing-nu16-b01": "cloudpush.aliyuncs.com",
			"cn-edge-1": "cloudpush.aliyuncs.com",
			"cn-huhehaote": "cloudpush.aliyuncs.com",
			"cn-fujian": "cloudpush.aliyuncs.com",
			"ap-northeast-2-pop": "cloudpush.aliyuncs.com",
			"cn-hangzhou": "cloudpush.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
