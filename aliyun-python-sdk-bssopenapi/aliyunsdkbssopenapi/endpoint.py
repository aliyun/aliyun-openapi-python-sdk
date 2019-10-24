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
			"cn-shanghai-internal-test-1": "business.aliyuncs.com",
			"cn-shenzhen-su18-b01": "business.aliyuncs.com",
			"cn-beijing": "business.aliyuncs.com",
			"cn-shanghai-inner": "business.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "business.aliyuncs.com",
			"cn-north-2-gov-1": "business.aliyuncs.com",
			"cn-yushanfang": "business.aliyuncs.com",
			"cn-qingdao-nebula": "business.aliyuncs.com",
			"cn-beijing-finance-pop": "business.aliyuncs.com",
			"cn-wuhan": "business.aliyuncs.com",
			"cn-zhangjiakou": "business.aliyuncs.com",
			"us-west-1": "business.ap-southeast-1.aliyuncs.com",
			"rus-west-1-pop": "business.ap-southeast-1.aliyuncs.com",
			"cn-shanghai-et15-b01": "business.aliyuncs.com",
			"cn-hangzhou-bj-b01": "business.aliyuncs.com",
			"cn-zhangbei-na61-b01": "business.aliyuncs.com",
			"ap-northeast-1": "business.ap-southeast-1.aliyuncs.com",
			"cn-shanghai-et2-b01": "business.aliyuncs.com",
			"ap-southeast-1": "business.ap-southeast-1.aliyuncs.com",
			"ap-southeast-2": "business.ap-southeast-1.aliyuncs.com",
			"ap-southeast-3": "business.ap-southeast-1.aliyuncs.com",
			"ap-southeast-5": "business.ap-southeast-1.aliyuncs.com",
			"us-east-1": "business.ap-southeast-1.aliyuncs.com",
			"cn-shenzhen-inner": "business.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "business.aliyuncs.com",
			"cn-beijing-gov-1": "business.aliyuncs.com",
			"ap-south-1": "business.ap-southeast-1.aliyuncs.com",
			"cn-shenzhen-st4-d01": "business.aliyuncs.com",
			"cn-haidian-cm12-c01": "business.aliyuncs.com",
			"cn-qingdao": "business.aliyuncs.com",
			"cn-hongkong-finance-pop": "business.aliyuncs.com",
			"cn-shanghai": "business.aliyuncs.com",
			"cn-shanghai-finance-1": "business.aliyuncs.com",
			"cn-hongkong": "business.aliyuncs.com",
			"eu-central-1": "business.ap-southeast-1.aliyuncs.com",
			"cn-shenzhen": "business.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "business.aliyuncs.com",
			"eu-west-1": "business.ap-southeast-1.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "business.aliyuncs.com",
			"eu-west-1-oxs": "business.ap-southeast-1.aliyuncs.com",
			"cn-beijing-finance-1": "business.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "business.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "business.aliyuncs.com",
			"cn-shenzhen-finance-1": "business.aliyuncs.com",
			"me-east-1": "business.ap-southeast-1.aliyuncs.com",
			"cn-chengdu": "business.aliyuncs.com",
			"cn-hangzhou-test-306": "business.aliyuncs.com",
			"cn-hangzhou-finance": "business.aliyuncs.com",
			"cn-beijing-nu16-b01": "business.aliyuncs.com",
			"cn-edge-1": "business.aliyuncs.com",
			"cn-huhehaote": "business.aliyuncs.com",
			"cn-fujian": "business.aliyuncs.com",
			"ap-northeast-2-pop": "business.ap-southeast-1.aliyuncs.com",
			"cn-hangzhou": "business.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
