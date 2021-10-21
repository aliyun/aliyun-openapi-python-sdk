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
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'CreateGADInstance','rds')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DBList(self):
		return self.get_query_params().get('DBList')

	def set_DBList(self,DBList):
		self.add_query_param('DBList',DBList)

	def get_CentralDBInstanceId(self):
		return self.get_query_params().get('CentralDBInstanceId')

	def set_CentralDBInstanceId(self,CentralDBInstanceId):
		self.add_query_param('CentralDBInstanceId',CentralDBInstanceId)

	def get_CentralRdsDtsAdminPassword(self):
		return self.get_query_params().get('CentralRdsDtsAdminPassword')

	def set_CentralRdsDtsAdminPassword(self,CentralRdsDtsAdminPassword):
		self.add_query_param('CentralRdsDtsAdminPassword',CentralRdsDtsAdminPassword)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_CentralRdsDtsAdminAccount(self):
		return self.get_query_params().get('CentralRdsDtsAdminAccount')

	def set_CentralRdsDtsAdminAccount(self,CentralRdsDtsAdminAccount):
		self.add_query_param('CentralRdsDtsAdminAccount',CentralRdsDtsAdminAccount)

	def get_CentralRegionId(self):
		return self.get_query_params().get('CentralRegionId')

	def set_CentralRegionId(self,CentralRegionId):
		self.add_query_param('CentralRegionId',CentralRegionId)

	def get_UnitNodes(self):
		return self.get_query_params().get('UnitNode')

	def set_UnitNodes(self, UnitNodes):
		for depth1 in range(len(UnitNodes)):
			if UnitNodes[depth1].get('DBInstanceStorage') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.DBInstanceStorage', UnitNodes[depth1].get('DBInstanceStorage'))
			if UnitNodes[depth1].get('ZoneIDSlave1') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.ZoneIDSlave1', UnitNodes[depth1].get('ZoneIDSlave1'))
			if UnitNodes[depth1].get('ZoneIDSlave2') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.ZoneIDSlave2', UnitNodes[depth1].get('ZoneIDSlave2'))
			if UnitNodes[depth1].get('EngineVersion') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.EngineVersion', UnitNodes[depth1].get('EngineVersion'))
			if UnitNodes[depth1].get('DbInstanceClass') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.DbInstanceClass', UnitNodes[depth1].get('DbInstanceClass'))
			if UnitNodes[depth1].get('SecurityIPList') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.SecurityIPList', UnitNodes[depth1].get('SecurityIPList'))
			if UnitNodes[depth1].get('VSwitchID') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.VSwitchID', UnitNodes[depth1].get('VSwitchID'))
			if UnitNodes[depth1].get('RegionID') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.RegionID', UnitNodes[depth1].get('RegionID'))
			if UnitNodes[depth1].get('Engine') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.Engine', UnitNodes[depth1].get('Engine'))
			if UnitNodes[depth1].get('DtsInstanceClass') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.DtsInstanceClass', UnitNodes[depth1].get('DtsInstanceClass'))
			if UnitNodes[depth1].get('VpcID') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.VpcID', UnitNodes[depth1].get('VpcID'))
			if UnitNodes[depth1].get('ZoneID') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.ZoneID', UnitNodes[depth1].get('ZoneID'))
			if UnitNodes[depth1].get('DBInstanceDescription') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.DBInstanceDescription', UnitNodes[depth1].get('DBInstanceDescription'))
			if UnitNodes[depth1].get('PayType') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.PayType', UnitNodes[depth1].get('PayType'))
			if UnitNodes[depth1].get('DtsConflict') is not None:
				self.add_query_param('UnitNode.' + str(depth1 + 1) + '.DtsConflict', UnitNodes[depth1].get('DtsConflict'))