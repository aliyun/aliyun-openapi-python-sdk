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
			"cn-shenzhen": "cusanalytic.aliyuncs.com",
			"cn-beijing": "cusanalytic.aliyuncs.com",
			"ap-south-1": "cusanalytic.aliyuncs.com",
			"eu-west-1": "cusanalytic.aliyuncs.com",
			"ap-northeast-1": "cusanalytic.aliyuncs.com",
			"cn-shenzhen-finance-1": "cusanalytic.aliyuncs.com",
			"me-east-1": "cusanalytic.aliyuncs.com",
			"cn-chengdu": "cusanalytic.aliyuncs.com",
			"cn-north-2-gov-1": "cusanalytic.aliyuncs.com",
			"cn-qingdao": "cusanalytic.aliyuncs.com",
			"cn-shanghai": "cusanalytic.aliyuncs.com",
			"cn-shanghai-finance-1": "cusanalytic.aliyuncs.com",
			"cn-hongkong": "cusanalytic.aliyuncs.com",
			"cn-hangzhou-finance": "cusanalytic.aliyuncs.com",
			"ap-southeast-1": "cusanalytic.aliyuncs.com",
			"ap-southeast-2": "cusanalytic.aliyuncs.com",
			"ap-southeast-3": "cusanalytic.aliyuncs.com",
			"eu-central-1": "cusanalytic.aliyuncs.com",
			"cn-huhehaote": "cusanalytic.aliyuncs.com",
			"ap-southeast-5": "cusanalytic.aliyuncs.com",
			"us-east-1": "cusanalytic.aliyuncs.com",
			"cn-zhangjiakou": "cusanalytic.aliyuncs.com",
			"us-west-1": "cusanalytic.aliyuncs.com",
			"cn-hangzhou": "cusanalytic.aliyuncs.com",
		}
		self.endpoint_regional = "central"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
