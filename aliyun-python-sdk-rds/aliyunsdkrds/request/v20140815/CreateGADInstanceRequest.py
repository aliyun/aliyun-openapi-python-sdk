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

class CreateGADInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'CreateGADInstance')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_CentralRdsDtsAdminAccount(self): # String
		return self.get_query_params().get('CentralRdsDtsAdminAccount')

	def set_CentralRdsDtsAdminAccount(self, CentralRdsDtsAdminAccount):  # String
		self.add_query_param('CentralRdsDtsAdminAccount', CentralRdsDtsAdminAccount)
	def get_CentralRegionId(self): # String
		return self.get_query_params().get('CentralRegionId')

	def set_CentralRegionId(self, CentralRegionId):  # String
		self.add_query_param('CentralRegionId', CentralRegionId)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_UnitNodes(self): # RepeatList
		return self.get_query_params().get('UnitNode')

	def set_UnitNodes(self, UnitNode):  # RepeatList
		for depth1 in range(len(UnitNode)):
			if UnitNode[depth1].get('DBInstanceStorage') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.DBInstanceStorage', UnitNode[depth1].get('DBInstanceStorage'))
			if UnitNode[depth1].get('ZoneIDSlave1') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.ZoneIDSlave1', UnitNode[depth1].get('ZoneIDSlave1'))
			if UnitNode[depth1].get('ZoneIDSlave2') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.ZoneIDSlave2', UnitNode[depth1].get('ZoneIDSlave2'))
			if UnitNode[depth1].get('EngineVersion') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.EngineVersion', UnitNode[depth1].get('EngineVersion'))
			if UnitNode[depth1].get('DbInstanceClass') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.DbInstanceClass', UnitNode[depth1].get('DbInstanceClass'))
			if UnitNode[depth1].get('SecurityIPList') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.SecurityIPList', UnitNode[depth1].get('SecurityIPList'))
			if UnitNode[depth1].get('VSwitchID') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.VSwitchID', UnitNode[depth1].get('VSwitchID'))
			if UnitNode[depth1].get('RegionID') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.RegionID', UnitNode[depth1].get('RegionID'))
			if UnitNode[depth1].get('Engine') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.Engine', UnitNode[depth1].get('Engine'))
			if UnitNode[depth1].get('DtsInstanceClass') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.DtsInstanceClass', UnitNode[depth1].get('DtsInstanceClass'))
			if UnitNode[depth1].get('VpcID') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.VpcID', UnitNode[depth1].get('VpcID'))
			if UnitNode[depth1].get('ZoneID') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.ZoneID', UnitNode[depth1].get('ZoneID'))
			if UnitNode[depth1].get('DBInstanceDescription') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.DBInstanceDescription', UnitNode[depth1].get('DBInstanceDescription'))
			if UnitNode[depth1].get('DBInstanceStorageType') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.DBInstanceStorageType', UnitNode[depth1].get('DBInstanceStorageType'))
			if UnitNode[depth1].get('PayType') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.PayType', UnitNode[depth1].get('PayType'))
			if UnitNode[depth1].get('DtsConflict') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.DtsConflict', UnitNode[depth1].get('DtsConflict'))
	def get_DBList(self): # String
		return self.get_query_params().get('DBList')

	def set_DBList(self, DBList):  # String
		self.add_query_param('DBList', DBList)
	def get_CentralDBInstanceId(self): # String
		return self.get_query_params().get('CentralDBInstanceId')

	def set_CentralDBInstanceId(self, CentralDBInstanceId):  # String
		self.add_query_param('CentralDBInstanceId', CentralDBInstanceId)
	def get_CentralRdsDtsAdminPassword(self): # String
		return self.get_query_params().get('CentralRdsDtsAdminPassword')

	def set_CentralRdsDtsAdminPassword(self, CentralRdsDtsAdminPassword):  # String
		self.add_query_param('CentralRdsDtsAdminPassword', CentralRdsDtsAdminPassword)
