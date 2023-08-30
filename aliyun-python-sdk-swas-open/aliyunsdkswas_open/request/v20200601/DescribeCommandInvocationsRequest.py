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

class DescribeCommandInvocationsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'SWAS-OPEN', '2020-06-01', 'DescribeCommandInvocations','SWAS-OPEN')
		self.set_method('POST')

	def get_CommandId(self): # String
		return self.get_query_params().get('CommandId')

	def set_CommandId(self, CommandId):  # String
		self.add_query_param('CommandId', CommandId)
	def get_PageNumber(self): # String
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # String
		self.add_query_param('PageNumber', PageNumber)
	def get_PageSize(self): # String
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # String
		self.add_query_param('PageSize', PageSize)
	def get_InvokeId(self): # String
		return self.get_query_params().get('InvokeId')

	def set_InvokeId(self, InvokeId):  # String
		self.add_query_param('InvokeId', InvokeId)
	def get_CommandName(self): # String
		return self.get_query_params().get('CommandName')

	def set_CommandName(self, CommandName):  # String
		self.add_query_param('CommandName', CommandName)
	def get_CommandType(self): # String
		return self.get_query_params().get('CommandType')

	def set_CommandType(self, CommandType):  # String
		self.add_query_param('CommandType', CommandType)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_InvocationStatus(self): # String
		return self.get_query_params().get('InvocationStatus')

	def set_InvocationStatus(self, InvocationStatus):  # String
		self.add_query_param('InvocationStatus', InvocationStatus)
