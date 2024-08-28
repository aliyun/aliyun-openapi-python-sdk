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
			"cn-shanghai-internal-test-1": "mongodb.aliyuncs.com",
			"cn-shenzhen-su18-b01": "mongodb.aliyuncs.com",
			"cn-beijing": "mongodb.aliyuncs.com",
			"cn-shanghai-inner": "mongodb.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "mongodb.aliyuncs.com",
			"cn-north-2-gov-1": "mongodb.aliyuncs.com",
			"cn-yushanfang": "mongodb.aliyuncs.com",
			"cn-qingdao-nebula": "mongodb.aliyuncs.com",
			"cn-heyuan": "mongodb.aliyuncs.com",
			"cn-beijing-finance-pop": "mongodb.aliyuncs.com",
			"cn-wuhan": "mongodb.aliyuncs.com",
			"cn-zhangjiakou": "mongodb.cn-zhangjiakou.aliyuncs.com",
			"us-west-1": "mongodb.us-west-1.aliyuncs.com",
			"cn-zhangbei": "mongodb.aliyuncs.com",
			"rus-west-1-pop": "mongodb.aliyuncs.com",
			"cn-shanghai-et15-b01": "mongodb.aliyuncs.com",
			"cn-hangzhou-bj-b01": "mongodb.aliyuncs.com",
			"cn-zhangbei-na61-b01": "mongodb.aliyuncs.com",
			"ap-northeast-1": "mongodb.ap-northeast-1.aliyuncs.com",
			"cn-huhehaote-nebula-1": "mongodb.aliyuncs.com",
			"cn-shanghai-et2-b01": "mongodb.aliyuncs.com",
			"ap-southeast-1": "mongodb.ap-southeast-1.aliyuncs.com",
			"ap-southeast-2": "mongodb.ap-southeast-2.aliyuncs.com",
			"ap-southeast-3": "mongodb.ap-southeast-3.aliyuncs.com",
			"ap-southeast-5": "mongodb.ap-southeast-5.aliyuncs.com",
			"us-east-1": "mongodb.us-east-1.aliyuncs.com",
			"cn-shenzhen-inner": "mongodb.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "mongodb.aliyuncs.com",
			"cn-beijing-gov-1": "mongodb.aliyuncs.com",
			"cn-wulanchabu": "mongodb.aliyuncs.com",
			"ap-south-1": "mongodb.ap-south-1.aliyuncs.com",
			"cn-shenzhen-st4-d01": "mongodb.aliyuncs.com",
			"cn-haidian-cm12-c01": "mongodb.aliyuncs.com",
			"cn-qingdao": "mongodb.aliyuncs.com",
			"cn-hongkong-finance-pop": "mongodb.aliyuncs.com",
			"cn-shanghai": "mongodb.aliyuncs.com",
			"cn-shanghai-finance-1": "mongodb.aliyuncs.com",
			"cn-hongkong": "mongodb.cn-hongkong.aliyuncs.com",
			"eu-central-1": "mongodb.eu-central-1.aliyuncs.com",
			"cn-shenzhen": "mongodb.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "mongodb.aliyuncs.com",
			"eu-west-1": "mongodb.eu-west-1.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "mongodb.aliyuncs.com",
			"eu-west-1-oxs": "mongodb.aliyuncs.com",
			"cn-beijing-finance-1": "mongodb.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "mongodb.aliyuncs.com",
			"cn-shenzhen-finance-1": "mongodb.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "mongodb.aliyuncs.com",
			"me-east-1": "mongodb.me-east-1.aliyuncs.com",
			"cn-chengdu": "mongodb.cn-chengdu.aliyuncs.com",
			"cn-hangzhou-test-306": "mongodb.aliyuncs.com",
			"cn-guangzhou": "mongodb.aliyuncs.com",
			"cn-hangzhou-finance": "mongodb.aliyuncs.com",
			"cn-beijing-nu16-b01": "mongodb.aliyuncs.com",
			"cn-edge-1": "mongodb.aliyuncs.com",
			"cn-huhehaote": "mongodb.cn-huhehaote.aliyuncs.com",
			"cn-fujian": "mongodb.aliyuncs.com",
			"ap-northeast-2-pop": "mongodb.aliyuncs.com",
			"cn-hangzhou": "mongodb.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
