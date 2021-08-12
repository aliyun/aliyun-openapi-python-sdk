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
			"cn-shanghai-internal-test-1": "iot.aliyuncs.com",
			"cn-beijing-gov-1": "iot.aliyuncs.com",
			"cn-shenzhen-su18-b01": "iot.aliyuncs.com",
			"cn-wulanchabu": "iot.aliyuncs.com",
			"ap-south-1": "iot.aliyuncs.com",
			"cn-shanghai-inner": "iot.aliyuncs.com",
			"cn-shenzhen-st4-d01": "iot.aliyuncs.com",
			"cn-haidian-cm12-c01": "iot.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "iot.aliyuncs.com",
			"cn-yushanfang": "iot.aliyuncs.com",
			"cn-qingdao": "iot.aliyuncs.com",
			"cn-hongkong-finance-pop": "iot.aliyuncs.com",
			"cn-qingdao-nebula": "iot.aliyuncs.com",
			"cn-shanghai-finance-1": "iot.aliyuncs.com",
			"cn-hongkong": "iot.aliyuncs.com",
			"cn-beijing-finance-pop": "iot.aliyuncs.com",
			"cn-wuhan": "iot.aliyuncs.com",
			"cn-zhangjiakou": "iot.aliyuncs.com",
			"cn-zhangbei": "iot.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "iot.aliyuncs.com",
			"rus-west-1-pop": "iot.aliyuncs.com",
			"cn-shanghai-et15-b01": "iot.aliyuncs.com",
			"cn-hangzhou-bj-b01": "iot.aliyuncs.com",
			"eu-west-1": "iot.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "iot.aliyuncs.com",
			"eu-west-1-oxs": "iot.aliyuncs.com",
			"cn-zhangbei-na61-b01": "iot.aliyuncs.com",
			"cn-beijing-finance-1": "iot.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "iot.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "iot.aliyuncs.com",
			"cn-shenzhen-finance-1": "iot.aliyuncs.com",
			"me-east-1": "iot.aliyuncs.com",
			"cn-chengdu": "iot.aliyuncs.com",
			"cn-hangzhou-test-306": "iot.aliyuncs.com",
			"cn-huhehaote-nebula-1": "iot.aliyuncs.com",
			"cn-shanghai-et2-b01": "iot.aliyuncs.com",
			"cn-hangzhou-finance": "iot.aliyuncs.com",
			"cn-beijing-nu16-b01": "iot.aliyuncs.com",
			"cn-edge-1": "iot.aliyuncs.com",
			"ap-southeast-2": "iot.aliyuncs.com",
			"ap-southeast-3": "iot.aliyuncs.com",
			"cn-huhehaote": "iot.aliyuncs.com",
			"ap-southeast-5": "iot.aliyuncs.com",
			"cn-fujian": "iot.aliyuncs.com",
			"ap-northeast-2-pop": "iot.aliyuncs.com",
			"cn-shenzhen-inner": "iot.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "iot.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
