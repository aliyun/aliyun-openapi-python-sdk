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
			"cn-shenzhen": "adcp.cn-shenzhen.aliyuncs.com",
			"cn-beijing": "adcp.cn-beijing.aliyuncs.com",
			"cn-wulanchabu": "adcp.cn-wulanchabu.aliyuncs.com",
			"ap-south-1": "adcp.ap-south-1.aliyuncs.com",
			"eu-west-1": "adcp-vpc.eu-west-1.aliyuncs.com",
			"ap-northeast-1": "adcp.ap-northeast-1.aliyuncs.com",
			"me-east-1": "adcp.me-east-1.aliyuncs.com",
			"cn-chengdu": "adcp-vpc.cn-chengdu.aliyuncs.com",
			"cn-qingdao": "adcp.cn-qingdao.aliyuncs.com",
			"cn-shanghai": "adcp.cn-shanghai.aliyuncs.com",
			"cn-shanghai-finance-1": "adcp-vpc.cn-shanghai-finance-1.aliyuncs.com",
			"cn-hongkong": "adcp.cn-hongkong.aliyuncs.com",
			"cn-heyuan": "adcp.cn-heyuan.aliyuncs.com",
			"ap-southeast-1": "adcp.ap-southeast-1.aliyuncs.com",
			"ap-southeast-2": "adcp.ap-southeast-2.aliyuncs.com",
			"ap-southeast-3": "adcp.ap-southeast-3.aliyuncs.com",
			"eu-central-1": "adcp.eu-central-1.aliyuncs.com",
			"cn-huhehaote": "adcp.cn-huhehaote.aliyuncs.com",
			"ap-southeast-5": "adcp.ap-southeast-5.aliyuncs.com",
			"us-east-1": "adcp.us-east-1.aliyuncs.com",
			"cn-zhangjiakou": "adcp.cn-zhangjiakou.aliyuncs.com",
			"us-west-1": "adcp.us-west-1.aliyuncs.com",
			"cn-hangzhou": "adcp.cn-hangzhou.aliyuncs.com",
		}
		self.endpoint_regional = "central"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
