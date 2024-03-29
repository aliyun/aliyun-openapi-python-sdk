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
			"cn-shanghai-internal-test-1": "ice.aliyuncs.com",
			"cn-shenzhen-su18-b01": "ice.aliyuncs.com",
			"cn-beijing": "ice.aliyuncs.com",
			"cn-shanghai-inner": "ice.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "ice.aliyuncs.com",
			"cn-north-2-gov-1": "ice.aliyuncs.com",
			"cn-yushanfang": "ice.aliyuncs.com",
			"cn-qingdao-nebula": "ice.aliyuncs.com",
			"cn-beijing-finance-pop": "ice.aliyuncs.com",
			"cn-wuhan": "ice.aliyuncs.com",
			"cn-zhangjiakou": "ice.aliyuncs.com",
			"us-west-1": "ice.aliyuncs.com",
			"cn-zhangbei": "ice.aliyuncs.com",
			"rus-west-1-pop": "ice.aliyuncs.com",
			"cn-shanghai-et15-b01": "ice.aliyuncs.com",
			"cn-hangzhou-bj-b01": "ice.aliyuncs.com",
			"cn-zhangbei-na61-b01": "ice.aliyuncs.com",
			"ap-northeast-1": "ice.aliyuncs.com",
			"cn-huhehaote-nebula-1": "ice.aliyuncs.com",
			"cn-shanghai-et2-b01": "ice.aliyuncs.com",
			"ap-southeast-1": "ice.aliyuncs.com",
			"ap-southeast-2": "ice.aliyuncs.com",
			"ap-southeast-3": "ice.aliyuncs.com",
			"ap-southeast-5": "ice.aliyuncs.com",
			"us-east-1": "ice.aliyuncs.com",
			"cn-shenzhen-inner": "ice.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "ice.aliyuncs.com",
			"cn-beijing-gov-1": "ice.aliyuncs.com",
			"cn-wulanchabu": "ice.aliyuncs.com",
			"ap-south-1": "ice.aliyuncs.com",
			"cn-shenzhen-st4-d01": "ice.aliyuncs.com",
			"cn-haidian-cm12-c01": "ice.aliyuncs.com",
			"cn-qingdao": "ice.aliyuncs.com",
			"cn-hongkong-finance-pop": "ice.aliyuncs.com",
			"cn-shanghai-finance-1": "ice.aliyuncs.com",
			"cn-hongkong": "ice.aliyuncs.com",
			"eu-central-1": "ice.aliyuncs.com",
			"cn-shenzhen": "ice.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "ice.aliyuncs.com",
			"eu-west-1": "ice.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "ice.aliyuncs.com",
			"eu-west-1-oxs": "ice.aliyuncs.com",
			"cn-beijing-finance-1": "ice.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "ice.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "ice.aliyuncs.com",
			"cn-shenzhen-finance-1": "ice.aliyuncs.com",
			"me-east-1": "ice.aliyuncs.com",
			"cn-chengdu": "ice.aliyuncs.com",
			"cn-hangzhou-test-306": "ice.aliyuncs.com",
			"cn-hangzhou-finance": "ice.aliyuncs.com",
			"cn-beijing-nu16-b01": "ice.aliyuncs.com",
			"cn-edge-1": "ice.aliyuncs.com",
			"cn-huhehaote": "ice.aliyuncs.com",
			"cn-fujian": "ice.aliyuncs.com",
			"ap-northeast-2-pop": "ice.aliyuncs.com",
			"cn-hangzhou": "ice.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
