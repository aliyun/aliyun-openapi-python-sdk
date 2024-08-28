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
			"cn-shanghai-internal-test-1": "r-kvstore.aliyuncs.com",
			"cn-beijing-gov-1": "r-kvstore.aliyuncs.com",
			"cn-shenzhen-su18-b01": "r-kvstore.aliyuncs.com",
			"cn-beijing": "r-kvstore.aliyuncs.com",
			"cn-wulanchabu": "r-kvstore.aliyuncs.com",
			"cn-shanghai-inner": "r-kvstore.aliyuncs.com",
			"cn-shenzhen-st4-d01": "r-kvstore.aliyuncs.com",
			"cn-haidian-cm12-c01": "r-kvstore.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "r-kvstore.aliyuncs.com",
			"cn-north-2-gov-1": "r-kvstore.aliyuncs.com",
			"cn-yushanfang": "r-kvstore.aliyuncs.com",
			"cn-qingdao": "r-kvstore.aliyuncs.com",
			"cn-hongkong-finance-pop": "r-kvstore.aliyuncs.com",
			"cn-qingdao-nebula": "r-kvstore.aliyuncs.com",
			"cn-shanghai": "r-kvstore.aliyuncs.com",
			"cn-shanghai-finance-1": "r-kvstore.aliyuncs.com",
			"cn-heyuan": "r-kvstore.aliyuncs.com",
			"cn-beijing-finance-pop": "r-kvstore.aliyuncs.com",
			"cn-wuhan": "r-kvstore.aliyuncs.com",
			"cn-zhangbei": "r-kvstore.aliyuncs.com",
			"cn-shenzhen": "r-kvstore.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "r-kvstore.aliyuncs.com",
			"rus-west-1-pop": "r-kvstore.aliyuncs.com",
			"cn-shanghai-et15-b01": "r-kvstore.aliyuncs.com",
			"cn-hangzhou-bj-b01": "r-kvstore.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "r-kvstore.aliyuncs.com",
			"eu-west-1-oxs": "r-kvstore.aliyuncs.com",
			"cn-zhangbei-na61-b01": "r-kvstore.aliyuncs.com",
			"cn-beijing-finance-1": "r-kvstore.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "r-kvstore.aliyuncs.com",
			"cn-shenzhen-finance-1": "r-kvstore.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "r-kvstore.aliyuncs.com",
			"cn-hangzhou-test-306": "r-kvstore.aliyuncs.com",
			"cn-shanghai-et2-b01": "r-kvstore.aliyuncs.com",
			"cn-guangzhou": "r-kvstore.aliyuncs.com",
			"cn-hangzhou-finance": "r-kvstore.aliyuncs.com",
			"cn-beijing-nu16-b01": "r-kvstore.aliyuncs.com",
			"cn-edge-1": "r-kvstore.aliyuncs.com",
			"cn-fujian": "r-kvstore.aliyuncs.com",
			"ap-northeast-2-pop": "r-kvstore.aliyuncs.com",
			"cn-shenzhen-inner": "r-kvstore.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "r-kvstore.aliyuncs.com",
			"cn-hangzhou": "r-kvstore.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
