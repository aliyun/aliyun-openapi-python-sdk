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
			"cn-shenzhen": "apigateway.cn-shenzhen.aliyuncs.com",
			"cn-beijing": "apigateway.cn-beijing.aliyuncs.com",
			"ap-south-1": "apigateway.ap-south-1.aliyuncs.com",
			"eu-west-1": "apigateway.eu-west-1.aliyuncs.com",
			"ap-northeast-1": "apigateway.ap-northeast-1.aliyuncs.com",
			"cn-shenzhen-finance-1": "apigateway.aliyuncs.com",
			"me-east-1": "apigateway.me-east-1.aliyuncs.com",
			"cn-chengdu": "apigateway.cn-chengdu.aliyuncs.com",
			"cn-north-2-gov-1": "apigateway.cn-north-2-gov-1.aliyuncs.com",
			"cn-qingdao": "apigateway.cn-qingdao.aliyuncs.com",
			"cn-shanghai": "apigateway.cn-shanghai.aliyuncs.com",
			"cn-shanghai-finance-1": "apigateway.aliyuncs.com",
			"cn-hongkong": "apigateway.cn-hongkong.aliyuncs.com",
			"cn-hangzhou-finance": "apigateway.aliyuncs.com",
			"ap-southeast-1": "apigateway.ap-southeast-1.aliyuncs.com",
			"ap-southeast-2": "apigateway.ap-southeast-2.aliyuncs.com",
			"ap-southeast-3": "apigateway.ap-southeast-3.aliyuncs.com",
			"eu-central-1": "apigateway.eu-central-1.aliyuncs.com",
			"cn-huhehaote": "apigateway.cn-huhehaote.aliyuncs.com",
			"ap-southeast-5": "apigateway.ap-southeast-5.aliyuncs.com",
			"us-east-1": "apigateway.us-east-1.aliyuncs.com",
			"cn-zhangjiakou": "apigateway.cn-zhangjiakou.aliyuncs.com",
			"us-west-1": "apigateway.us-west-1.aliyuncs.com",
			"cn-hangzhou": "apigateway.cn-hangzhou.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
