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
			"cn-shanghai-internal-test-1": "aas.aliyuncs.com",
			"cn-beijing-gov-1": "aas.aliyuncs.com",
			"cn-shenzhen-su18-b01": "aas.aliyuncs.com",
			"cn-shanghai-inner": "aas.aliyuncs.com",
			"cn-shenzhen-st4-d01": "aas.aliyuncs.com",
			"cn-haidian-cm12-c01": "aas.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "aas.aliyuncs.com",
			"cn-north-2-gov-1": "aas.aliyuncs.com",
			"cn-yushanfang": "aas.aliyuncs.com",
			"cn-hongkong-finance-pop": "aas.aliyuncs.com",
			"cn-qingdao-nebula": "aas.aliyuncs.com",
			"cn-shanghai": "aas-vpc.cn-shanghai.aliyuncs.com",
			"cn-shanghai-finance-1": "aas.aliyuncs.com",
			"cn-beijing-finance-pop": "aas.aliyuncs.com",
			"cn-wuhan": "aas.aliyuncs.com",
			"cn-shenzhen": "aas.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "aas.aliyuncs.com",
			"rus-west-1-pop": "aas.ap-northeast-1.aliyuncs.com",
			"cn-shanghai-et15-b01": "aas.aliyuncs.com",
			"cn-hangzhou-bj-b01": "aas.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "aas.aliyuncs.com",
			"eu-west-1-oxs": "aas.ap-northeast-1.aliyuncs.com",
			"cn-zhangbei-na61-b01": "aas.aliyuncs.com",
			"cn-beijing-finance-1": "aas.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "aas.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "aas.aliyuncs.com",
			"cn-shenzhen-finance-1": "aas.aliyuncs.com",
			"cn-chengdu": "aas.aliyuncs.com",
			"cn-hangzhou-test-306": "aas.aliyuncs.com",
			"cn-shanghai-et2-b01": "aas.aliyuncs.com",
			"cn-hangzhou-finance": "aas.aliyuncs.com",
			"cn-beijing-nu16-b01": "aas.aliyuncs.com",
			"cn-edge-1": "aas.aliyuncs.com",
			"cn-huhehaote": "aas.aliyuncs.com",
			"cn-fujian": "aas.aliyuncs.com",
			"us-east-1": "aas.ap-northeast-1.aliyuncs.com",
			"ap-northeast-2-pop": "aas.ap-northeast-1.aliyuncs.com",
			"cn-shenzhen-inner": "aas.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "aas.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
