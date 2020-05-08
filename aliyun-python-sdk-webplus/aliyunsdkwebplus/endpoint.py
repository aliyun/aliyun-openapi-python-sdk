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
			"cn-shenzhen": "webplus.cn-hangzhou.aliyuncs.com",
			"cn-beijing": "webplus.cn-hangzhou.aliyuncs.com",
			"ap-south-1": "webplus.aliyuncs.com",
			"eu-west-1": "webplus.aliyuncs.com",
			"ap-northeast-1": "webplus.aliyuncs.com",
			"me-east-1": "webplus.aliyuncs.com",
			"cn-chengdu": "webplus.aliyuncs.com",
			"cn-qingdao": "webplus.aliyuncs.com",
			"cn-shanghai": "webplus.cn-hangzhou.aliyuncs.com",
			"cn-hongkong": "webplus.aliyuncs.com",
			"ap-southeast-1": "webplus.aliyuncs.com",
			"ap-southeast-2": "webplus.aliyuncs.com",
			"ap-southeast-3": "webplus.aliyuncs.com",
			"eu-central-1": "webplus.aliyuncs.com",
			"cn-huhehaote": "webplus.aliyuncs.com",
			"ap-southeast-5": "webplus.aliyuncs.com",
			"us-east-1": "webplus.aliyuncs.com",
			"cn-zhangjiakou": "webplus.cn-hangzhou.aliyuncs.com",
			"us-west-1": "webplus.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
