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
			"cn-shanghai-internal-test-1": "ft.aliyuncs.com",
			"cn-shenzhen-su18-b01": "ft.aliyuncs.com",
			"cn-beijing": "ft.aliyuncs.com",
			"cn-shanghai-inner": "ft.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "ft.aliyuncs.com",
			"cn-yushanfang": "ft.aliyuncs.com",
			"cn-qingdao-nebula": "ft.aliyuncs.com",
			"cn-beijing-finance-pop": "ft.aliyuncs.com",
			"cn-wuhan": "ft.aliyuncs.com",
			"us-west-1": "ft.aliyuncs.com",
			"cn-zhangbei": "ft.aliyuncs.com",
			"rus-west-1-pop": "ft.aliyuncs.com",
			"cn-shanghai-et15-b01": "ft.aliyuncs.com",
			"cn-hangzhou-bj-b01": "ft.aliyuncs.com",
			"cn-zhangbei-na61-b01": "ft.aliyuncs.com",
			"cn-huhehaote-nebula-1": "ft.aliyuncs.com",
			"cn-shanghai-et2-b01": "ft.aliyuncs.com",
			"ap-southeast-1": "ft.aliyuncs.com",
			"ap-southeast-2": "ft.aliyuncs.com",
			"ap-southeast-3": "ft.aliyuncs.com",
			"ap-southeast-5": "ft.aliyuncs.com",
			"cn-shenzhen-inner": "ft.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "ft.aliyuncs.com",
			"cn-beijing-gov-1": "ft.aliyuncs.com",
			"cn-wulanchabu": "ft.aliyuncs.com",
			"ap-south-1": "ft.aliyuncs.com",
			"cn-shenzhen-st4-d01": "ft.aliyuncs.com",
			"cn-haidian-cm12-c01": "ft.aliyuncs.com",
			"cn-qingdao": "ft.aliyuncs.com",
			"cn-hongkong-finance-pop": "ft.aliyuncs.com",
			"cn-shanghai-finance-1": "ft.aliyuncs.com",
			"eu-central-1": "ft.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "ft.aliyuncs.com",
			"eu-west-1": "ft.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "ft.aliyuncs.com",
			"eu-west-1-oxs": "ft.aliyuncs.com",
			"cn-beijing-finance-1": "ft.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "ft.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "ft.aliyuncs.com",
			"cn-shenzhen-finance-1": "ft.aliyuncs.com",
			"me-east-1": "ft.aliyuncs.com",
			"cn-chengdu": "ft.aliyuncs.com",
			"cn-hangzhou-test-306": "ft.aliyuncs.com",
			"cn-hangzhou-finance": "ft.aliyuncs.com",
			"cn-beijing-nu16-b01": "ft.aliyuncs.com",
			"cn-edge-1": "ft.aliyuncs.com",
			"cn-huhehaote": "ft.aliyuncs.com",
			"cn-fujian": "ft.aliyuncs.com",
			"ap-northeast-2-pop": "ft.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
