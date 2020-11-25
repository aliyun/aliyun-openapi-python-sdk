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
			"cn-shanghai-internal-test-1": "hitsdb.aliyuncs.com",
			"cn-beijing-gov-1": "hitsdb.aliyuncs.com",
			"cn-shenzhen-su18-b01": "hitsdb.aliyuncs.com",
			"cn-beijing": "hitsdb.aliyuncs.com",
			"cn-wulanchabu": "hitsdb.aliyuncs.com",
			"cn-shanghai-inner": "hitsdb.aliyuncs.com",
			"cn-shenzhen-st4-d01": "hitsdb.aliyuncs.com",
			"cn-haidian-cm12-c01": "hitsdb.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "hitsdb.aliyuncs.com",
			"cn-yushanfang": "hitsdb.aliyuncs.com",
			"cn-qingdao": "hitsdb.aliyuncs.com",
			"cn-hongkong-finance-pop": "hitsdb.aliyuncs.com",
			"cn-qingdao-nebula": "hitsdb.aliyuncs.com",
			"cn-shanghai": "hitsdb.aliyuncs.com",
			"cn-shanghai-finance-1": "hitsdb.aliyuncs.com",
			"cn-hongkong": "hitsdb.aliyuncs.com",
			"cn-beijing-finance-pop": "hitsdb.aliyuncs.com",
			"cn-wuhan": "hitsdb.aliyuncs.com",
			"us-west-1": "hitsdb.aliyuncs.com",
			"cn-zhangbei": "hitsdb.aliyuncs.com",
			"cn-shenzhen": "hitsdb.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "hitsdb.aliyuncs.com",
			"rus-west-1-pop": "hitsdb.aliyuncs.com",
			"cn-shanghai-et15-b01": "hitsdb.aliyuncs.com",
			"cn-hangzhou-bj-b01": "hitsdb.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "hitsdb.aliyuncs.com",
			"eu-west-1-oxs": "hitsdb.aliyuncs.com",
			"cn-zhangbei-na61-b01": "hitsdb.aliyuncs.com",
			"cn-beijing-finance-1": "hitsdb.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "hitsdb.aliyuncs.com",
			"cn-shenzhen-finance-1": "hitsdb.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "hitsdb.aliyuncs.com",
			"me-east-1": "hitsdb.aliyuncs.com",
			"cn-chengdu": "hitsdb.aliyuncs.com",
			"cn-hangzhou-test-306": "hitsdb.aliyuncs.com",
			"cn-huhehaote-nebula-1": "hitsdb.aliyuncs.com",
			"cn-shanghai-et2-b01": "hitsdb.aliyuncs.com",
			"cn-hangzhou-finance": "hitsdb.aliyuncs.com",
			"ap-southeast-1": "hitsdb.aliyuncs.com",
			"cn-beijing-nu16-b01": "hitsdb.aliyuncs.com",
			"cn-edge-1": "hitsdb.aliyuncs.com",
			"us-east-1": "hitsdb.aliyuncs.com",
			"cn-fujian": "hitsdb.aliyuncs.com",
			"ap-northeast-2-pop": "hitsdb.aliyuncs.com",
			"cn-shenzhen-inner": "hitsdb.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "hitsdb.aliyuncs.com",
			"cn-hangzhou": "hitsdb.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
