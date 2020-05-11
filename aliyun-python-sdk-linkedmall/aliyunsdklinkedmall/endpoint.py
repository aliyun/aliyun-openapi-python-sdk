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
			"cn-shanghai-internal-test-1": "linkedmall.aliyuncs.com",
			"cn-shenzhen-su18-b01": "linkedmall.aliyuncs.com",
			"cn-beijing": "linkedmall.aliyuncs.com",
			"cn-shanghai-inner": "linkedmall.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "linkedmall.aliyuncs.com",
			"cn-north-2-gov-1": "linkedmall.aliyuncs.com",
			"cn-yushanfang": "linkedmall.aliyuncs.com",
			"cn-qingdao-nebula": "linkedmall.aliyuncs.com",
			"cn-beijing-finance-pop": "linkedmall.aliyuncs.com",
			"cn-wuhan": "linkedmall.aliyuncs.com",
			"cn-zhangjiakou": "linkedmall.aliyuncs.com",
			"us-west-1": "linkedmall.aliyuncs.com",
			"rus-west-1-pop": "linkedmall.aliyuncs.com",
			"cn-shanghai-et15-b01": "linkedmall.aliyuncs.com",
			"cn-hangzhou-bj-b01": "linkedmall.aliyuncs.com",
			"cn-zhangbei-na61-b01": "linkedmall.aliyuncs.com",
			"ap-northeast-1": "linkedmall.aliyuncs.com",
			"cn-shanghai-et2-b01": "linkedmall.aliyuncs.com",
			"ap-southeast-1": "linkedmall.aliyuncs.com",
			"ap-southeast-2": "linkedmall.aliyuncs.com",
			"ap-southeast-3": "linkedmall.aliyuncs.com",
			"ap-southeast-5": "linkedmall.aliyuncs.com",
			"us-east-1": "linkedmall.aliyuncs.com",
			"cn-shenzhen-inner": "linkedmall.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "linkedmall.aliyuncs.com",
			"cn-beijing-gov-1": "linkedmall.aliyuncs.com",
			"ap-south-1": "linkedmall.aliyuncs.com",
			"cn-shenzhen-st4-d01": "linkedmall.aliyuncs.com",
			"cn-haidian-cm12-c01": "linkedmall.aliyuncs.com",
			"cn-qingdao": "linkedmall.aliyuncs.com",
			"cn-hongkong-finance-pop": "linkedmall.aliyuncs.com",
			"cn-shanghai": "linkedmall.aliyuncs.com",
			"cn-shanghai-finance-1": "linkedmall.aliyuncs.com",
			"cn-hongkong": "linkedmall.aliyuncs.com",
			"eu-central-1": "linkedmall.aliyuncs.com",
			"cn-shenzhen": "linkedmall.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "linkedmall.aliyuncs.com",
			"eu-west-1": "linkedmall.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "linkedmall.aliyuncs.com",
			"eu-west-1-oxs": "linkedmall.aliyuncs.com",
			"cn-beijing-finance-1": "linkedmall.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "linkedmall.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "linkedmall.aliyuncs.com",
			"cn-shenzhen-finance-1": "linkedmall.aliyuncs.com",
			"me-east-1": "linkedmall.aliyuncs.com",
			"cn-chengdu": "linkedmall.aliyuncs.com",
			"cn-hangzhou-test-306": "linkedmall.aliyuncs.com",
			"cn-hangzhou-finance": "linkedmall.aliyuncs.com",
			"cn-beijing-nu16-b01": "linkedmall.aliyuncs.com",
			"cn-edge-1": "linkedmall.aliyuncs.com",
			"cn-huhehaote": "linkedmall.aliyuncs.com",
			"cn-fujian": "linkedmall.aliyuncs.com",
			"ap-northeast-2-pop": "linkedmall.aliyuncs.com",
			"cn-hangzhou": "linkedmall.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
