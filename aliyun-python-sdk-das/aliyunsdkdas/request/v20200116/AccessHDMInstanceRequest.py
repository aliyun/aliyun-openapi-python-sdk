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
from aliyunsdkdas.endpoint import endpoint_data

class AccessHDMInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DAS', '2020-01-16', 'AccessHDMInstance','das')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_skipAuth(self):
		return self.get_query_params().get('skipAuth')

	def set_skipAuth(self,skipAuth):
		self.add_query_param('skipAuth',skipAuth)

	def get_signature(self):
		return self.get_query_params().get('signature')

	def set_signature(self,signature):
		self.add_query_param('signature',signature)

	def get_NetworkType(self):
		return self.get_query_params().get('NetworkType')

	def set_NetworkType(self,NetworkType):
		self.add_query_param('NetworkType',NetworkType)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)

	def get_CallerType(self):
		return self.get_query_params().get('CallerType')

	def set_CallerType(self,CallerType):
		self.add_query_param('CallerType',CallerType)

	def get_Uid(self):
		return self.get_query_params().get('Uid')

	def set_Uid(self,Uid):
		self.add_query_param('Uid',Uid)

	def get_Password(self):
		return self.get_query_params().get('Password')

	def set_Password(self,Password):
		self.add_query_param('Password',Password)

	def get_accessKey(self):
		return self.get_query_params().get('accessKey')

	def set_accessKey(self,accessKey):
		self.add_query_param('accessKey',accessKey)

	def get_Engine(self):
		return self.get_query_params().get('Engine')

	def set_Engine(self,Engine):
		self.add_query_param('Engine',Engine)

	def get_TenantId(self):
		return self.get_query_params().get('TenantId')

	def set_TenantId(self,TenantId):
		self.add_query_param('TenantId',TenantId)

	def get_CallerUid(self):
		return self.get_query_params().get('CallerUid')

	def set_CallerUid(self,CallerUid):
		self.add_query_param('CallerUid',CallerUid)

	def get_timestamp(self):
		return self.get_query_params().get('timestamp')

	def set_timestamp(self,timestamp):
		self.add_query_param('timestamp',timestamp)

	def get_Product(self):
		return self.get_query_params().get('Product')

	def set_Product(self,Product):
		self.add_query_param('Product',Product)

	def get___context(self):
		return self.get_query_params().get('__context')

	def set___context(self,__context):
		self.add_query_param('__context',__context)

	def get_Ip(self):
		return self.get_query_params().get('Ip')

	def set_Ip(self,Ip):
		self.add_query_param('Ip',Ip)

	def get_InstanceAlias(self):
		return self.get_query_params().get('InstanceAlias')

	def set_InstanceAlias(self,InstanceAlias):
		self.add_query_param('InstanceAlias',InstanceAlias)

	def get_CallerBid(self):
		return self.get_query_params().get('CallerBid')

	def set_CallerBid(self,CallerBid):
		self.add_query_param('CallerBid',CallerBid)

	def get_InstanceArea(self):
		return self.get_query_params().get('InstanceArea')

	def set_InstanceArea(self,InstanceArea):
		self.add_query_param('InstanceArea',InstanceArea)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Target(self):
		return self.get_query_params().get('Target')

	def set_Target(self,Target):
		self.add_query_param('Target',Target)

	def get_External(self):
		return self.get_query_params().get('External')

	def set_External(self,External):
		self.add_query_param('External',External)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_Port(self):
		return self.get_query_params().get('Port')

	def set_Port(self,Port):
		self.add_query_param('Port',Port)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_OwnerIdSignature(self):
		return self.get_query_params().get('OwnerIdSignature')

	def set_OwnerIdSignature(self,OwnerIdSignature):
		self.add_query_param('OwnerIdSignature',OwnerIdSignature)

	def get_Region(self):
		return self.get_query_params().get('Region')

	def set_Region(self,Region):
		self.add_query_param('Region',Region)

	def get_Username(self):
		return self.get_query_params().get('Username')

	def set_Username(self,Username):
		self.add_query_param('Username',Username)