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
from aliyunsdkdms_enterprise.endpoint import endpoint_data

class ExecuteDataCorrectRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dms-enterprise', '2018-11-01', 'ExecuteDataCorrect','dmsenterprise')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ActionDetail(self):
		return self.get_query_params().get('ActionDetail')

	def set_ActionDetail(self,ActionDetail):
		self.add_query_param('ActionDetail',ActionDetail)

	def get_OrderId(self):
		return self.get_query_params().get('OrderId')

	def set_OrderId(self,OrderId):
		self.add_query_param('OrderId',OrderId)

	def get_Tid(self):
		return self.get_query_params().get('Tid')

	def set_Tid(self,Tid):
		self.add_query_param('Tid',Tid)