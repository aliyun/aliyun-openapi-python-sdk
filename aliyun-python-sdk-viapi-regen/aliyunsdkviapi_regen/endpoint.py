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
			"cn-shanghai-internal-test-1": "viapi-regen-daily.aliyuncs.com",
			"cn-shenzhen-su18-b01": "viapi-regen-daily.aliyuncs.com",
			"cn-beijing": "viapi-regen-daily.aliyuncs.com",
			"cn-shanghai-inner": "viapi-regen-daily.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "viapi-regen-daily.aliyuncs.com",
			"cn-north-2-gov-1": "viapi-regen-daily.aliyuncs.com",
			"cn-yushanfang": "viapi-regen-daily.aliyuncs.com",
			"cn-qingdao-nebula": "viapi-regen-daily.aliyuncs.com",
			"cn-beijing-finance-pop": "viapi-regen-daily.aliyuncs.com",
			"cn-wuhan": "viapi-regen-daily.aliyuncs.com",
			"cn-zhangjiakou": "viapi-regen-daily.aliyuncs.com",
			"us-west-1": "viapi-regen-daily.aliyuncs.com",
			"cn-zhangbei": "viapi-regen-daily.aliyuncs.com",
			"rus-west-1-pop": "viapi-regen-daily.aliyuncs.com",
			"cn-shanghai-et15-b01": "viapi-regen-daily.aliyuncs.com",
			"cn-hangzhou-bj-b01": "viapi-regen-daily.aliyuncs.com",
			"cn-zhangbei-na61-b01": "viapi-regen-daily.aliyuncs.com",
			"ap-northeast-1": "viapi-regen-daily.aliyuncs.com",
			"cn-huhehaote-nebula-1": "viapi-regen-daily.aliyuncs.com",
			"cn-shanghai-et2-b01": "viapi-regen-daily.aliyuncs.com",
			"ap-southeast-1": "viapi-regen-daily.aliyuncs.com",
			"ap-southeast-2": "viapi-regen-daily.aliyuncs.com",
			"ap-southeast-3": "viapi-regen-daily.aliyuncs.com",
			"ap-southeast-5": "viapi-regen-daily.aliyuncs.com",
			"us-east-1": "viapi-regen-daily.aliyuncs.com",
			"cn-shenzhen-inner": "viapi-regen-daily.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "viapi-regen-daily.aliyuncs.com",
			"cn-beijing-gov-1": "viapi-regen-daily.aliyuncs.com",
			"cn-wulanchabu": "viapi-regen-daily.aliyuncs.com",
			"ap-south-1": "viapi-regen-daily.aliyuncs.com",
			"cn-shenzhen-st4-d01": "viapi-regen-daily.aliyuncs.com",
			"cn-haidian-cm12-c01": "viapi-regen-daily.aliyuncs.com",
			"cn-qingdao": "viapi-regen-daily.aliyuncs.com",
			"cn-hongkong-finance-pop": "viapi-regen-daily.aliyuncs.com",
			"cn-shanghai-finance-1": "viapi-regen-daily.aliyuncs.com",
			"cn-hongkong": "viapi-regen-daily.aliyuncs.com",
			"eu-central-1": "viapi-regen-daily.aliyuncs.com",
			"cn-shenzhen": "viapi-regen-daily.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "viapi-regen-daily.aliyuncs.com",
			"eu-west-1": "viapi-regen-daily.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "viapi-regen-daily.aliyuncs.com",
			"eu-west-1-oxs": "viapi-regen-daily.aliyuncs.com",
			"cn-beijing-finance-1": "viapi-regen-daily.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "viapi-regen-daily.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "viapi-regen-daily.aliyuncs.com",
			"cn-shenzhen-finance-1": "viapi-regen-daily.aliyuncs.com",
			"me-east-1": "viapi-regen-daily.aliyuncs.com",
			"cn-chengdu": "viapi-regen-daily.aliyuncs.com",
			"cn-hangzhou-test-306": "viapi-regen-daily.aliyuncs.com",
			"cn-hangzhou-finance": "viapi-regen-daily.aliyuncs.com",
			"cn-beijing-nu16-b01": "viapi-regen-daily.aliyuncs.com",
			"cn-edge-1": "viapi-regen-daily.aliyuncs.com",
			"cn-huhehaote": "viapi-regen-daily.aliyuncs.com",
			"cn-fujian": "viapi-regen-daily.aliyuncs.com",
			"ap-northeast-2-pop": "viapi-regen-daily.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
