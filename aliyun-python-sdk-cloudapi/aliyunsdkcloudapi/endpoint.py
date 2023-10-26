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
			"cn-shanghai-internal-test-1": "apigateway.aliyuncs.com",
			"cn-shenzhen-su18-b01": "apigateway.aliyuncs.com",
			"cn-beijing": "apigateway.cn-beijing.aliyuncs.com",
			"cn-shanghai-inner": "apigateway.cn-shanghai-inner.aliyuncs.com",
			"me-central-1": "apigateway.me-central-1.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "apigateway.aliyuncs.com",
			"cn-north-2-gov-1": "apigateway.cn-north-2-gov-1.aliyuncs.com",
			"cn-yushanfang": "apigateway.aliyuncs.com",
			"cn-qingdao-nebula": "apigateway.aliyuncs.com",
			"cn-heyuan": "apigateway.cn-heyuan.aliyuncs.com",
			"cn-beijing-finance-pop": "apigateway.aliyuncs.com",
			"cn-wuhan": "apigateway.aliyuncs.com",
			"cn-zhangjiakou": "apigateway.cn-zhangjiakou.aliyuncs.com",
			"us-west-1": "apigateway.us-west-1.aliyuncs.com",
			"cn-zhangbei": "apigateway.aliyuncs.com",
			"rus-west-1-pop": "apigateway.aliyuncs.com",
			"cn-shanghai-et15-b01": "apigateway.aliyuncs.com",
			"cn-hangzhou-bj-b01": "apigateway.aliyuncs.com",
			"cn-zhangbei-na61-b01": "apigateway.aliyuncs.com",
			"ap-northeast-1": "apigateway.ap-northeast-1.aliyuncs.com",
			"cn-huhehaote-nebula-1": "apigateway.aliyuncs.com",
			"cn-shanghai-et2-b01": "apigateway.aliyuncs.com",
			"ap-southeast-1": "apigateway.ap-southeast-1.aliyuncs.com",
			"ap-southeast-2": "apigateway.ap-southeast-2.aliyuncs.com",
			"ap-southeast-3": "apigateway.ap-southeast-3.aliyuncs.com",
			"ap-southeast-5": "apigateway.ap-southeast-5.aliyuncs.com",
			"us-east-1": "apigateway.us-east-1.aliyuncs.com",
			"ap-southeast-6": "apigateway.ap-southeast-6.aliyuncs.com",
			"cn-shenzhen-inner": "apigateway.aliyuncs.com",
			"ap-southeast-7": "apigateway.ap-southeast-7.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "apigateway.aliyuncs.com",
			"cn-beijing-gov-1": "apigateway.aliyuncs.com",
			"cn-wulanchabu": "apigateway.cn-wulanchabu.aliyuncs.com",
			"ap-south-1": "apigateway.ap-south-1.aliyuncs.com",
			"cn-shenzhen-st4-d01": "apigateway.aliyuncs.com",
			"cn-haidian-cm12-c01": "apigateway.aliyuncs.com",
			"cn-qingdao": "apigateway.cn-qingdao.aliyuncs.com",
			"cn-hongkong-finance-pop": "apigateway.aliyuncs.com",
			"cn-shanghai": "apigateway.cn-shanghai.aliyuncs.com",
			"cn-shanghai-finance-1": "apigateway.cn-shanghai-finance-1.aliyuncs.com",
			"cn-hongkong": "apigateway.cn-hongkong.aliyuncs.com",
			"eu-central-1": "apigateway.eu-central-1.aliyuncs.com",
			"cn-shenzhen": "apigateway.cn-shenzhen.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "apigateway.aliyuncs.com",
			"eu-west-1": "apigateway.eu-west-1.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "apigateway.aliyuncs.com",
			"eu-west-1-oxs": "apigateway.aliyuncs.com",
			"cn-beijing-finance-1": "apigateway.cn-beijing-finance-1.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "apigateway.aliyuncs.com",
			"cn-shenzhen-finance-1": "apigateway.cn-shenzhen-finance-1.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "apigateway.aliyuncs.com",
			"me-east-1": "apigateway.me-east-1.aliyuncs.com",
			"cn-chengdu": "apigateway.cn-chengdu.aliyuncs.com",
			"cn-hangzhou-test-306": "apigateway.aliyuncs.com",
			"cn-guangzhou": "apigateway.cn-guangzhou.aliyuncs.com",
			"cn-hangzhou-finance": "apigateway.cn-hangzhou-finance.aliyuncs.com",
			"cn-beijing-nu16-b01": "apigateway.aliyuncs.com",
			"cn-edge-1": "apigateway.aliyuncs.com",
			"cn-huhehaote": "apigateway.cn-huhehaote.aliyuncs.com",
			"cn-fujian": "apigateway.aliyuncs.com",
			"ap-northeast-2-pop": "apigateway.aliyuncs.com",
			"cn-hangzhou": "apigateway.cn-hangzhou.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
