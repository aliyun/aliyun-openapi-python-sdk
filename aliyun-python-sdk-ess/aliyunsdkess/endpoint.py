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
			"cn-shanghai-internal-test-1": "ess.aliyuncs.com",
			"cn-beijing-gov-1": "ess.aliyuncs.com",
			"cn-shenzhen-su18-b01": "ess.aliyuncs.com",
			"cn-beijing": "ess.aliyuncs.com",
			"cn-shanghai-inner": "ess.aliyuncs.com",
			"cn-shenzhen-st4-d01": "ess.aliyuncs.com",
			"cn-haidian-cm12-c01": "ess.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "ess.aliyuncs.com",
			"cn-north-2-gov-1": "ess.aliyuncs.com",
			"cn-yushanfang": "ess.aliyuncs.com",
			"cn-qingdao": "ess.aliyuncs.com",
			"cn-hongkong-finance-pop": "ess.aliyuncs.com",
			"cn-qingdao-nebula": "ess.aliyuncs.com",
			"cn-shanghai": "ess.aliyuncs.com",
			"cn-shanghai-finance-1": "ess.aliyuncs.com",
			"cn-hongkong": "ess.aliyuncs.com",
			"cn-beijing-finance-pop": "ess.aliyuncs.com",
			"cn-wuhan": "ess.aliyuncs.com",
			"us-west-1": "ess.aliyuncs.com",
			"cn-shenzhen": "ess.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "ess.aliyuncs.com",
			"rus-west-1-pop": "ess.ap-northeast-1.aliyuncs.com",
			"cn-shanghai-et15-b01": "ess.aliyuncs.com",
			"cn-hangzhou-bj-b01": "ess.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "ess.aliyuncs.com",
			"eu-west-1-oxs": "ess.ap-northeast-1.aliyuncs.com",
			"cn-zhangbei-na61-b01": "ess.aliyuncs.com",
			"cn-beijing-finance-1": "ess.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "ess.aliyuncs.com",
			"cn-shenzhen-finance-1": "ess.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "ess.aliyuncs.com",
			"cn-hangzhou-test-306": "ess.aliyuncs.com",
			"cn-shanghai-et2-b01": "ess.aliyuncs.com",
			"cn-hangzhou-finance": "ess.aliyuncs.com",
			"ap-southeast-1": "ess.aliyuncs.com",
			"cn-beijing-nu16-b01": "ess.aliyuncs.com",
			"cn-edge-1": "ess.aliyuncs.com",
			"us-east-1": "ess.aliyuncs.com",
			"cn-fujian": "ess.aliyuncs.com",
			"ap-northeast-2-pop": "ess.ap-northeast-1.aliyuncs.com",
			"cn-shenzhen-inner": "ess.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "ess.aliyuncs.com",
			"cn-hangzhou": "ess.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
