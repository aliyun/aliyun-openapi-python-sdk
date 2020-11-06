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
			"cn-shanghai-internal-test-1": "gdb-api.aliyuncs.com",
			"cn-shenzhen-su18-b01": "gdb-api.aliyuncs.com",
			"cn-beijing": "gdb-api.aliyuncs.com",
			"cn-shanghai-inner": "gdb-api.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "gdb-api.aliyuncs.com",
			"cn-north-2-gov-1": "gdb-api.aliyuncs.com",
			"cn-yushanfang": "gdb-api.aliyuncs.com",
			"cn-qingdao-nebula": "gdb-api.aliyuncs.com",
			"cn-beijing-finance-pop": "gdb-api.aliyuncs.com",
			"cn-wuhan": "gdb-api.aliyuncs.com",
			"cn-zhangjiakou": "gdb-api.cn-zhangjiakou.aliyuncs.com",
			"us-west-1": "gdb-api.aliyuncs.com",
			"rus-west-1-pop": "gdb-api.aliyuncs.com",
			"cn-shanghai-et15-b01": "gdb-api.aliyuncs.com",
			"cn-hangzhou-bj-b01": "gdb-api.aliyuncs.com",
			"cn-zhangbei-na61-b01": "gdb-api.aliyuncs.com",
			"ap-northeast-1": "gdb-api.aliyuncs.com",
			"cn-huhehaote-nebula-1": "gdb-api.aliyuncs.com",
			"cn-shanghai-et2-b01": "gdb-api.aliyuncs.com",
			"ap-southeast-1": "gdb-api.ap-southeast-1.aliyuncs.com",
			"ap-southeast-2": "gdb-api.aliyuncs.com",
			"ap-southeast-3": "gdb-api.aliyuncs.com",
			"ap-southeast-5": "gdb-api.ap-southeast-5.aliyuncs.com",
			"us-east-1": "gdb-api.aliyuncs.com",
			"cn-shenzhen-inner": "gdb-api.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "gdb-api.aliyuncs.com",
			"cn-beijing-gov-1": "gdb-api.aliyuncs.com",
			"cn-wulanchabu": "gdb-api.aliyuncs.com",
			"ap-south-1": "gdb-api.ap-south-1.aliyuncs.com",
			"cn-shenzhen-st4-d01": "gdb-api.aliyuncs.com",
			"cn-haidian-cm12-c01": "gdb-api.aliyuncs.com",
			"cn-qingdao": "gdb-api.aliyuncs.com",
			"cn-hongkong-finance-pop": "gdb-api.aliyuncs.com",
			"cn-shanghai": "gdb-api.aliyuncs.com",
			"cn-shanghai-finance-1": "gdb-api.aliyuncs.com",
			"cn-hongkong": "gdb-api.aliyuncs.com",
			"eu-central-1": "gdb-api.aliyuncs.com",
			"cn-shenzhen": "gdb-api.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "gdb-api.aliyuncs.com",
			"eu-west-1": "gdb-api.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "gdb-api.aliyuncs.com",
			"eu-west-1-oxs": "gdb-api.aliyuncs.com",
			"cn-beijing-finance-1": "gdb-api.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "gdb-api.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "gdb-api.aliyuncs.com",
			"cn-shenzhen-finance-1": "gdb-api.aliyuncs.com",
			"me-east-1": "gdb-api.aliyuncs.com",
			"cn-chengdu": "gdb-api.aliyuncs.com",
			"cn-hangzhou-test-306": "gdb-api.aliyuncs.com",
			"cn-hangzhou-finance": "gdb-api.aliyuncs.com",
			"cn-beijing-nu16-b01": "gdb-api.aliyuncs.com",
			"cn-edge-1": "gdb-api.aliyuncs.com",
			"cn-huhehaote": "gdb-api.aliyuncs.com",
			"cn-fujian": "gdb-api.aliyuncs.com",
			"ap-northeast-2-pop": "gdb-api.aliyuncs.com",
			"cn-hangzhou": "gdb-api.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
