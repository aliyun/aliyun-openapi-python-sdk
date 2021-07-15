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
			"cn-shenzhen": "alb.cn-shenzhen.aliyuncs.com",
			"cn-beijing": "alb.cn-beijing.aliyuncs.com",
			"cn-wulanchabu": "alb.cn-wulanchabu.aliyuncs.com",
			"ap-south-1": "alb.ap-south-1.aliyuncs.com",
			"ap-northeast-1": "alb.ap-northeast-1.aliyuncs.com",
			"cn-chengdu": "alb.cn-chengdu.aliyuncs.com",
			"cn-shanghai": "alb.cn-shanghai.aliyuncs.com",
			"cn-hongkong": "alb.cn-hongkong.aliyuncs.com",
			"ap-southeast-1": "alb.ap-southeast-1.aliyuncs.com",
			"ap-southeast-2": "alb.ap-southeast-2.aliyuncs.com",
			"eu-central-1": "alb.eu-central-1.aliyuncs.com",
			"ap-southeast-5": "alb.ap-southeast-5.aliyuncs.com",
			"us-east-1": "alb.us-east-1.aliyuncs.com",
			"cn-zhangjiakou": "alb.cn-zhangjiakou.aliyuncs.com",
			"cn-hangzhou": "alb.cn-hangzhou.aliyuncs.com",
		}
		self.endpoint_regional = "central"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
