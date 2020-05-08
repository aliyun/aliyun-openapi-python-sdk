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
from aliyunsdkdms_enterprise.endpoint import endpoint_data

class UpdateInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dms-enterprise', '2018-11-01', 'UpdateInstance','dmsenterprise')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SafeRuleId(self):
		return self.get_query_params().get('SafeRuleId')

	def set_SafeRuleId(self,SafeRuleId):
		self.add_query_param('SafeRuleId',SafeRuleId)

	def get_EcsRegion(self):
		return self.get_query_params().get('EcsRegion')

	def set_EcsRegion(self,EcsRegion):
		self.add_query_param('EcsRegion',EcsRegion)

	def get_DdlOnline(self):
		return self.get_query_params().get('DdlOnline')

	def set_DdlOnline(self,DdlOnline):
		self.add_query_param('DdlOnline',DdlOnline)

	def get_UseDsql(self):
		return self.get_query_params().get('UseDsql')

	def set_UseDsql(self,UseDsql):
		self.add_query_param('UseDsql',UseDsql)

	def get_Tid(self):
		return self.get_query_params().get('Tid')

	def set_Tid(self,Tid):
		self.add_query_param('Tid',Tid)

	def get_Sid(self):
		return self.get_query_params().get('Sid')

	def set_Sid(self,Sid):
		self.add_query_param('Sid',Sid)

	def get_DbaId(self):
		return self.get_query_params().get('DbaId')

	def set_DbaId(self,DbaId):
		self.add_query_param('DbaId',DbaId)

	def get_DataLinkName(self):
		return self.get_query_params().get('DataLinkName')

	def set_DataLinkName(self,DataLinkName):
		self.add_query_param('DataLinkName',DataLinkName)

	def get_InstanceSource(self):
		return self.get_query_params().get('InstanceSource')

	def set_InstanceSource(self,InstanceSource):
		self.add_query_param('InstanceSource',InstanceSource)

	def get_EnvType(self):
		return self.get_query_params().get('EnvType')

	def set_EnvType(self,EnvType):
		self.add_query_param('EnvType',EnvType)

	def get_Host(self):
		return self.get_query_params().get('Host')

	def set_Host(self,Host):
		self.add_query_param('Host',Host)

	def get_InstanceType(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self,InstanceType):
		self.add_query_param('InstanceType',InstanceType)

	def get_QueryTimeout(self):
		return self.get_query_params().get('QueryTimeout')

	def set_QueryTimeout(self,QueryTimeout):
		self.add_query_param('QueryTimeout',QueryTimeout)

	def get_EcsInstanceId(self):
		return self.get_query_params().get('EcsInstanceId')

	def set_EcsInstanceId(self,EcsInstanceId):
		self.add_query_param('EcsInstanceId',EcsInstanceId)

	def get_ExportTimeout(self):
		return self.get_query_params().get('ExportTimeout')

	def set_ExportTimeout(self,ExportTimeout):
		self.add_query_param('ExportTimeout',ExportTimeout)

	def get_DatabasePassword(self):
		return self.get_query_params().get('DatabasePassword')

	def set_DatabasePassword(self,DatabasePassword):
		self.add_query_param('DatabasePassword',DatabasePassword)

	def get_InstanceAlias(self):
		return self.get_query_params().get('InstanceAlias')

	def set_InstanceAlias(self,InstanceAlias):
		self.add_query_param('InstanceAlias',InstanceAlias)

	def get_DatabaseUser(self):
		return self.get_query_params().get('DatabaseUser')

	def set_DatabaseUser(self,DatabaseUser):
		self.add_query_param('DatabaseUser',DatabaseUser)

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