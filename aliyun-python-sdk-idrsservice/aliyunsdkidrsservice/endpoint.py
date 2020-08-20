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
			"cn-shanghai-internal-test-1": "idrsservice.aliyuncs.com",
			"cn-shenzhen-su18-b01": "idrsservice.aliyuncs.com",
			"cn-beijing": "idrsservice.aliyuncs.com",
			"cn-shanghai-inner": "idrsservice.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "idrsservice.aliyuncs.com",
			"cn-north-2-gov-1": "idrsservice.aliyuncs.com",
			"cn-yushanfang": "idrsservice.aliyuncs.com",
			"cn-qingdao-nebula": "idrsservice.aliyuncs.com",
			"cn-beijing-finance-pop": "idrsservice.aliyuncs.com",
			"cn-wuhan": "idrsservice.aliyuncs.com",
			"cn-zhangjiakou": "idrsservice.aliyuncs.com",
			"us-west-1": "idrsservice.aliyuncs.com",
			"rus-west-1-pop": "idrsservice.aliyuncs.com",
			"cn-shanghai-et15-b01": "idrsservice.aliyuncs.com",
			"cn-hangzhou-bj-b01": "idrsservice.aliyuncs.com",
			"cn-zhangbei-na61-b01": "idrsservice.aliyuncs.com",
			"ap-northeast-1": "idrsservice.aliyuncs.com",
			"cn-huhehaote-nebula-1": "idrsservice.aliyuncs.com",
			"cn-shanghai-et2-b01": "idrsservice.aliyuncs.com",
			"ap-southeast-1": "idrsservice.aliyuncs.com",
			"ap-southeast-2": "idrsservice.aliyuncs.com",
			"ap-southeast-3": "idrsservice.aliyuncs.com",
			"ap-southeast-5": "idrsservice.aliyuncs.com",
			"us-east-1": "idrsservice.aliyuncs.com",
			"cn-shenzhen-inner": "idrsservice.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "idrsservice.aliyuncs.com",
			"cn-beijing-gov-1": "idrsservice.aliyuncs.com",
			"cn-wulanchabu": "idrsservice.aliyuncs.com",
			"ap-south-1": "idrsservice.aliyuncs.com",
			"cn-shenzhen-st4-d01": "idrsservice.aliyuncs.com",
			"cn-haidian-cm12-c01": "idrsservice.aliyuncs.com",
			"cn-qingdao": "idrsservice.aliyuncs.com",
			"cn-hongkong-finance-pop": "idrsservice.aliyuncs.com",
			"cn-shanghai": "idrsservice.aliyuncs.com",
			"cn-hongkong": "idrsservice.aliyuncs.com",
			"eu-central-1": "idrsservice.aliyuncs.com",
			"cn-shenzhen": "idrsservice.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "idrsservice.aliyuncs.com",
			"eu-west-1": "idrsservice.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "idrsservice.aliyuncs.com",
			"eu-west-1-oxs": "idrsservice.aliyuncs.com",
			"cn-beijing-finance-1": "idrsservice.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "idrsservice.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "idrsservice.aliyuncs.com",
			"cn-shenzhen-finance-1": "idrsservice.aliyuncs.com",
			"me-east-1": "idrsservice.aliyuncs.com",
			"cn-chengdu": "idrsservice.aliyuncs.com",
			"cn-hangzhou-test-306": "idrsservice.aliyuncs.com",
			"cn-hangzhou-finance": "idrsservice.aliyuncs.com",
			"cn-beijing-nu16-b01": "idrsservice.aliyuncs.com",
			"cn-edge-1": "idrsservice.aliyuncs.com",
			"cn-huhehaote": "idrsservice.aliyuncs.com",
			"cn-fujian": "idrsservice.aliyuncs.com",
			"ap-northeast-2-pop": "idrsservice.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
