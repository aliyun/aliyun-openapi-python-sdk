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
			"cn-shanghai-internal-test-1": "tds.aliyuncs.com",
			"cn-shenzhen-su18-b01": "tds.aliyuncs.com",
			"cn-beijing": "tds.aliyuncs.com",
			"cn-shanghai-inner": "tds.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "tds.aliyuncs.com",
			"cn-north-2-gov-1": "tds.aliyuncs.com",
			"cn-yushanfang": "tds.aliyuncs.com",
			"cn-qingdao-nebula": "tds.aliyuncs.com",
			"cn-beijing-finance-pop": "tds.aliyuncs.com",
			"cn-wuhan": "tds.aliyuncs.com",
			"cn-zhangjiakou": "tds.aliyuncs.com",
			"us-west-1": "tds.aliyuncs.com",
			"cn-zhangbei": "tds.aliyuncs.com",
			"rus-west-1-pop": "tds.aliyuncs.com",
			"cn-shanghai-et15-b01": "tds.aliyuncs.com",
			"cn-hangzhou-bj-b01": "tds.aliyuncs.com",
			"cn-zhangbei-na61-b01": "tds.aliyuncs.com",
			"ap-northeast-1": "tds.aliyuncs.com",
			"cn-huhehaote-nebula-1": "tds.aliyuncs.com",
			"cn-shanghai-et2-b01": "tds.aliyuncs.com",
			"ap-southeast-1": "tds.ap-southeast-1.aliyuncs.com",
			"ap-southeast-2": "tds.aliyuncs.com",
			"ap-southeast-3": "tds.ap-southeast-3.aliyuncs.com",
			"ap-southeast-5": "tds.aliyuncs.com",
			"us-east-1": "tds.aliyuncs.com",
			"cn-shenzhen-inner": "tds.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "tds.aliyuncs.com",
			"cn-beijing-gov-1": "tds.aliyuncs.com",
			"cn-wulanchabu": "tds.aliyuncs.com",
			"ap-south-1": "tds.aliyuncs.com",
			"cn-shenzhen-st4-d01": "tds.aliyuncs.com",
			"cn-haidian-cm12-c01": "tds.aliyuncs.com",
			"cn-qingdao": "tds.aliyuncs.com",
			"cn-hongkong-finance-pop": "tds.aliyuncs.com",
			"cn-shanghai": "tds.aliyuncs.com",
			"cn-shanghai-finance-1": "tds.aliyuncs.com",
			"cn-hongkong": "tds.aliyuncs.com",
			"eu-central-1": "tds.aliyuncs.com",
			"cn-shenzhen": "tds.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "tds.aliyuncs.com",
			"eu-west-1": "tds.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "tds.aliyuncs.com",
			"eu-west-1-oxs": "tds.aliyuncs.com",
			"cn-beijing-finance-1": "tds.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "tds.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "tds.aliyuncs.com",
			"cn-shenzhen-finance-1": "tds.aliyuncs.com",
			"me-east-1": "tds.aliyuncs.com",
			"cn-chengdu": "tds.aliyuncs.com",
			"cn-hangzhou-test-306": "tds.aliyuncs.com",
			"cn-hangzhou-finance": "tds.aliyuncs.com",
			"cn-beijing-nu16-b01": "tds.aliyuncs.com",
			"cn-edge-1": "tds.aliyuncs.com",
			"cn-huhehaote": "tds.aliyuncs.com",
			"cn-fujian": "tds.aliyuncs.com",
			"ap-northeast-2-pop": "tds.aliyuncs.com",
			"cn-hangzhou": "tds.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
