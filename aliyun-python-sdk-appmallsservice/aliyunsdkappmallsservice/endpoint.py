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
			"cn-shenzhen": "appms.aliyuncs.com",
			"cn-beijing": "appms.aliyuncs.com",
			"ap-south-1": "appms.aliyuncs.com",
			"eu-west-1": "appms.aliyuncs.com",
			"ap-northeast-1": "appms.aliyuncs.com",
			"me-east-1": "appms.aliyuncs.com",
			"cn-chengdu": "appms.aliyuncs.com",
			"cn-qingdao": "appms.aliyuncs.com",
			"cn-shanghai": "appms.aliyuncs.com",
			"cn-hongkong": "appms.aliyuncs.com",
			"ap-southeast-1": "appms.aliyuncs.com",
			"ap-southeast-2": "appms.aliyuncs.com",
			"ap-southeast-3": "appms.aliyuncs.com",
			"eu-central-1": "appms.aliyuncs.com",
			"cn-huhehaote": "appms.aliyuncs.com",
			"ap-southeast-5": "appms.aliyuncs.com",
			"us-east-1": "appms.aliyuncs.com",
			"cn-zhangjiakou": "appms.aliyuncs.com",
			"us-west-1": "appms.aliyuncs.com",
			"cn-hangzhou": "appms.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
