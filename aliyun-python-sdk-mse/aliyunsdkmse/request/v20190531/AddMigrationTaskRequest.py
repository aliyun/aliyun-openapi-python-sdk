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
from aliyunsdkmse.endpoint import endpoint_data

class AddMigrationTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mse', '2019-05-31', 'AddMigrationTask','mse')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TargetClusterUrl(self): # String
		return self.get_query_params().get('TargetClusterUrl')

	def set_TargetClusterUrl(self, TargetClusterUrl):  # String
		self.add_query_param('TargetClusterUrl', TargetClusterUrl)
	def get_OriginInstanceAddress(self): # String
		return self.get_query_params().get('OriginInstanceAddress')

	def set_OriginInstanceAddress(self, OriginInstanceAddress):  # String
		self.add_query_param('OriginInstanceAddress', OriginInstanceAddress)
	def get_RequestPars(self): # String
		return self.get_query_params().get('RequestPars')

	def set_RequestPars(self, RequestPars):  # String
		self.add_query_param('RequestPars', RequestPars)
	def get_Id(self): # String
		return self.get_query_params().get('Id')

	def set_Id(self, Id):  # String
		self.add_query_param('Id', Id)
	def get_OriginInstanceName(self): # String
		return self.get_query_params().get('OriginInstanceName')

	def set_OriginInstanceName(self, OriginInstanceName):  # String
		self.add_query_param('OriginInstanceName', OriginInstanceName)
	def get_ProjectDesc(self): # String
		return self.get_query_params().get('ProjectDesc')

	def set_ProjectDesc(self, ProjectDesc):  # String
		self.add_query_param('ProjectDesc', ProjectDesc)
	def get_OriginInstanceNamespace(self): # String
		return self.get_query_params().get('OriginInstanceNamespace')

	def set_OriginInstanceNamespace(self, OriginInstanceNamespace):  # String
		self.add_query_param('OriginInstanceNamespace', OriginInstanceNamespace)
	def get_ClusterType(self): # String
		return self.get_query_params().get('ClusterType')

	def set_ClusterType(self, ClusterType):  # String
		self.add_query_param('ClusterType', ClusterType)
	def get_TargetInstanceId(self): # String
		return self.get_query_params().get('TargetInstanceId')

	def set_TargetInstanceId(self, TargetInstanceId):  # String
		self.add_query_param('TargetInstanceId', TargetInstanceId)
	def get_TargetClusterName(self): # String
		return self.get_query_params().get('TargetClusterName')

	def set_TargetClusterName(self, TargetClusterName):  # String
		self.add_query_param('TargetClusterName', TargetClusterName)
	def get_AcceptLanguage(self): # String
		return self.get_query_params().get('AcceptLanguage')

	def set_AcceptLanguage(self, AcceptLanguage):  # String
		self.add_query_param('AcceptLanguage', AcceptLanguage)
