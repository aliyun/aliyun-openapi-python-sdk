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

class UpdateNacosInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mse', '2019-05-31', 'UpdateNacosInstance')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Metadata(self): # String
		return self.get_body_params().get('Metadata')

	def set_Metadata(self, Metadata):  # String
		self.add_body_params('Metadata', Metadata)
	def get_ClusterName(self): # String
		return self.get_query_params().get('ClusterName')

	def set_ClusterName(self, ClusterName):  # String
		self.add_query_param('ClusterName', ClusterName)
	def get_Ip(self): # String
		return self.get_query_params().get('Ip')

	def set_Ip(self, Ip):  # String
		self.add_query_param('Ip', Ip)
	def get_Ephemeral(self): # Boolean
		return self.get_query_params().get('Ephemeral')

	def set_Ephemeral(self, Ephemeral):  # Boolean
		self.add_query_param('Ephemeral', Ephemeral)
	def get_Weight(self): # String
		return self.get_query_params().get('Weight')

	def set_Weight(self, Weight):  # String
		self.add_query_param('Weight', Weight)
	def get_GroupName(self): # String
		return self.get_query_params().get('GroupName')

	def set_GroupName(self, GroupName):  # String
		self.add_query_param('GroupName', GroupName)
	def get_Enabled(self): # Boolean
		return self.get_query_params().get('Enabled')

	def set_Enabled(self, Enabled):  # Boolean
		self.add_query_param('Enabled', Enabled)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_NamespaceId(self): # String
		return self.get_query_params().get('NamespaceId')

	def set_NamespaceId(self, NamespaceId):  # String
		self.add_query_param('NamespaceId', NamespaceId)
	def get_Port(self): # Integer
		return self.get_query_params().get('Port')

	def set_Port(self, Port):  # Integer
		self.add_query_param('Port', Port)
	def get_ServiceName(self): # String
		return self.get_query_params().get('ServiceName')

	def set_ServiceName(self, ServiceName):  # String
		self.add_query_param('ServiceName', ServiceName)
