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
			"cn-shanghai-internal-test-1": "cbn.aliyuncs.com",
			"cn-shenzhen-su18-b01": "cbn.aliyuncs.com",
			"cn-beijing": "cbn.aliyuncs.com",
			"cn-shanghai-inner": "cbn.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "cbn.aliyuncs.com",
			"cn-north-2-gov-1": "cbn.aliyuncs.com",
			"cn-yushanfang": "cbn.aliyuncs.com",
			"cn-qingdao-nebula": "cbn.aliyuncs.com",
			"cn-beijing-finance-pop": "cbn.aliyuncs.com",
			"cn-wuhan": "cbn.aliyuncs.com",
			"cn-zhangjiakou": "cbn.aliyuncs.com",
			"us-west-1": "cbn.aliyuncs.com",
			"rus-west-1-pop": "cbn.aliyuncs.com",
			"cn-shanghai-et15-b01": "cbn.aliyuncs.com",
			"cn-hangzhou-bj-b01": "cbn.aliyuncs.com",
			"cn-zhangbei-na61-b01": "cbn.aliyuncs.com",
			"ap-northeast-1": "cbn.aliyuncs.com",
			"cn-shanghai-et2-b01": "cbn.aliyuncs.com",
			"ap-southeast-1": "cbn.aliyuncs.com",
			"ap-southeast-2": "cbn.aliyuncs.com",
			"ap-southeast-3": "cbn.aliyuncs.com",
			"ap-southeast-5": "cbn.aliyuncs.com",
			"us-east-1": "cbn.aliyuncs.com",
			"cn-shenzhen-inner": "cbn.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "cbn.aliyuncs.com",
			"cn-beijing-gov-1": "cbn.aliyuncs.com",
			"ap-south-1": "cbn.aliyuncs.com",
			"cn-shenzhen-st4-d01": "cbn.aliyuncs.com",
			"cn-haidian-cm12-c01": "cbn.aliyuncs.com",
			"cn-qingdao": "cbn.aliyuncs.com",
			"cn-hongkong-finance-pop": "cbn.aliyuncs.com",
			"cn-shanghai": "cbn.aliyuncs.com",
			"cn-shanghai-finance-1": "cbn.aliyuncs.com",
			"cn-hongkong": "cbn.aliyuncs.com",
			"eu-central-1": "cbn.aliyuncs.com",
			"cn-shenzhen": "cbn.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "cbn.aliyuncs.com",
			"eu-west-1": "cbn.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "cbn.aliyuncs.com",
			"eu-west-1-oxs": "cbn.aliyuncs.com",
			"cn-beijing-finance-1": "cbn.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "cbn.aliyuncs.com",
			"cn-shenzhen-finance-1": "cbn.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "cbn.aliyuncs.com",
			"me-east-1": "cbn.aliyuncs.com",
			"cn-chengdu": "cbn.aliyuncs.com",
			"cn-hangzhou-test-306": "cbn.aliyuncs.com",
			"cn-hangzhou-finance": "cbn.aliyuncs.com",
			"cn-beijing-nu16-b01": "cbn.aliyuncs.com",
			"cn-edge-1": "cbn.aliyuncs.com",
			"cn-huhehaote": "cbn.aliyuncs.com",
			"cn-fujian": "cbn.aliyuncs.com",
			"ap-northeast-2-pop": "cbn.aliyuncs.com",
			"cn-hangzhou": "cbn.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
