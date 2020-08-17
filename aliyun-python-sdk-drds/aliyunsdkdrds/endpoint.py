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
			"cn-shanghai-internal-test-1": "drds.aliyuncs.com",
			"cn-beijing-gov-1": "drds.aliyuncs.com",
			"cn-shenzhen-su18-b01": "drds.aliyuncs.com",
			"ap-south-1": "drds.ap-southeast-1.aliyuncs.com",
			"cn-shanghai-inner": "drds.aliyuncs.com",
			"cn-shenzhen-st4-d01": "drds.aliyuncs.com",
			"cn-haidian-cm12-c01": "drds.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "drds.aliyuncs.com",
			"cn-yushanfang": "drds.aliyuncs.com",
			"cn-hongkong-finance-pop": "drds.aliyuncs.com",
			"cn-qingdao-nebula": "drds.aliyuncs.com",
			"cn-beijing-finance-pop": "drds.aliyuncs.com",
			"cn-wuhan": "drds.aliyuncs.com",
			"eu-central-1": "drds.ap-southeast-1.aliyuncs.com",
			"us-west-1": "drds.ap-southeast-1.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "drds.aliyuncs.com",
			"rus-west-1-pop": "drds.ap-southeast-1.aliyuncs.com",
			"cn-shanghai-et15-b01": "drds.aliyuncs.com",
			"cn-hangzhou-bj-b01": "drds.aliyuncs.com",
			"eu-west-1": "drds.ap-southeast-1.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "drds.aliyuncs.com",
			"eu-west-1-oxs": "drds.ap-southeast-1.aliyuncs.com",
			"cn-zhangbei-na61-b01": "drds.aliyuncs.com",
			"cn-beijing-finance-1": "drds.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "drds.aliyuncs.com",
			"ap-northeast-1": "drds.ap-southeast-1.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "drds.aliyuncs.com",
			"me-east-1": "drds.ap-southeast-1.aliyuncs.com",
			"cn-chengdu": "drds.aliyuncs.com",
			"cn-hangzhou-test-306": "drds.aliyuncs.com",
			"cn-shanghai-et2-b01": "drds.aliyuncs.com",
			"cn-hangzhou-finance": "drds.aliyuncs.com",
			"cn-beijing-nu16-b01": "drds.aliyuncs.com",
			"cn-edge-1": "drds.aliyuncs.com",
			"ap-southeast-2": "drds.ap-southeast-1.aliyuncs.com",
			"ap-southeast-3": "drds.ap-southeast-1.aliyuncs.com",
			"ap-southeast-5": "drds.ap-southeast-1.aliyuncs.com",
			"cn-fujian": "drds.aliyuncs.com",
			"ap-northeast-2-pop": "drds.ap-southeast-1.aliyuncs.com",
			"cn-shenzhen-inner": "drds.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "drds.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
