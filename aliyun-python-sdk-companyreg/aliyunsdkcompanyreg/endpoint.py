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
			"cn-shanghai-internal-test-1": "companyreg.aliyuncs.com",
			"cn-shenzhen-su18-b01": "companyreg.aliyuncs.com",
			"cn-beijing": "companyreg.aliyuncs.com",
			"cn-shanghai-inner": "companyreg.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "companyreg.aliyuncs.com",
			"cn-north-2-gov-1": "companyreg.aliyuncs.com",
			"cn-yushanfang": "companyreg.aliyuncs.com",
			"cn-qingdao-nebula": "companyreg.aliyuncs.com",
			"cn-beijing-finance-pop": "companyreg.aliyuncs.com",
			"cn-wuhan": "companyreg.aliyuncs.com",
			"cn-zhangjiakou": "companyreg.aliyuncs.com",
			"us-west-1": "companyreg.aliyuncs.com",
			"cn-zhangbei": "companyreg.aliyuncs.com",
			"rus-west-1-pop": "companyreg.aliyuncs.com",
			"cn-shanghai-et15-b01": "companyreg.aliyuncs.com",
			"cn-hangzhou-bj-b01": "companyreg.aliyuncs.com",
			"cn-zhangbei-na61-b01": "companyreg.aliyuncs.com",
			"ap-northeast-1": "companyreg.aliyuncs.com",
			"cn-huhehaote-nebula-1": "companyreg.aliyuncs.com",
			"cn-shanghai-et2-b01": "companyreg.aliyuncs.com",
			"ap-southeast-1": "companyreg.aliyuncs.com",
			"ap-southeast-2": "companyreg.aliyuncs.com",
			"ap-southeast-3": "companyreg.aliyuncs.com",
			"ap-southeast-5": "companyreg.aliyuncs.com",
			"us-east-1": "companyreg.aliyuncs.com",
			"cn-shenzhen-inner": "companyreg.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "companyreg.aliyuncs.com",
			"cn-beijing-gov-1": "companyreg.aliyuncs.com",
			"cn-wulanchabu": "companyreg.aliyuncs.com",
			"ap-south-1": "companyreg.aliyuncs.com",
			"cn-shenzhen-st4-d01": "companyreg.aliyuncs.com",
			"cn-haidian-cm12-c01": "companyreg.aliyuncs.com",
			"cn-qingdao": "companyreg.aliyuncs.com",
			"cn-hongkong-finance-pop": "companyreg.aliyuncs.com",
			"cn-shanghai": "companyreg.aliyuncs.com",
			"cn-shanghai-finance-1": "companyreg.aliyuncs.com",
			"cn-hongkong": "companyreg.aliyuncs.com",
			"eu-central-1": "companyreg.aliyuncs.com",
			"cn-shenzhen": "companyreg.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "companyreg.aliyuncs.com",
			"eu-west-1": "companyreg.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "companyreg.aliyuncs.com",
			"eu-west-1-oxs": "companyreg.aliyuncs.com",
			"cn-beijing-finance-1": "companyreg.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "companyreg.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "companyreg.aliyuncs.com",
			"cn-shenzhen-finance-1": "companyreg.aliyuncs.com",
			"me-east-1": "companyreg.aliyuncs.com",
			"cn-chengdu": "companyreg.aliyuncs.com",
			"cn-hangzhou-test-306": "companyreg.aliyuncs.com",
			"cn-hangzhou-finance": "companyreg.aliyuncs.com",
			"cn-beijing-nu16-b01": "companyreg.aliyuncs.com",
			"cn-edge-1": "companyreg.aliyuncs.com",
			"cn-huhehaote": "companyreg.aliyuncs.com",
			"cn-fujian": "companyreg.aliyuncs.com",
			"ap-northeast-2-pop": "companyreg.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
