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
from aliyunsdkiot.endpoint import endpoint_data

class QuerySpeechPushJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'QuerySpeechPushJob','iot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_StatusLists(self):
		return self.get_body_params().get('StatusList')

	def set_StatusLists(self, StatusLists):
		for depth1 in range(len(StatusLists)):
			if StatusLists[depth1] is not None:
				self.add_body_params('StatusList.' + str(depth1 + 1) , StatusLists[depth1])

	def get_ProjectCode(self):
		return self.get_body_params().get('ProjectCode')

	def set_ProjectCode(self,ProjectCode):
		self.add_body_params('ProjectCode', ProjectCode)

	def get_PageId(self):
		return self.get_body_params().get('PageId')

	def set_PageId(self,PageId):
		self.add_body_params('PageId', PageId)

	def get_IotInstanceId(self):
		return self.get_body_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_body_params('IotInstanceId', IotInstanceId)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_PushMode(self):
		return self.get_body_params().get('PushMode')

	def set_PushMode(self,PushMode):
		self.add_body_params('PushMode', PushMode)

	def get_JobCode(self):
		return self.get_query_params().get('JobCode')

	def set_JobCode(self,JobCode):
		self.add_query_param('JobCode',JobCode)