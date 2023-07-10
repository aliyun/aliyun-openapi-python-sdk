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
from aliyunsdkrds.endpoint import endpoint_data

class ModifyPGHbaConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'ModifyPGHbaConfig')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_OpsType(self): # String
		return self.get_query_params().get('OpsType')

	def set_OpsType(self, OpsType):  # String
		self.add_query_param('OpsType', OpsType)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_HbaItems(self): # RepeatList
		return self.get_query_params().get('HbaItem')

	def set_HbaItems(self, HbaItem):  # RepeatList
		for depth1 in range(len(HbaItem)):
			if HbaItem[depth1].get('Database') is not None:
				self.add_query_param('HbaItem.' + str(depth1 + 1) + '.Database', HbaItem[depth1].get('Database'))
			if HbaItem[depth1].get('Address') is not None:
				self.add_query_param('HbaItem.' + str(depth1 + 1) + '.Address', HbaItem[depth1].get('Address'))
			if HbaItem[depth1].get('Method') is not None:
				self.add_query_param('HbaItem.' + str(depth1 + 1) + '.Method', HbaItem[depth1].get('Method'))
			if HbaItem[depth1].get('Type') is not None:
				self.add_query_param('HbaItem.' + str(depth1 + 1) + '.Type', HbaItem[depth1].get('Type'))
			if HbaItem[depth1].get('User') is not None:
				self.add_query_param('HbaItem.' + str(depth1 + 1) + '.User', HbaItem[depth1].get('User'))
			if HbaItem[depth1].get('Mask') is not None:
				self.add_query_param('HbaItem.' + str(depth1 + 1) + '.Mask', HbaItem[depth1].get('Mask'))
			if HbaItem[depth1].get('PriorityId') is not None:
				self.add_query_param('HbaItem.' + str(depth1 + 1) + '.PriorityId', HbaItem[depth1].get('PriorityId'))
			if HbaItem[depth1].get('Option') is not None:
				self.add_query_param('HbaItem.' + str(depth1 + 1) + '.Option', HbaItem[depth1].get('Option'))
