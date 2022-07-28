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
			"cn-shenzhen": "pai-eas.cn-shenzhen.aliyuncs.com",
			"cn-beijing": "pai-eas.cn-beijing.aliyuncs.com",
			"ap-south-1": "pai-eas.ap-south-1.aliyuncs.com",
			"cn-north-2-gov-1": "pai-eas.cn-north-2-gov-1.aliyuncs.com",
			"cn-chengdu": "pai-eas.cn-chengdu.aliyuncs.com",
			"cn-shanghai": "pai-eas.cn-shanghai.aliyuncs.com",
			"cn-shanghai-finance-1": "pai-eas.cn-shanghai-finance-1.aliyuncs.com",
			"cn-hongkong": "pai-eas.cn-hongkong.aliyuncs.com",
			"ap-southeast-1": "pai-eas.ap-southeast-1.aliyuncs.com",
			"eu-central-1": "pai-eas.eu-central-1.aliyuncs.com",
			"ap-southeast-5": "pai-eas.ap-southeast-5.aliyuncs.com",
			"us-east-1": "pai-eas.us-east-1.aliyuncs.com",
			"cn-zhangjiakou": "pai-eas.cn-zhangjiakou.aliyuncs.com",
			"us-west-1": "pai-eas.us-west-1.aliyuncs.com",
			"cn-hangzhou": "pai-eas.cn-hangzhou.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
