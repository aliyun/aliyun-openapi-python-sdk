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
			"cn-shanghai-internal-test-1": "dataworks.aliyuncs.com",
			"cn-shenzhen-su18-b01": "dataworks.aliyuncs.com",
			"cn-beijing": "dataworks.cn-beijing.aliyuncs.com",
			"cn-shanghai-inner": "dataworks.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "dataworks.aliyuncs.com",
			"cn-north-2-gov-1": "dataworks.cn-north-2-gov-1.aliyuncs.com",
			"cn-yushanfang": "dataworks.aliyuncs.com",
			"cn-qingdao-nebula": "dataworks.aliyuncs.com",
			"cn-beijing-finance-pop": "dataworks.aliyuncs.com",
			"cn-wuhan": "dataworks.aliyuncs.com",
			"cn-zhangjiakou": "dataworks.cn-zhangjiakou.aliyuncs.com",
			"us-west-1": "dataworks.us-west-1.aliyuncs.com",
			"cn-zhangbei": "dataworks.aliyuncs.com",
			"rus-west-1-pop": "dataworks.aliyuncs.com",
			"cn-shanghai-et15-b01": "dataworks.aliyuncs.com",
			"cn-hangzhou-bj-b01": "dataworks.aliyuncs.com",
			"cn-zhangbei-na61-b01": "dataworks.aliyuncs.com",
			"ap-northeast-1": "dataworks.ap-northeast-1.aliyuncs.com",
			"cn-huhehaote-nebula-1": "dataworks.aliyuncs.com",
			"cn-shanghai-et2-b01": "dataworks.aliyuncs.com",
			"ap-southeast-1": "dataworks.ap-southeast-1.aliyuncs.com",
			"ap-southeast-2": "dataworks.aliyuncs.com",
			"ap-southeast-3": "dataworks.ap-southeast-3.aliyuncs.com",
			"ap-southeast-5": "dataworks.ap-southeast-5.aliyuncs.com",
			"us-east-1": "dataworks.us-east-1.aliyuncs.com",
			"cn-shenzhen-inner": "dataworks.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "dataworks.aliyuncs.com",
			"cn-beijing-gov-1": "dataworks.aliyuncs.com",
			"cn-wulanchabu": "dataworks.cn-wulanchabu.aliyuncs.com",
			"ap-south-1": "dataworks.aliyuncs.com",
			"cn-shenzhen-st4-d01": "dataworks.aliyuncs.com",
			"cn-haidian-cm12-c01": "dataworks.aliyuncs.com",
			"cn-qingdao": "dataworks.aliyuncs.com",
			"cn-hongkong-finance-pop": "dataworks.aliyuncs.com",
			"cn-shanghai": "dataworks.cn-shanghai.aliyuncs.com",
			"cn-shanghai-finance-1": "dataworks.cn-shanghai-finance-1.aliyuncs.com",
			"cn-hongkong": "dataworks.cn-hongkong.aliyuncs.com",
			"eu-central-1": "dataworks.eu-central-1.aliyuncs.com",
			"cn-shenzhen": "dataworks.cn-shenzhen.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "dataworks.aliyuncs.com",
			"eu-west-1": "dataworks.eu-west-1.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "dataworks.aliyuncs.com",
			"eu-west-1-oxs": "dataworks.aliyuncs.com",
			"cn-beijing-finance-1": "dataworks.cn-beijing-finance-1.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "dataworks.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "dataworks.aliyuncs.com",
			"cn-shenzhen-finance-1": "dataworks.cn-shenzhen-finance-1.aliyuncs.com",
			"me-east-1": "dataworks.me-east-1.aliyuncs.com",
			"cn-chengdu": "dataworks.cn-chengdu.aliyuncs.com",
			"cn-hangzhou-test-306": "dataworks.aliyuncs.com",
			"cn-hangzhou-finance": "dataworks.aliyuncs.com",
			"cn-beijing-nu16-b01": "dataworks.aliyuncs.com",
			"cn-edge-1": "dataworks.aliyuncs.com",
			"cn-huhehaote": "dataworks.aliyuncs.com",
			"cn-fujian": "dataworks.aliyuncs.com",
			"ap-northeast-2-pop": "dataworks.aliyuncs.com",
			"cn-hangzhou": "dataworks.cn-hangzhou.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
