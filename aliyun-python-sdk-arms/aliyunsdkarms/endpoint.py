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
			"cn-shanghai-internal-test-1": "arms.aliyuncs.com",
			"cn-beijing-gov-1": "arms.aliyuncs.com",
			"cn-shenzhen-su18-b01": "arms.aliyuncs.com",
			"cn-shanghai-inner": "arms.aliyuncs.com",
			"cn-shenzhen-st4-d01": "arms.aliyuncs.com",
			"cn-haidian-cm12-c01": "arms.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "arms.aliyuncs.com",
			"cn-yushanfang": "arms.aliyuncs.com",
			"cn-hongkong-finance-pop": "arms.aliyuncs.com",
			"cn-qingdao-nebula": "arms.aliyuncs.com",
			"cn-beijing-finance-pop": "arms.aliyuncs.com",
			"cn-wuhan": "arms.aliyuncs.com",
			"cn-zhangbei": "arms.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "arms.aliyuncs.com",
			"rus-west-1-pop": "arms.aliyuncs.com",
			"cn-shanghai-et15-b01": "arms.aliyuncs.com",
			"cn-hangzhou-bj-b01": "arms.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "arms.aliyuncs.com",
			"eu-west-1-oxs": "arms.aliyuncs.com",
			"cn-zhangbei-na61-b01": "arms.aliyuncs.com",
			"cn-beijing-finance-1": "arms.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "arms.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "arms.aliyuncs.com",
			"me-east-1": "arms.aliyuncs.com",
			"cn-hangzhou-test-306": "arms.aliyuncs.com",
			"cn-huhehaote-nebula-1": "arms.aliyuncs.com",
			"cn-shanghai-et2-b01": "arms.aliyuncs.com",
			"cn-beijing-nu16-b01": "arms.aliyuncs.com",
			"cn-edge-1": "arms.aliyuncs.com",
			"cn-fujian": "arms.aliyuncs.com",
			"ap-northeast-2-pop": "arms.aliyuncs.com",
			"cn-shenzhen-inner": "arms.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "arms.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
