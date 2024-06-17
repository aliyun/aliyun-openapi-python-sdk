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
from aliyunsdkpolardbx.endpoint import endpoint_data

class CreateDBInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardbx', '2020-02-02', 'CreateDBInstance','polardbx')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_NetworkType(self): # String
		return self.get_query_params().get('NetworkType')

	def set_NetworkType(self, NetworkType):  # String
		self.add_query_param('NetworkType', NetworkType)
	def get_EngineVersion(self): # String
		return self.get_query_params().get('EngineVersion')

	def set_EngineVersion(self, EngineVersion):  # String
		self.add_query_param('EngineVersion', EngineVersion)
	def get_TertiaryZone(self): # String
		return self.get_query_params().get('TertiaryZone')

	def set_TertiaryZone(self, TertiaryZone):  # String
		self.add_query_param('TertiaryZone', TertiaryZone)
	def get_CnClass(self): # String
		return self.get_query_params().get('CnClass')

	def set_CnClass(self, CnClass):  # String
		self.add_query_param('CnClass', CnClass)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_DBNodeClass(self): # String
		return self.get_query_params().get('DBNodeClass')

	def set_DBNodeClass(self, DBNodeClass):  # String
		self.add_query_param('DBNodeClass', DBNodeClass)
	def get_SecondaryZone(self): # String
		return self.get_query_params().get('SecondaryZone')

	def set_SecondaryZone(self, SecondaryZone):  # String
		self.add_query_param('SecondaryZone', SecondaryZone)
	def get_Period(self): # String
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # String
		self.add_query_param('Period', Period)
	def get_IsReadDBInstance(self): # Boolean
		return self.get_query_params().get('IsReadDBInstance')

	def set_IsReadDBInstance(self, IsReadDBInstance):  # Boolean
		self.add_query_param('IsReadDBInstance', IsReadDBInstance)
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_AutoRenew(self): # Boolean
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self, AutoRenew):  # Boolean
		self.add_query_param('AutoRenew', AutoRenew)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
	def get_CNNodeCount(self): # String
		return self.get_query_params().get('CNNodeCount')

	def set_CNNodeCount(self, CNNodeCount):  # String
		self.add_query_param('CNNodeCount', CNNodeCount)
	def get_PrimaryDBInstanceName(self): # String
		return self.get_query_params().get('PrimaryDBInstanceName')

	def set_PrimaryDBInstanceName(self, PrimaryDBInstanceName):  # String
		self.add_query_param('PrimaryDBInstanceName', PrimaryDBInstanceName)
	def get_TopologyType(self): # String
		return self.get_query_params().get('TopologyType')

	def set_TopologyType(self, TopologyType):  # String
		self.add_query_param('TopologyType', TopologyType)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_IsColumnarReadDBInstance(self): # Boolean
		return self.get_query_params().get('IsColumnarReadDBInstance')

	def set_IsColumnarReadDBInstance(self, IsColumnarReadDBInstance):  # Boolean
		self.add_query_param('IsColumnarReadDBInstance', IsColumnarReadDBInstance)
	def get_DNNodeCount(self): # String
		return self.get_query_params().get('DNNodeCount')

	def set_DNNodeCount(self, DNNodeCount):  # String
		self.add_query_param('DNNodeCount', DNNodeCount)
	def get_DBNodeCount(self): # Integer
		return self.get_query_params().get('DBNodeCount')

	def set_DBNodeCount(self, DBNodeCount):  # Integer
		self.add_query_param('DBNodeCount', DBNodeCount)
	def get_DnClass(self): # String
		return self.get_query_params().get('DnClass')

	def set_DnClass(self, DnClass):  # String
		self.add_query_param('DnClass', DnClass)
	def get_UsedTime(self): # Integer
		return self.get_query_params().get('UsedTime')

	def set_UsedTime(self, UsedTime):  # Integer
		self.add_query_param('UsedTime', UsedTime)
	def get_DnStorageSpace(self): # String
		return self.get_query_params().get('DnStorageSpace')

	def set_DnStorageSpace(self, DnStorageSpace):  # String
		self.add_query_param('DnStorageSpace', DnStorageSpace)
	def get_PrimaryZone(self): # String
		return self.get_query_params().get('PrimaryZone')

	def set_PrimaryZone(self, PrimaryZone):  # String
		self.add_query_param('PrimaryZone', PrimaryZone)
	def get_Series(self): # String
		return self.get_query_params().get('Series')

	def set_Series(self, Series):  # String
		self.add_query_param('Series', Series)
	def get_VPCId(self): # String
		return self.get_query_params().get('VPCId')

	def set_VPCId(self, VPCId):  # String
		self.add_query_param('VPCId', VPCId)
	def get_PayType(self): # String
		return self.get_query_params().get('PayType')

	def set_PayType(self, PayType):  # String
		self.add_query_param('PayType', PayType)
