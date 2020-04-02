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
			"cn-shanghai-internal-test-1": "cloudesl.aliyuncs.com",
			"cn-shenzhen-su18-b01": "cloudesl.aliyuncs.com",
			"cn-beijing": "cloudesl.aliyuncs.com",
			"cn-shanghai-inner": "cloudesl.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "cloudesl.aliyuncs.com",
			"cn-north-2-gov-1": "cloudesl.aliyuncs.com",
			"cn-yushanfang": "cloudesl.aliyuncs.com",
			"cn-qingdao-nebula": "cloudesl.aliyuncs.com",
			"cn-beijing-finance-pop": "cloudesl.aliyuncs.com",
			"cn-wuhan": "cloudesl.aliyuncs.com",
			"cn-zhangjiakou": "cloudesl.aliyuncs.com",
			"us-west-1": "cloudesl.aliyuncs.com",
			"rus-west-1-pop": "cloudesl.aliyuncs.com",
			"cn-shanghai-et15-b01": "cloudesl.aliyuncs.com",
			"cn-hangzhou-bj-b01": "cloudesl.aliyuncs.com",
			"cn-zhangbei-na61-b01": "cloudesl.aliyuncs.com",
			"ap-northeast-1": "cloudesl.aliyuncs.com",
			"cn-shanghai-et2-b01": "cloudesl.aliyuncs.com",
			"ap-southeast-1": "cloudesl.aliyuncs.com",
			"ap-southeast-2": "cloudesl.aliyuncs.com",
			"ap-southeast-3": "cloudesl.aliyuncs.com",
			"ap-southeast-5": "cloudesl.aliyuncs.com",
			"us-east-1": "cloudesl.aliyuncs.com",
			"cn-shenzhen-inner": "cloudesl.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "cloudesl.aliyuncs.com",
			"cn-beijing-gov-1": "cloudesl.aliyuncs.com",
			"ap-south-1": "cloudesl.aliyuncs.com",
			"cn-shenzhen-st4-d01": "cloudesl.aliyuncs.com",
			"cn-haidian-cm12-c01": "cloudesl.aliyuncs.com",
			"cn-qingdao": "cloudesl.aliyuncs.com",
			"cn-hongkong-finance-pop": "cloudesl.aliyuncs.com",
			"cn-shanghai": "cloudesl.aliyuncs.com",
			"cn-shanghai-finance-1": "cloudesl.aliyuncs.com",
			"cn-hongkong": "cloudesl.aliyuncs.com",
			"eu-central-1": "cloudesl.aliyuncs.com",
			"cn-shenzhen": "cloudesl.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "cloudesl.aliyuncs.com",
			"eu-west-1": "cloudesl.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "cloudesl.aliyuncs.com",
			"eu-west-1-oxs": "cloudesl.aliyuncs.com",
			"cn-beijing-finance-1": "cloudesl.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "cloudesl.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "cloudesl.aliyuncs.com",
			"cn-shenzhen-finance-1": "cloudesl.aliyuncs.com",
			"me-east-1": "cloudesl.aliyuncs.com",
			"cn-chengdu": "cloudesl.aliyuncs.com",
			"cn-hangzhou-test-306": "cloudesl.aliyuncs.com",
			"cn-hangzhou-finance": "cloudesl.aliyuncs.com",
			"cn-beijing-nu16-b01": "cloudesl.aliyuncs.com",
			"cn-edge-1": "cloudesl.aliyuncs.com",
			"cn-huhehaote": "cloudesl.aliyuncs.com",
			"cn-fujian": "cloudesl.aliyuncs.com",
			"ap-northeast-2-pop": "cloudesl.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
