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

class CreateDBProxyEndpointAddressRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'CreateDBProxyEndpointAddress','rds')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ConnectionStringPrefix(self):
		return self.get_query_params().get('ConnectionStringPrefix')

	def set_ConnectionStringPrefix(self,ConnectionStringPrefix):
		self.add_query_param('ConnectionStringPrefix',ConnectionStringPrefix)

	def get_DBProxyConnectStringNetType(self):
		return self.get_query_params().get('DBProxyConnectStringNetType')

	def set_DBProxyConnectStringNetType(self,DBProxyConnectStringNetType):
		self.add_query_param('DBProxyConnectStringNetType',DBProxyConnectStringNetType)

	def get_DBInstanceId(self):
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self,DBInstanceId):
		self.add_query_param('DBInstanceId',DBInstanceId)

	def get_DBProxyNewConnectStringPort(self):
		return self.get_query_params().get('DBProxyNewConnectStringPort')

	def set_DBProxyNewConnectStringPort(self,DBProxyNewConnectStringPort):
		self.add_query_param('DBProxyNewConnectStringPort',DBProxyNewConnectStringPort)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_DBProxyEndpointId(self):
		return self.get_query_params().get('DBProxyEndpointId')

	def set_DBProxyEndpointId(self,DBProxyEndpointId):
		self.add_query_param('DBProxyEndpointId',DBProxyEndpointId)

	def get_VPCId(self):
		return self.get_query_params().get('VPCId')

	def set_VPCId(self,VPCId):
		self.add_query_param('VPCId',VPCId)