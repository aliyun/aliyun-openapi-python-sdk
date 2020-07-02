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
			"cn-shenzhen": "dataworks.cn-shenzhen.aliyuncs.com",
			"cn-beijing": "dataworks.cn-beijing.aliyuncs.com",
			"ap-south-1": "dataworks.ap-south-1.aliyuncs.com",
			"eu-west-1": "dataworks.eu-west-1.aliyuncs.com",
			"ap-northeast-1": "dataworks.ap-northeast-1.aliyuncs.com",
			"cn-shenzhen-finance-1": "dataworks.aliyuncs.com",
			"me-east-1": "dataworks.me-east-1.aliyuncs.com",
			"cn-chengdu": "dataworks.cn-chengdu.aliyuncs.com",
			"cn-north-2-gov-1": "dataworks.aliyuncs.com",
			"cn-qingdao": "dataworks.aliyuncs.com",
			"cn-shanghai": "dataworks.cn-shanghai.aliyuncs.com",
			"cn-shanghai-finance-1": "dataworks.aliyuncs.com",
			"cn-hongkong": "dataworks.cn-hongkong.aliyuncs.com",
			"cn-hangzhou-finance": "dataworks.aliyuncs.com",
			"ap-southeast-1": "dataworks.ap-southeast-1.aliyuncs.com",
			"ap-southeast-2": "dataworks.ap-southeast-2.aliyuncs.com",
			"ap-southeast-3": "dataworks.ap-southeast-3.aliyuncs.com",
			"eu-central-1": "dataworks.eu-central-1.aliyuncs.com",
			"cn-huhehaote": "dataworks.aliyuncs.com",
			"ap-southeast-5": "dataworks.ap-southeast-5.aliyuncs.com",
			"us-east-1": "dataworks.us-east-1.aliyuncs.com",
			"cn-zhangjiakou": "dataworks.aliyuncs.com",
			"us-west-1": "dataworks.us-west-1.aliyuncs.com",
			"cn-hangzhou": "dataworks.cn-hangzhou.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
