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
from aliyunsdkdts.endpoint import endpoint_data

class ModifyDtsJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dts', '2020-01-01', 'ModifyDtsJob','dts')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DbList(self): # String
		return self.get_body_params().get('DbList')

	def set_DbList(self, DbList):  # String
		self.add_body_params('DbList', DbList)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_ModifyTypeEnum(self): # String
		return self.get_body_params().get('ModifyTypeEnum')

	def set_ModifyTypeEnum(self, ModifyTypeEnum):  # String
		self.add_body_params('ModifyTypeEnum', ModifyTypeEnum)
	def get_EtlOperatorColumnReference(self): # String
		return self.get_body_params().get('EtlOperatorColumnReference')

	def set_EtlOperatorColumnReference(self, EtlOperatorColumnReference):  # String
		self.add_body_params('EtlOperatorColumnReference', EtlOperatorColumnReference)
	def get_Reserved(self): # String
		return self.get_body_params().get('Reserved')

	def set_Reserved(self, Reserved):  # String
		self.add_body_params('Reserved', Reserved)
	def get_DtsInstanceId(self): # String
		return self.get_query_params().get('DtsInstanceId')

	def set_DtsInstanceId(self, DtsInstanceId):  # String
		self.add_query_param('DtsInstanceId', DtsInstanceId)
	def get_SynchronizationDirection(self): # String
		return self.get_query_params().get('SynchronizationDirection')

	def set_SynchronizationDirection(self, SynchronizationDirection):  # String
		self.add_query_param('SynchronizationDirection', SynchronizationDirection)
