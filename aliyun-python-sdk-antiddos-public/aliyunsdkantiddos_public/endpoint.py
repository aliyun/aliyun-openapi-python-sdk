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
			"cn-shanghai-internal-test-1": "antiddos.aliyuncs.com",
			"cn-shenzhen-su18-b01": "antiddos.aliyuncs.com",
			"cn-beijing": "antiddos-openapi-vpc.cn-beijing.aliyuncs.com",
			"cn-shanghai-inner": "antiddos.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "antiddos.aliyuncs.com",
			"cn-north-2-gov-1": "antiddos.aliyuncs.com",
			"cn-yushanfang": "antiddos.aliyuncs.com",
			"cn-qingdao-nebula": "antiddos.aliyuncs.com",
			"cn-beijing-finance-pop": "antiddos.aliyuncs.com",
			"cn-wuhan": "antiddos.aliyuncs.com",
			"cn-zhangjiakou": "antiddos-openapi.cn-zhangjiakou.aliyuncs.com",
			"us-west-1": "antiddos.aliyuncs.com",
			"cn-zhangbei": "antiddos.aliyuncs.com",
			"rus-west-1-pop": "antiddos.aliyuncs.com",
			"cn-shanghai-et15-b01": "antiddos.aliyuncs.com",
			"cn-hangzhou-bj-b01": "antiddos.aliyuncs.com",
			"cn-zhangbei-na61-b01": "antiddos.aliyuncs.com",
			"ap-northeast-1": "antiddos-openapi.ap-northeast-1.aliyuncs.com",
			"cn-huhehaote-nebula-1": "antiddos.aliyuncs.com",
			"cn-shanghai-et2-b01": "antiddos.aliyuncs.com",
			"ap-southeast-1": "antiddos.aliyuncs.com",
			"ap-southeast-2": "antiddos-openapi.ap-southeast-2.aliyuncs.com",
			"ap-southeast-3": "antiddos-openapi.ap-southeast-3.aliyuncs.com",
			"ap-southeast-5": "antiddos-openapi.ap-southeast-5.aliyuncs.com",
			"us-east-1": "antiddos.aliyuncs.com",
			"cn-shenzhen-inner": "antiddos.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "antiddos.aliyuncs.com",
			"cn-beijing-gov-1": "antiddos.aliyuncs.com",
			"cn-wulanchabu": "antiddos-openapi.cn-wulanchabu.aliyuncs.com",
			"ap-south-1": "antiddos-openapi.ap-south-1.aliyuncs.com",
			"cn-shenzhen-st4-d01": "antiddos.aliyuncs.com",
			"cn-haidian-cm12-c01": "antiddos.aliyuncs.com",
			"cn-qingdao": "antiddos-openapi-vpc.cn-qingdao.aliyuncs.com",
			"cn-hongkong-finance-pop": "antiddos.aliyuncs.com",
			"cn-shanghai": "antiddos-openapi-vpc.cn-shanghai.aliyuncs.com",
			"cn-shanghai-finance-1": "antiddos.aliyuncs.com",
			"cn-hongkong": "antiddos-openapi-vpc.cn-hongkong.aliyuncs.com",
			"eu-central-1": "antiddos-openapi.eu-central-1.aliyuncs.com",
			"cn-shenzhen": "antiddos.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "antiddos.aliyuncs.com",
			"eu-west-1": "antiddos-openapi.eu-west-1.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "antiddos.aliyuncs.com",
			"eu-west-1-oxs": "antiddos.aliyuncs.com",
			"cn-beijing-finance-1": "antiddos.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "antiddos.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "antiddos.aliyuncs.com",
			"cn-shenzhen-finance-1": "antiddos.aliyuncs.com",
			"me-east-1": "antiddos-openapi.me-east-1.aliyuncs.com",
			"cn-chengdu": "antiddos-openapi.cn-chengdu.aliyuncs.com",
			"cn-hangzhou-test-306": "antiddos.aliyuncs.com",
			"cn-hangzhou-finance": "antiddos.aliyuncs.com",
			"cn-beijing-nu16-b01": "antiddos.aliyuncs.com",
			"cn-edge-1": "antiddos.aliyuncs.com",
			"cn-huhehaote": "antiddos-openapi.cn-huhehaote.aliyuncs.com",
			"cn-fujian": "antiddos.aliyuncs.com",
			"ap-northeast-2-pop": "antiddos.aliyuncs.com",
			"cn-hangzhou": "antiddos-openapi-vpc.cn-hangzhou.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
