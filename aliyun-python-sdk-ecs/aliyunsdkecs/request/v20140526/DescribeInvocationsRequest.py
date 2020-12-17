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
from aliyunsdkecs.endpoint import endpoint_data

class DescribeInvocationsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribeInvocations','ecs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_InvokeStatus(self):
		return self.get_query_params().get('InvokeStatus')

	def set_InvokeStatus(self,InvokeStatus):
		self.add_query_param('InvokeStatus',InvokeStatus)

	def get_IncludeOutput(self):
		return self.get_query_params().get('IncludeOutput')

	def set_IncludeOutput(self,IncludeOutput):
		self.add_query_param('IncludeOutput',IncludeOutput)

	def get_CommandId(self):
		return self.get_query_params().get('CommandId')

	def set_CommandId(self,CommandId):
		self.add_query_param('CommandId',CommandId)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_ContentEncoding(self):
		return self.get_query_params().get('ContentEncoding')

	def set_ContentEncoding(self,ContentEncoding):
		self.add_query_param('ContentEncoding',ContentEncoding)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_InvokeId(self):
		return self.get_query_params().get('InvokeId')

	def set_InvokeId(self,InvokeId):
		self.add_query_param('InvokeId',InvokeId)

	def get_Timed(self):
		return self.get_query_params().get('Timed')

	def set_Timed(self,Timed):
		self.add_query_param('Timed',Timed)

	def get_CommandName(self):
		return self.get_query_params().get('CommandName')

	def set_CommandName(self,CommandName):
		self.add_query_param('CommandName',CommandName)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_CommandType(self):
		return self.get_query_params().get('CommandType')

	def set_CommandType(self,CommandType):
		self.add_query_param('CommandType',CommandType)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)