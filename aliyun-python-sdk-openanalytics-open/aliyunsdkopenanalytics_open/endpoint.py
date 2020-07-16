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
			"cn-shanghai-internal-test-1": "openanalytics.aliyuncs.com",
			"cn-shenzhen-su18-b01": "openanalytics.aliyuncs.com",
			"cn-beijing": "openanalytics.cn-beijing.aliyuncs.com",
			"cn-shanghai-inner": "openanalytics.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "openanalytics.aliyuncs.com",
			"cn-north-2-gov-1": "openanalytics.aliyuncs.com",
			"cn-yushanfang": "openanalytics.aliyuncs.com",
			"cn-qingdao-nebula": "openanalytics.aliyuncs.com",
			"cn-beijing-finance-pop": "openanalytics.aliyuncs.com",
			"cn-wuhan": "openanalytics.aliyuncs.com",
			"cn-zhangjiakou": "openanalytics.cn-zhangjiakou.aliyuncs.com",
			"us-west-1": "openanalytics.us-west-1.aliyuncs.com",
			"rus-west-1-pop": "openanalytics.ap-northeast-1.aliyuncs.com",
			"cn-shanghai-et15-b01": "openanalytics.aliyuncs.com",
			"cn-hangzhou-bj-b01": "openanalytics.aliyuncs.com",
			"cn-zhangbei-na61-b01": "openanalytics.aliyuncs.com",
			"ap-northeast-1": "datalakeanalytics.ap-northeast-1.aliyuncs.com",
			"cn-shanghai-et2-b01": "openanalytics.aliyuncs.com",
			"ap-southeast-1": "openanalytics.ap-southeast-1.aliyuncs.com",
			"ap-southeast-2": "datalakeanalytics.ap-southeast-2.aliyuncs.com",
			"ap-southeast-3": "openanalytics.ap-southeast-3.aliyuncs.com",
			"us-east-1": "datalakeanalytics.us-east-1.aliyuncs.com",
			"ap-southeast-5": "openanalytics.ap-southeast-5.aliyuncs.com",
			"cn-shenzhen-inner": "openanalytics.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "openanalytics.aliyuncs.com",
			"cn-beijing-gov-1": "openanalytics.aliyuncs.com",
			"ap-south-1": "openanalytics.ap-south-1.aliyuncs.com",
			"cn-shenzhen-st4-d01": "openanalytics.aliyuncs.com",
			"cn-haidian-cm12-c01": "openanalytics.aliyuncs.com",
			"cn-qingdao": "openanalytics.cn-qingdao.aliyuncs.com",
			"cn-hongkong-finance-pop": "openanalytics.aliyuncs.com",
			"cn-shanghai": "openanalytics.cn-shanghai.aliyuncs.com",
			"cn-shanghai-finance-1": "openanalytics.aliyuncs.com",
			"cn-hongkong": "openanalytics.cn-hongkong.aliyuncs.com",
			"eu-central-1": "datalakeanalytics.eu-central-1.aliyuncs.com",
			"cn-shenzhen": "openanalytics.cn-shenzhen.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "openanalytics.aliyuncs.com",
			"eu-west-1": "openanalytics.eu-west-1.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "openanalytics.aliyuncs.com",
			"eu-west-1-oxs": "openanalytics.ap-northeast-1.aliyuncs.com",
			"cn-beijing-finance-1": "openanalytics.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "openanalytics.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "openanalytics.aliyuncs.com",
			"cn-shenzhen-finance-1": "openanalytics.aliyuncs.com",
			"me-east-1": "openanalytics.me-east-1.aliyuncs.com",
			"cn-chengdu": "openanalytics.aliyuncs.com",
			"cn-hangzhou-test-306": "openanalytics.aliyuncs.com",
			"cn-hangzhou-finance": "openanalytics.aliyuncs.com",
			"cn-beijing-nu16-b01": "openanalytics.aliyuncs.com",
			"cn-edge-1": "openanalytics.aliyuncs.com",
			"cn-huhehaote": "openanalytics.cn-huhehaote.aliyuncs.com",
			"cn-fujian": "openanalytics.aliyuncs.com",
			"ap-northeast-2-pop": "openanalytics.ap-northeast-1.aliyuncs.com",
			"cn-hangzhou": "openanalytics.cn-hangzhou.aliyuncs.com",
		}
		self.endpoint_regional = "central"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
