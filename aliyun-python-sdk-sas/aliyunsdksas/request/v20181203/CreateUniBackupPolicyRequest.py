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
from aliyunsdksas.endpoint import endpoint_data

class CreateUniBackupPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'CreateUniBackupPolicy','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DatabaseType(self): # String
		return self.get_query_params().get('DatabaseType')

	def set_DatabaseType(self, DatabaseType):  # String
		self.add_query_param('DatabaseType', DatabaseType)
	def get_SpeedLimiter(self): # Long
		return self.get_query_params().get('SpeedLimiter')

	def set_SpeedLimiter(self, SpeedLimiter):  # Long
		self.add_query_param('SpeedLimiter', SpeedLimiter)
	def get_IncPlan(self): # String
		return self.get_query_params().get('IncPlan')

	def set_IncPlan(self, IncPlan):  # String
		self.add_query_param('IncPlan', IncPlan)
	def get_Uuid(self): # String
		return self.get_query_params().get('Uuid')

	def set_Uuid(self, Uuid):  # String
		self.add_query_param('Uuid', Uuid)
	def get_AccountName(self): # String
		return self.get_query_params().get('AccountName')

	def set_AccountName(self, AccountName):  # String
		self.add_query_param('AccountName', AccountName)
	def get_DatabaseAddByUser(self): # String
		return self.get_query_params().get('DatabaseAddByUser')

	def set_DatabaseAddByUser(self, DatabaseAddByUser):  # String
		self.add_query_param('DatabaseAddByUser', DatabaseAddByUser)
	def get_FullPlan(self): # String
		return self.get_query_params().get('FullPlan')

	def set_FullPlan(self, FullPlan):  # String
		self.add_query_param('FullPlan', FullPlan)
	def get_Retention(self): # Integer
		return self.get_query_params().get('Retention')

	def set_Retention(self, Retention):  # Integer
		self.add_query_param('Retention', Retention)
	def get_AccountPassword(self): # String
		return self.get_query_params().get('AccountPassword')

	def set_AccountPassword(self, AccountPassword):  # String
		self.add_query_param('AccountPassword', AccountPassword)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_PolicyName(self): # String
		return self.get_query_params().get('PolicyName')

	def set_PolicyName(self, PolicyName):  # String
		self.add_query_param('PolicyName', PolicyName)
	def get_UniRegionId(self): # String
		return self.get_query_params().get('UniRegionId')

	def set_UniRegionId(self, UniRegionId):  # String
		self.add_query_param('UniRegionId', UniRegionId)
