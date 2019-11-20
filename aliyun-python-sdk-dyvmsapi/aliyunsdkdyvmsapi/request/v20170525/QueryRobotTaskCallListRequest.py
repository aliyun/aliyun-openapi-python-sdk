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
from aliyunsdkdyvmsapi.endpoint import endpoint_data

class QueryRobotTaskCallListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dyvmsapi', '2017-05-25', 'QueryRobotTaskCallList','dyvms')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Called(self):
		return self.get_query_params().get('Called')

	def set_Called(self,Called):
		self.add_query_param('Called',Called)

	def get_DialogCountTo(self):
		return self.get_query_params().get('DialogCountTo')

	def set_DialogCountTo(self,DialogCountTo):
		self.add_query_param('DialogCountTo',DialogCountTo)

	def get_DurationFrom(self):
		return self.get_query_params().get('DurationFrom')

	def set_DurationFrom(self,DurationFrom):
		self.add_query_param('DurationFrom',DurationFrom)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_TaskId(self):
		return self.get_query_params().get('TaskId')

	def set_TaskId(self,TaskId):
		self.add_query_param('TaskId',TaskId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_DialogCountFrom(self):
		return self.get_query_params().get('DialogCountFrom')

	def set_DialogCountFrom(self,DialogCountFrom):
		self.add_query_param('DialogCountFrom',DialogCountFrom)

	def get_DurationTo(self):
		return self.get_query_params().get('DurationTo')

	def set_DurationTo(self,DurationTo):
		self.add_query_param('DurationTo',DurationTo)

	def get_HangupDirection(self):
		return self.get_query_params().get('HangupDirection')

	def set_HangupDirection(self,HangupDirection):
		self.add_query_param('HangupDirection',HangupDirection)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_PageNo(self):
		return self.get_query_params().get('PageNo')

	def set_PageNo(self,PageNo):
		self.add_query_param('PageNo',PageNo)

	def get_CallResult(self):
		return self.get_query_params().get('CallResult')

	def set_CallResult(self,CallResult):
		self.add_query_param('CallResult',CallResult)