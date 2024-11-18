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
			"cn-shanghai-internal-test-1": "polardb.aliyuncs.com",
			"cn-beijing-gov-1": "polardb.aliyuncs.com",
			"cn-shenzhen-su18-b01": "polardb.aliyuncs.com",
			"cn-beijing": "polardb.aliyuncs.com",
			"cn-wulanchabu": "polardb.aliyuncs.com",
			"cn-shanghai-inner": "polardb.aliyuncs.com",
			"cn-shenzhen-st4-d01": "polardb.aliyuncs.com",
			"cn-haidian-cm12-c01": "polardb.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "polardb.aliyuncs.com",
			"cn-north-2-gov-1": "polardb.aliyuncs.com",
			"cn-yushanfang": "polardb.aliyuncs.com",
			"cn-qingdao": "polardb.aliyuncs.com",
			"cn-hongkong-finance-pop": "polardb.aliyuncs.com",
			"cn-qingdao-nebula": "polardb.aliyuncs.com",
			"cn-shanghai": "polardb.aliyuncs.com",
			"cn-shanghai-finance-1": "polardb.aliyuncs.com",
			"cn-hongkong": "polardb.aliyuncs.com",
			"cn-beijing-finance-pop": "polardb.aliyuncs.com",
			"cn-wuhan": "polardb.aliyuncs.com",
			"cn-zhangbei": "polardb.aliyuncs.com",
			"cn-shenzhen": "polardb.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "polardb.aliyuncs.com",
			"rus-west-1-pop": "polardb.aliyuncs.com",
			"cn-shanghai-et15-b01": "polardb.aliyuncs.com",
			"cn-hangzhou-bj-b01": "polardb.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "polardb.aliyuncs.com",
			"eu-west-1-oxs": "polardb.aliyuncs.com",
			"cn-zhangbei-na61-b01": "polardb.aliyuncs.com",
			"cn-beijing-finance-1": "polardb.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "polardb.aliyuncs.com",
			"cn-shenzhen-finance-1": "polardb.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "polardb.aliyuncs.com",
			"cn-hangzhou-test-306": "polardb.aliyuncs.com",
			"cn-huhehaote-nebula-1": "polardb.aliyuncs.com",
			"cn-shanghai-et2-b01": "polardb.aliyuncs.com",
			"cn-guangzhou": "polardb.aliyuncs.com",
			"cn-hangzhou-finance": "polardb.aliyuncs.com",
			"cn-beijing-nu16-b01": "polardb.aliyuncs.com",
			"cn-edge-1": "polardb.aliyuncs.com",
			"cn-fujian": "polardb.aliyuncs.com",
			"ap-northeast-2-pop": "polardb.aliyuncs.com",
			"cn-shenzhen-inner": "polardb.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "polardb.aliyuncs.com",
			"cn-hangzhou": "polardb.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
