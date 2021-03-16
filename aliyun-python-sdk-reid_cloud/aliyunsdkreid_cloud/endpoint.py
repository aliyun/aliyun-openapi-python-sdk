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
			"cn-shanghai-internal-test-1": "reidcloud.aliyuncs.com",
			"cn-shenzhen-su18-b01": "reidcloud.aliyuncs.com",
			"cn-beijing": "reidcloud.aliyuncs.com",
			"cn-shanghai-inner": "reidcloud.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "reidcloud.aliyuncs.com",
			"cn-north-2-gov-1": "reidcloud.aliyuncs.com",
			"cn-yushanfang": "reidcloud.aliyuncs.com",
			"cn-qingdao-nebula": "reidcloud.aliyuncs.com",
			"cn-beijing-finance-pop": "reidcloud.aliyuncs.com",
			"cn-wuhan": "reidcloud.aliyuncs.com",
			"cn-zhangjiakou": "reidcloud.aliyuncs.com",
			"us-west-1": "reidcloud.aliyuncs.com",
			"cn-zhangbei": "reidcloud.aliyuncs.com",
			"rus-west-1-pop": "reidcloud.aliyuncs.com",
			"cn-shanghai-et15-b01": "reidcloud.aliyuncs.com",
			"cn-hangzhou-bj-b01": "reidcloud.aliyuncs.com",
			"cn-zhangbei-na61-b01": "reidcloud.aliyuncs.com",
			"ap-northeast-1": "reidcloud.aliyuncs.com",
			"cn-huhehaote-nebula-1": "reidcloud.aliyuncs.com",
			"cn-shanghai-et2-b01": "reidcloud.aliyuncs.com",
			"ap-southeast-1": "reidcloud.aliyuncs.com",
			"ap-southeast-2": "reidcloud.aliyuncs.com",
			"ap-southeast-3": "reidcloud.aliyuncs.com",
			"ap-southeast-5": "reidcloud.aliyuncs.com",
			"us-east-1": "reidcloud.aliyuncs.com",
			"cn-shenzhen-inner": "reidcloud.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "reidcloud.aliyuncs.com",
			"cn-beijing-gov-1": "reidcloud.aliyuncs.com",
			"cn-wulanchabu": "reidcloud.aliyuncs.com",
			"ap-south-1": "reidcloud.aliyuncs.com",
			"cn-shenzhen-st4-d01": "reidcloud.aliyuncs.com",
			"cn-haidian-cm12-c01": "reidcloud.aliyuncs.com",
			"cn-qingdao": "reidcloud.aliyuncs.com",
			"cn-hongkong-finance-pop": "reidcloud.aliyuncs.com",
			"cn-shanghai": "reidcloud.cn-shanghai.aliyuncs.com",
			"cn-shanghai-finance-1": "reidcloud.aliyuncs.com",
			"cn-hongkong": "reidcloud.aliyuncs.com",
			"eu-central-1": "reidcloud.aliyuncs.com",
			"cn-shenzhen": "reidcloud.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "reidcloud.aliyuncs.com",
			"eu-west-1": "reidcloud.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "reidcloud.aliyuncs.com",
			"eu-west-1-oxs": "reidcloud.aliyuncs.com",
			"cn-beijing-finance-1": "reidcloud.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "reidcloud.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "reidcloud.aliyuncs.com",
			"cn-shenzhen-finance-1": "reidcloud.aliyuncs.com",
			"me-east-1": "reidcloud.aliyuncs.com",
			"cn-chengdu": "reidcloud.aliyuncs.com",
			"cn-hangzhou-test-306": "reidcloud.aliyuncs.com",
			"cn-hangzhou-finance": "reidcloud.aliyuncs.com",
			"cn-beijing-nu16-b01": "reidcloud.aliyuncs.com",
			"cn-edge-1": "reidcloud.aliyuncs.com",
			"cn-huhehaote": "reidcloud.aliyuncs.com",
			"cn-fujian": "reidcloud.aliyuncs.com",
			"ap-northeast-2-pop": "reidcloud.aliyuncs.com",
			"cn-hangzhou": "reidcloud.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
