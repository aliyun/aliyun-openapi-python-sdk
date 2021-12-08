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

class CreateClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mse', '2019-05-31', 'CreateCluster')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClusterSpecification(self): # String
		return self.get_query_params().get('ClusterSpecification')

	def set_ClusterSpecification(self, ClusterSpecification):  # String
		self.add_query_param('ClusterSpecification', ClusterSpecification)
	def get_PubSlbSpecification(self): # String
		return self.get_query_params().get('PubSlbSpecification')

	def set_PubSlbSpecification(self, PubSlbSpecification):  # String
		self.add_query_param('PubSlbSpecification', PubSlbSpecification)
	def get_PrivateSlbSpecification(self): # String
		return self.get_query_params().get('PrivateSlbSpecification')

	def set_PrivateSlbSpecification(self, PrivateSlbSpecification):  # String
		self.add_query_param('PrivateSlbSpecification', PrivateSlbSpecification)
	def get_InstanceCount(self): # Integer
		return self.get_query_params().get('InstanceCount')

	def set_InstanceCount(self, InstanceCount):  # Integer
		self.add_query_param('InstanceCount', InstanceCount)
	def get_RequestPars(self): # String
		return self.get_query_params().get('RequestPars')

	def set_RequestPars(self, RequestPars):  # String
		self.add_query_param('RequestPars', RequestPars)
	def get_ConnectionType(self): # String
		return self.get_query_params().get('ConnectionType')

	def set_ConnectionType(self, ConnectionType):  # String
		self.add_query_param('ConnectionType', ConnectionType)
	def get_ClusterVersion(self): # String
		return self.get_query_params().get('ClusterVersion')

	def set_ClusterVersion(self, ClusterVersion):  # String
		self.add_query_param('ClusterVersion', ClusterVersion)
	def get_DiskCapacity(self): # Integer
		return self.get_query_params().get('DiskCapacity')

	def set_DiskCapacity(self, DiskCapacity):  # Integer
		self.add_query_param('DiskCapacity', DiskCapacity)
	def get_DiskType(self): # String
		return self.get_query_params().get('DiskType')

	def set_DiskType(self, DiskType):  # String
		self.add_query_param('DiskType', DiskType)
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_ClusterType(self): # String
		return self.get_query_params().get('ClusterType')

	def set_ClusterType(self, ClusterType):  # String
		self.add_query_param('ClusterType', ClusterType)
	def get_PubNetworkFlow(self): # String
		return self.get_query_params().get('PubNetworkFlow')

	def set_PubNetworkFlow(self, PubNetworkFlow):  # String
		self.add_query_param('PubNetworkFlow', PubNetworkFlow)
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
	def get_NetType(self): # String
		return self.get_query_params().get('NetType')

	def set_NetType(self, NetType):  # String
		self.add_query_param('NetType', NetType)
	def get_MseVersion(self): # String
		return self.get_query_params().get('MseVersion')

	def set_MseVersion(self, MseVersion):  # String
		self.add_query_param('MseVersion', MseVersion)
	def get_Region(self): # String
		return self.get_query_params().get('Region')

	def set_Region(self, Region):  # String
		self.add_query_param('Region', Region)
