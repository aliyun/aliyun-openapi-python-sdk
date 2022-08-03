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
			"cn-shenzhen": "resourcemanager.cn-shenzhen.aliyuncs.com",
			"cn-beijing": "resourcemanager.cn-beijing.aliyuncs.com",
			"cn-wulanchabu": "resourcemanager.cn-wulanchabu.aliyuncs.com",
			"ap-south-1": "resourcemanager.ap-south-1.aliyuncs.com",
			"eu-west-1": "resourcemanager.eu-west-1.aliyuncs.com",
			"ap-northeast-1": "resourcemanager.ap-northeast-1.aliyuncs.com",
			"cn-shenzhen-finance-1": "resourcemanager.cn-shenzhen-finance-1.aliyuncs.com",
			"me-east-1": "resourcemanager.me-east-1.aliyuncs.com",
			"cn-chengdu": "resourcemanager.cn-chengdu.aliyuncs.com",
			"cn-north-2-gov-1": "resourcemanager.cn-north-2-gov-1.aliyuncs.com",
			"cn-qingdao": "resourcemanager.cn-qingdao.aliyuncs.com",
			"cn-shanghai-finance-1": "resourcemanager.cn-shanghai-finance-1.aliyuncs.com",
			"cn-hangzhou-finance": "resourcemanager.cn-hangzhou-finance.aliyuncs.com",
			"cn-hongkong": "resourcemanager.cn-hongkong.aliyuncs.com",
			"ap-southeast-1": "resourcemanager.ap-southeast-1.aliyuncs.com",
			"ap-southeast-2": "resourcemanager.ap-southeast-2.aliyuncs.com",
			"ap-southeast-3": "resourcemanager.ap-southeast-3.aliyuncs.com",
			"eu-central-1": "resourcemanager.eu-central-1.aliyuncs.com",
			"cn-huhehaote": "resourcemanager.cn-huhehaote.aliyuncs.com",
			"ap-southeast-5": "resourcemanager.ap-southeast-5.aliyuncs.com",
			"us-east-1": "resourcemanager.us-east-1.aliyuncs.com",
			"cn-zhangjiakou": "resourcemanager.cn-zhangjiakou.aliyuncs.com",
			"us-west-1": "resourcemanager.us-west-1.aliyuncs.com",
		}
		self.endpoint_regional = "central"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
