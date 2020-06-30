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
from aliyunsdksmartag.endpoint import endpoint_data

class ModifySagRouteProtocolOspfRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Smartag', '2018-03-13', 'ModifySagRouteProtocolOspf','smartag')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_AuthenticationType(self):
		return self.get_query_params().get('AuthenticationType')

	def set_AuthenticationType(self,AuthenticationType):
		self.add_query_param('AuthenticationType',AuthenticationType)

	def get_Password(self):
		return self.get_query_params().get('Password')

	def set_Password(self,Password):
		self.add_query_param('Password',Password)

	def get_AreaId(self):
		return self.get_query_params().get('AreaId')

	def set_AreaId(self,AreaId):
		self.add_query_param('AreaId',AreaId)

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

	def get_Md5KeyId(self):
		return self.get_query_params().get('Md5KeyId')

	def set_Md5KeyId(self,Md5KeyId):
		self.add_query_param('Md5KeyId',Md5KeyId)

	def get_RouterId(self):
		return self.get_query_params().get('RouterId')

	def set_RouterId(self,RouterId):
		self.add_query_param('RouterId',RouterId)

	def get_SmartAGId(self):
		return self.get_query_params().get('SmartAGId')

	def set_SmartAGId(self,SmartAGId):
		self.add_query_param('SmartAGId',SmartAGId)

	def get_SmartAGSn(self):
		return self.get_query_params().get('SmartAGSn')

	def set_SmartAGSn(self,SmartAGSn):
		self.add_query_param('SmartAGSn',SmartAGSn)

	def get_DeadTime(self):
		return self.get_query_params().get('DeadTime')

	def set_DeadTime(self,DeadTime):
		self.add_query_param('DeadTime',DeadTime)

	def get_Md5Key(self):
		return self.get_query_params().get('Md5Key')

	def set_Md5Key(self,Md5Key):
		self.add_query_param('Md5Key',Md5Key)

	def get_HelloTime(self):
		return self.get_query_params().get('HelloTime')

	def set_HelloTime(self,HelloTime):
		self.add_query_param('HelloTime',HelloTime)