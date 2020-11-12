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
			"cn-shanghai-internal-test-1": "actiontrail.aliyuncs.com",
			"cn-beijing-gov-1": "actiontrail.aliyuncs.com",
			"cn-shenzhen-su18-b01": "actiontrail.aliyuncs.com",
			"cn-shanghai-inner": "actiontrail.aliyuncs.com",
			"cn-shenzhen-st4-d01": "actiontrail.aliyuncs.com",
			"cn-haidian-cm12-c01": "actiontrail.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "actiontrail.aliyuncs.com",
			"cn-yushanfang": "actiontrail.aliyuncs.com",
			"cn-hongkong-finance-pop": "actiontrail.aliyuncs.com",
			"cn-qingdao-nebula": "actiontrail.aliyuncs.com",
			"cn-beijing-finance-pop": "actiontrail.aliyuncs.com",
			"cn-wuhan": "actiontrail.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "actiontrail.aliyuncs.com",
			"rus-west-1-pop": "actiontrail.ap-northeast-1.aliyuncs.com",
			"cn-shanghai-et15-b01": "actiontrail.aliyuncs.com",
			"cn-hangzhou-bj-b01": "actiontrail.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "actiontrail.aliyuncs.com",
			"eu-west-1-oxs": "actiontrail.ap-northeast-1.aliyuncs.com",
			"cn-zhangbei-na61-b01": "actiontrail.aliyuncs.com",
			"cn-beijing-finance-1": "actiontrail.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "actiontrail.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "actiontrail.aliyuncs.com",
			"cn-shenzhen-finance-1": "actiontrail.aliyuncs.com",
			"cn-hangzhou-test-306": "actiontrail.aliyuncs.com",
			"cn-shanghai-et2-b01": "actiontrail.aliyuncs.com",
			"cn-hangzhou-finance": "actiontrail.aliyuncs.com",
			"cn-beijing-nu16-b01": "actiontrail.aliyuncs.com",
			"cn-edge-1": "actiontrail.aliyuncs.com",
			"cn-fujian": "actiontrail.aliyuncs.com",
			"ap-northeast-2-pop": "actiontrail.ap-northeast-1.aliyuncs.com",
			"cn-shenzhen-inner": "actiontrail.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "actiontrail.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
