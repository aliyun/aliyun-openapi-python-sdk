# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkretailcloud.endpoint import endpoint_data

class SubmitInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'retailcloud', '2018-03-13', 'SubmitInfo')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RequestId(self): # String
		return self.get_query_params().get('RequestId')

	def set_RequestId(self, RequestId):  # String
		self.add_query_param('RequestId', RequestId)
	def get_MainUserId(self): # Long
		return self.get_query_params().get('MainUserId')

	def set_MainUserId(self, MainUserId):  # Long
		self.add_query_param('MainUserId', MainUserId)
	def get_EcsDescLists(self): # RepeatList
		return self.get_body_params().get('EcsDescList')

	def set_EcsDescLists(self, EcsDescList):  # RepeatList
		for depth1 in range(len(EcsDescList)):
			if EcsDescList[depth1].get('BussinessDesc') is not None:
				self.add_body_params('EcsDescList.' + str(depth1 + 1) + '.BussinessDesc', EcsDescList[depth1].get('BussinessDesc'))
			if EcsDescList[depth1].get('MiddleWareDesc') is not None:
				self.add_body_params('EcsDescList.' + str(depth1 + 1) + '.MiddleWareDesc', EcsDescList[depth1].get('MiddleWareDesc'))
			if EcsDescList[depth1].get('ResourceId') is not None:
				self.add_body_params('EcsDescList.' + str(depth1 + 1) + '.ResourceId', EcsDescList[depth1].get('ResourceId'))
			if EcsDescList[depth1].get('OtherMiddleWareDesc') is not None:
				self.add_body_params('EcsDescList.' + str(depth1 + 1) + '.OtherMiddleWareDesc', EcsDescList[depth1].get('OtherMiddleWareDesc'))
			if EcsDescList[depth1].get('BussinessType') is not None:
				self.add_body_params('EcsDescList.' + str(depth1 + 1) + '.BussinessType', EcsDescList[depth1].get('BussinessType'))
			if EcsDescList[depth1].get('AppType') is not None:
				self.add_body_params('EcsDescList.' + str(depth1 + 1) + '.AppType', EcsDescList[depth1].get('AppType'))
			if EcsDescList[depth1].get('EnvType') is not None:
				self.add_body_params('EcsDescList.' + str(depth1 + 1) + '.EnvType', EcsDescList[depth1].get('EnvType'))
			if EcsDescList[depth1].get('UserId') is not None:
				self.add_body_params('EcsDescList.' + str(depth1 + 1) + '.UserId', EcsDescList[depth1].get('UserId'))
	def get_CallerUid(self): # Long
		return self.get_query_params().get('CallerUid')

	def set_CallerUid(self, CallerUid):  # Long
		self.add_query_param('CallerUid', CallerUid)
