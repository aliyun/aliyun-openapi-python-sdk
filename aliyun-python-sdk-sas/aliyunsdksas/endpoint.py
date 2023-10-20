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
			"cn-beijing": "tds.aliyuncs.com",
			"cn-wulanchabu": "tds.aliyuncs.com",
			"ap-south-1": "tds.ap-southeast-1.aliyuncs.com",
			"me-central-1": "tds.ap-southeast-1.aliyuncs.com",
			"cn-qingdao": "tds.aliyuncs.com",
			"cn-shanghai": "tds.aliyuncs.com",
			"cn-shanghai-finance-1": "tds.aliyuncs.com",
			"cn-hongkong": "tds.aliyuncs.com",
			"cn-heyuan": "tds.aliyuncs.com",
			"eu-central-1": "tds.ap-southeast-1.aliyuncs.com",
			"cn-zhangjiakou": "tds.aliyuncs.com",
			"us-west-1": "tds.ap-southeast-1.aliyuncs.com",
			"cn-shenzhen": "tds.aliyuncs.com",
			"cn-nanjing": "tds.aliyuncs.com",
			"eu-west-1": "tds.ap-southeast-1.aliyuncs.com",
			"ap-northeast-2": "tds.ap-southeast-1.aliyuncs.com",
			"cn-beijing-finance-1": "tds.aliyuncs.com",
			"ap-northeast-1": "tds.ap-southeast-1.aliyuncs.com",
			"cn-shenzhen-finance-1": "tds.aliyuncs.com",
			"cn-fuzhou": "tds.aliyuncs.com",
			"me-east-1": "tds.ap-southeast-1.aliyuncs.com",
			"cn-chengdu": "tds.aliyuncs.com",
			"cn-guangzhou": "tds.aliyuncs.com",
			"cn-hangzhou-finance": "tds.aliyuncs.com",
			"ap-southeast-1": "tds.ap-southeast-1.aliyuncs.com",
			"ap-southeast-2": "tds.ap-southeast-1.aliyuncs.com",
			"ap-southeast-3": "tds.ap-southeast-1.aliyuncs.com",
			"cn-huhehaote": "tds.aliyuncs.com",
			"ap-southeast-5": "tds.ap-southeast-1.aliyuncs.com",
			"us-east-1": "tds.ap-southeast-1.aliyuncs.com",
			"ap-southeast-6": "tds.ap-southeast-1.aliyuncs.com",
			"ap-southeast-7": "tds.ap-southeast-1.aliyuncs.com",
			"cn-hangzhou": "tds.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
