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

class ModifySecurityIpsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'ModifySecurityIps','rds')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DBInstanceIPArrayName(self):
		return self.get_query_params().get('DBInstanceIPArrayName')

	def set_DBInstanceIPArrayName(self,DBInstanceIPArrayName):
		self.add_query_param('DBInstanceIPArrayName',DBInstanceIPArrayName)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_SecurityIps(self):
		return self.get_query_params().get('SecurityIps')

	def set_SecurityIps(self,SecurityIps):
		self.add_query_param('SecurityIps',SecurityIps)

	def get_WhitelistNetworkType(self):
		return self.get_query_params().get('WhitelistNetworkType')

	def set_WhitelistNetworkType(self,WhitelistNetworkType):
		self.add_query_param('WhitelistNetworkType',WhitelistNetworkType)

	def get_SecurityIPType(self):
		return self.get_query_params().get('SecurityIPType')

	def set_SecurityIPType(self,SecurityIPType):
		self.add_query_param('SecurityIPType',SecurityIPType)

	def get_DBInstanceId(self):
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self,DBInstanceId):
		self.add_query_param('DBInstanceId',DBInstanceId)

	def get_ModifyMode(self):
		return self.get_query_params().get('ModifyMode')

	def set_ModifyMode(self,ModifyMode):
		self.add_query_param('ModifyMode',ModifyMode)

	def get_DBInstanceIPArrayAttribute(self):
		return self.get_query_params().get('DBInstanceIPArrayAttribute')

	def set_DBInstanceIPArrayAttribute(self,DBInstanceIPArrayAttribute):
		self.add_query_param('DBInstanceIPArrayAttribute',DBInstanceIPArrayAttribute)