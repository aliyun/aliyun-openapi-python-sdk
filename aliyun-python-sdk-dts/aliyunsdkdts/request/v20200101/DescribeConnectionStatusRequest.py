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
from aliyunsdkdts.endpoint import endpoint_data

class DescribeConnectionStatusRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dts', '2020-01-01', 'DescribeConnectionStatus','dts')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SourceEndpointRegion(self):
		return self.get_query_params().get('SourceEndpointRegion')

	def set_SourceEndpointRegion(self,SourceEndpointRegion):
		self.add_query_param('SourceEndpointRegion',SourceEndpointRegion)

	def get_SourceEndpointArchitecture(self):
		return self.get_query_params().get('SourceEndpointArchitecture')

	def set_SourceEndpointArchitecture(self,SourceEndpointArchitecture):
		self.add_query_param('SourceEndpointArchitecture',SourceEndpointArchitecture)

	def get_DestinationEndpointInstanceType(self):
		return self.get_query_params().get('DestinationEndpointInstanceType')

	def set_DestinationEndpointInstanceType(self,DestinationEndpointInstanceType):
		self.add_query_param('DestinationEndpointInstanceType',DestinationEndpointInstanceType)

	def get_SourceEndpointInstanceID(self):
		return self.get_query_params().get('SourceEndpointInstanceID')

	def set_SourceEndpointInstanceID(self,SourceEndpointInstanceID):
		self.add_query_param('SourceEndpointInstanceID',SourceEndpointInstanceID)

	def get_SourceEndpointUserName(self):
		return self.get_query_params().get('SourceEndpointUserName')

	def set_SourceEndpointUserName(self,SourceEndpointUserName):
		self.add_query_param('SourceEndpointUserName',SourceEndpointUserName)

	def get_SourceEndpointDatabaseName(self):
		return self.get_query_params().get('SourceEndpointDatabaseName')

	def set_SourceEndpointDatabaseName(self,SourceEndpointDatabaseName):
		self.add_query_param('SourceEndpointDatabaseName',SourceEndpointDatabaseName)

	def get_DestinationEndpointRegion(self):
		return self.get_query_params().get('DestinationEndpointRegion')

	def set_DestinationEndpointRegion(self,DestinationEndpointRegion):
		self.add_query_param('DestinationEndpointRegion',DestinationEndpointRegion)

	def get_SourceEndpointIP(self):
		return self.get_query_params().get('SourceEndpointIP')

	def set_SourceEndpointIP(self,SourceEndpointIP):
		self.add_query_param('SourceEndpointIP',SourceEndpointIP)

	def get_DestinationEndpointUserName(self):
		return self.get_query_params().get('DestinationEndpointUserName')

	def set_DestinationEndpointUserName(self,DestinationEndpointUserName):
		self.add_query_param('DestinationEndpointUserName',DestinationEndpointUserName)

	def get_DestinationEndpointArchitecture(self):
		return self.get_query_params().get('DestinationEndpointArchitecture')

	def set_DestinationEndpointArchitecture(self,DestinationEndpointArchitecture):
		self.add_query_param('DestinationEndpointArchitecture',DestinationEndpointArchitecture)

	def get_DestinationEndpointOracleSID(self):
		return self.get_query_params().get('DestinationEndpointOracleSID')

	def set_DestinationEndpointOracleSID(self,DestinationEndpointOracleSID):
		self.add_query_param('DestinationEndpointOracleSID',DestinationEndpointOracleSID)

	def get_DestinationEndpointEngineName(self):
		return self.get_query_params().get('DestinationEndpointEngineName')

	def set_DestinationEndpointEngineName(self,DestinationEndpointEngineName):
		self.add_query_param('DestinationEndpointEngineName',DestinationEndpointEngineName)

	def get_DestinationEndpointInstanceID(self):
		return self.get_query_params().get('DestinationEndpointInstanceID')

	def set_DestinationEndpointInstanceID(self,DestinationEndpointInstanceID):
		self.add_query_param('DestinationEndpointInstanceID',DestinationEndpointInstanceID)

	def get_DestinationEndpointPort(self):
		return self.get_query_params().get('DestinationEndpointPort')

	def set_DestinationEndpointPort(self,DestinationEndpointPort):
		self.add_query_param('DestinationEndpointPort',DestinationEndpointPort)

	def get_SourceEndpointPassword(self):
		return self.get_query_params().get('SourceEndpointPassword')

	def set_SourceEndpointPassword(self,SourceEndpointPassword):
		self.add_query_param('SourceEndpointPassword',SourceEndpointPassword)

	def get_SourceEndpointPort(self):
		return self.get_query_params().get('SourceEndpointPort')

	def set_SourceEndpointPort(self,SourceEndpointPort):
		self.add_query_param('SourceEndpointPort',SourceEndpointPort)

	def get_DestinationEndpointIP(self):
		return self.get_query_params().get('DestinationEndpointIP')

	def set_DestinationEndpointIP(self,DestinationEndpointIP):
		self.add_query_param('DestinationEndpointIP',DestinationEndpointIP)

	def get_SourceEndpointInstanceType(self):
		return self.get_query_params().get('SourceEndpointInstanceType')

	def set_SourceEndpointInstanceType(self,SourceEndpointInstanceType):
		self.add_query_param('SourceEndpointInstanceType',SourceEndpointInstanceType)

	def get_SourceEndpointOracleSID(self):
		return self.get_query_params().get('SourceEndpointOracleSID')

	def set_SourceEndpointOracleSID(self,SourceEndpointOracleSID):
		self.add_query_param('SourceEndpointOracleSID',SourceEndpointOracleSID)

	def get_DestinationEndpointDatabaseName(self):
		return self.get_query_params().get('DestinationEndpointDatabaseName')

	def set_DestinationEndpointDatabaseName(self,DestinationEndpointDatabaseName):
		self.add_query_param('DestinationEndpointDatabaseName',DestinationEndpointDatabaseName)

	def get_DestinationEndpointPassword(self):
		return self.get_query_params().get('DestinationEndpointPassword')

	def set_DestinationEndpointPassword(self,DestinationEndpointPassword):
		self.add_query_param('DestinationEndpointPassword',DestinationEndpointPassword)

	def get_SourceEndpointEngineName(self):
		return self.get_query_params().get('SourceEndpointEngineName')

	def set_SourceEndpointEngineName(self,SourceEndpointEngineName):
		self.add_query_param('SourceEndpointEngineName',SourceEndpointEngineName)