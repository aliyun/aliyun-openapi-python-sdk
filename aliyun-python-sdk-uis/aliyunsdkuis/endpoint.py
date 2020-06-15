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
			"cn-shanghai-internal-test-1": "uis.aliyuncs.com",
			"cn-shenzhen-su18-b01": "uis.aliyuncs.com",
			"cn-beijing": "uis.aliyuncs.com",
			"cn-shanghai-inner": "uis.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "uis.aliyuncs.com",
			"cn-north-2-gov-1": "uis.cn-hangzhou.aliyuncs.com",
			"cn-yushanfang": "uis.aliyuncs.com",
			"cn-qingdao-nebula": "uis.aliyuncs.com",
			"cn-beijing-finance-pop": "uis.aliyuncs.com",
			"cn-wuhan": "uis.aliyuncs.com",
			"cn-zhangjiakou": "uis.aliyuncs.com",
			"us-west-1": "uis.aliyuncs.com",
			"rus-west-1-pop": "uis.aliyuncs.com",
			"cn-shanghai-et15-b01": "uis.aliyuncs.com",
			"cn-hangzhou-bj-b01": "uis.aliyuncs.com",
			"cn-zhangbei-na61-b01": "uis.aliyuncs.com",
			"ap-northeast-1": "uis.aliyuncs.com",
			"cn-shanghai-et2-b01": "uis.aliyuncs.com",
			"ap-southeast-1": "uis.aliyuncs.com",
			"ap-southeast-2": "uis.aliyuncs.com",
			"ap-southeast-3": "uis.aliyuncs.com",
			"ap-southeast-5": "uis.aliyuncs.com",
			"us-east-1": "uis.aliyuncs.com",
			"cn-shenzhen-inner": "uis.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "uis.aliyuncs.com",
			"cn-beijing-gov-1": "uis.aliyuncs.com",
			"ap-south-1": "uis.aliyuncs.com",
			"cn-shenzhen-st4-d01": "uis.aliyuncs.com",
			"cn-haidian-cm12-c01": "uis.aliyuncs.com",
			"cn-qingdao": "uis.aliyuncs.com",
			"cn-hongkong-finance-pop": "uis.aliyuncs.com",
			"cn-shanghai": "uis.aliyuncs.com",
			"cn-shanghai-finance-1": "uis.aliyuncs.com",
			"cn-hongkong": "uis.aliyuncs.com",
			"eu-central-1": "uis.aliyuncs.com",
			"cn-shenzhen": "uis.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "uis.aliyuncs.com",
			"eu-west-1": "uis.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "uis.aliyuncs.com",
			"eu-west-1-oxs": "uis.aliyuncs.com",
			"cn-beijing-finance-1": "uis.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "uis.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "uis.aliyuncs.com",
			"cn-shenzhen-finance-1": "uis.aliyuncs.com",
			"me-east-1": "uis.aliyuncs.com",
			"cn-chengdu": "uis.aliyuncs.com",
			"cn-hangzhou-test-306": "uis.aliyuncs.com",
			"cn-hangzhou-finance": "uis.aliyuncs.com",
			"cn-beijing-nu16-b01": "uis.aliyuncs.com",
			"cn-edge-1": "uis.aliyuncs.com",
			"cn-huhehaote": "uis.aliyuncs.com",
			"cn-fujian": "uis.aliyuncs.com",
			"ap-northeast-2-pop": "uis.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
