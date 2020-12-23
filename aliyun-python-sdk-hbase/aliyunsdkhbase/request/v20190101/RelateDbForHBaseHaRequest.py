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
from aliyunsdkhbase.endpoint import endpoint_data

class RelateDbForHBaseHaRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'HBase', '2019-01-01', 'RelateDbForHBaseHa','hbase')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_HaMigrateType(self):
		return self.get_query_params().get('HaMigrateType')

	def set_HaMigrateType(self,HaMigrateType):
		self.add_query_param('HaMigrateType',HaMigrateType)

	def get_HaActiveHdfsUri(self):
		return self.get_query_params().get('HaActiveHdfsUri')

	def set_HaActiveHdfsUri(self,HaActiveHdfsUri):
		self.add_query_param('HaActiveHdfsUri',HaActiveHdfsUri)

	def get_HaStandbyVersion(self):
		return self.get_query_params().get('HaStandbyVersion')

	def set_HaStandbyVersion(self,HaStandbyVersion):
		self.add_query_param('HaStandbyVersion',HaStandbyVersion)

	def get_IsStandbyStandard(self):
		return self.get_query_params().get('IsStandbyStandard')

	def set_IsStandbyStandard(self,IsStandbyStandard):
		self.add_query_param('IsStandbyStandard',IsStandbyStandard)

	def get_HaActiveClusterKey(self):
		return self.get_query_params().get('HaActiveClusterKey')

	def set_HaActiveClusterKey(self,HaActiveClusterKey):
		self.add_query_param('HaActiveClusterKey',HaActiveClusterKey)

	def get_HaStandbyPassword(self):
		return self.get_query_params().get('HaStandbyPassword')

	def set_HaStandbyPassword(self,HaStandbyPassword):
		self.add_query_param('HaStandbyPassword',HaStandbyPassword)

	def get_HaStandbyClusterKey(self):
		return self.get_query_params().get('HaStandbyClusterKey')

	def set_HaStandbyClusterKey(self,HaStandbyClusterKey):
		self.add_query_param('HaStandbyClusterKey',HaStandbyClusterKey)

	def get_HaStandbyHbaseFsDir(self):
		return self.get_query_params().get('HaStandbyHbaseFsDir')

	def set_HaStandbyHbaseFsDir(self,HaStandbyHbaseFsDir):
		self.add_query_param('HaStandbyHbaseFsDir',HaStandbyHbaseFsDir)

	def get_HaActiveHbaseFsDir(self):
		return self.get_query_params().get('HaActiveHbaseFsDir')

	def set_HaActiveHbaseFsDir(self,HaActiveHbaseFsDir):
		self.add_query_param('HaActiveHbaseFsDir',HaActiveHbaseFsDir)

	def get_HaActiveDBType(self):
		return self.get_query_params().get('HaActiveDBType')

	def set_HaActiveDBType(self,HaActiveDBType):
		self.add_query_param('HaActiveDBType',HaActiveDBType)

	def get_HaActivePassword(self):
		return self.get_query_params().get('HaActivePassword')

	def set_HaActivePassword(self,HaActivePassword):
		self.add_query_param('HaActivePassword',HaActivePassword)

	def get_IsActiveStandard(self):
		return self.get_query_params().get('IsActiveStandard')

	def set_IsActiveStandard(self,IsActiveStandard):
		self.add_query_param('IsActiveStandard',IsActiveStandard)

	def get_HaStandbyUser(self):
		return self.get_query_params().get('HaStandbyUser')

	def set_HaStandbyUser(self,HaStandbyUser):
		self.add_query_param('HaStandbyUser',HaStandbyUser)

	def get_HaActive(self):
		return self.get_query_params().get('HaActive')

	def set_HaActive(self,HaActive):
		self.add_query_param('HaActive',HaActive)

	def get_HaStandby(self):
		return self.get_query_params().get('HaStandby')

	def set_HaStandby(self,HaStandby):
		self.add_query_param('HaStandby',HaStandby)

	def get_HaStandbyHdfsUri(self):
		return self.get_query_params().get('HaStandbyHdfsUri')

	def set_HaStandbyHdfsUri(self,HaStandbyHdfsUri):
		self.add_query_param('HaStandbyHdfsUri',HaStandbyHdfsUri)

	def get_HaActiveVersion(self):
		return self.get_query_params().get('HaActiveVersion')

	def set_HaActiveVersion(self,HaActiveVersion):
		self.add_query_param('HaActiveVersion',HaActiveVersion)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_HaStandbyDBType(self):
		return self.get_query_params().get('HaStandbyDBType')

	def set_HaStandbyDBType(self,HaStandbyDBType):
		self.add_query_param('HaStandbyDBType',HaStandbyDBType)

	def get_HaTables(self):
		return self.get_query_params().get('HaTables')

	def set_HaTables(self,HaTables):
		self.add_query_param('HaTables',HaTables)

	def get_HaActiveUser(self):
		return self.get_query_params().get('HaActiveUser')

	def set_HaActiveUser(self,HaActiveUser):
		self.add_query_param('HaActiveUser',HaActiveUser)