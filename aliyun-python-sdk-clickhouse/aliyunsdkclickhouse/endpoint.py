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
			"cn-shanghai-internal-test-1": "clickhouse.aliyuncs.com",
			"cn-beijing-gov-1": "clickhouse.aliyuncs.com",
			"cn-shenzhen-su18-b01": "clickhouse.aliyuncs.com",
			"cn-beijing": "clickhouse.aliyuncs.com",
			"cn-shanghai-inner": "clickhouse.aliyuncs.com",
			"cn-shenzhen-st4-d01": "clickhouse.aliyuncs.com",
			"cn-haidian-cm12-c01": "clickhouse.aliyuncs.com",
			"cn-hangzhou-internal-prod-1": "clickhouse.aliyuncs.com",
			"cn-north-2-gov-1": "clickhouse.aliyuncs.com",
			"cn-yushanfang": "clickhouse.aliyuncs.com",
			"cn-qingdao": "clickhouse.aliyuncs.com",
			"cn-hongkong-finance-pop": "clickhouse.aliyuncs.com",
			"cn-qingdao-nebula": "clickhouse.aliyuncs.com",
			"cn-shanghai": "clickhouse.aliyuncs.com",
			"cn-shanghai-finance-1": "clickhouse.aliyuncs.com",
			"cn-hongkong": "clickhouse.aliyuncs.com",
			"cn-beijing-finance-pop": "clickhouse.aliyuncs.com",
			"cn-wuhan": "clickhouse.aliyuncs.com",
			"us-west-1": "clickhouse.aliyuncs.com",
			"cn-shenzhen": "clickhouse.aliyuncs.com",
			"cn-zhengzhou-nebula-1": "clickhouse.aliyuncs.com",
			"rus-west-1-pop": "clickhouse.aliyuncs.com",
			"cn-shanghai-et15-b01": "clickhouse.aliyuncs.com",
			"cn-hangzhou-bj-b01": "clickhouse.aliyuncs.com",
			"cn-hangzhou-internal-test-1": "clickhouse.aliyuncs.com",
			"eu-west-1-oxs": "clickhouse.aliyuncs.com",
			"cn-zhangbei-na61-b01": "clickhouse.aliyuncs.com",
			"cn-beijing-finance-1": "clickhouse.aliyuncs.com",
			"cn-hangzhou-internal-test-3": "clickhouse.aliyuncs.com",
			"cn-hangzhou-internal-test-2": "clickhouse.aliyuncs.com",
			"cn-shenzhen-finance-1": "clickhouse.aliyuncs.com",
			"me-east-1": "clickhouse.aliyuncs.com",
			"cn-hangzhou-test-306": "clickhouse.aliyuncs.com",
			"cn-shanghai-et2-b01": "clickhouse.aliyuncs.com",
			"cn-hangzhou-finance": "clickhouse.aliyuncs.com",
			"ap-southeast-1": "clickhouse.aliyuncs.com",
			"cn-beijing-nu16-b01": "clickhouse.aliyuncs.com",
			"cn-edge-1": "clickhouse.aliyuncs.com",
			"cn-fujian": "clickhouse.aliyuncs.com",
			"us-east-1": "clickhouse.aliyuncs.com",
			"ap-northeast-2-pop": "clickhouse.aliyuncs.com",
			"cn-shenzhen-inner": "clickhouse.aliyuncs.com",
			"cn-zhangjiakou-na62-a01": "clickhouse.aliyuncs.com",
			"cn-hangzhou": "clickhouse.aliyuncs.com",
		}
		self.endpoint_regional = "regional"

	def getEndpointMap(self):
		return self.endpoint_map

	def getEndpointRegional(self):
		return self.endpoint_regional


endpoint_data = EndpointData()
