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
from aliyunsdksmartag.endpoint import endpoint_data

class ModifyQosCarRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Smartag', '2018-03-13', 'ModifyQosCar','smartag')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_MinBandwidthAbs(self):
		return self.get_query_params().get('MinBandwidthAbs')

	def set_MinBandwidthAbs(self,MinBandwidthAbs):
		self.add_query_param('MinBandwidthAbs',MinBandwidthAbs)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_PercentSourceType(self):
		return self.get_query_params().get('PercentSourceType')

	def set_PercentSourceType(self,PercentSourceType):
		self.add_query_param('PercentSourceType',PercentSourceType)

	def get_QosId(self):
		return self.get_query_params().get('QosId')

	def set_QosId(self,QosId):
		self.add_query_param('QosId',QosId)

	def get_MaxBandwidthAbs(self):
		return self.get_query_params().get('MaxBandwidthAbs')

	def set_MaxBandwidthAbs(self,MaxBandwidthAbs):
		self.add_query_param('MaxBandwidthAbs',MaxBandwidthAbs)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_MaxBandwidthPercent(self):
		return self.get_query_params().get('MaxBandwidthPercent')

	def set_MaxBandwidthPercent(self,MaxBandwidthPercent):
		self.add_query_param('MaxBandwidthPercent',MaxBandwidthPercent)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_QosCarId(self):
		return self.get_query_params().get('QosCarId')

	def set_QosCarId(self,QosCarId):
		self.add_query_param('QosCarId',QosCarId)

	def get_Priority(self):
		return self.get_query_params().get('Priority')

	def set_Priority(self,Priority):
		self.add_query_param('Priority',Priority)

	def get_MinBandwidthPercent(self):
		return self.get_query_params().get('MinBandwidthPercent')

	def set_MinBandwidthPercent(self,MinBandwidthPercent):
		self.add_query_param('MinBandwidthPercent',MinBandwidthPercent)

	def get_LimitType(self):
		return self.get_query_params().get('LimitType')

	def set_LimitType(self,LimitType):
		self.add_query_param('LimitType',LimitType)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)