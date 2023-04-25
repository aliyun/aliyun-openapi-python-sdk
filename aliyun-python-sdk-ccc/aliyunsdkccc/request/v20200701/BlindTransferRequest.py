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
from aliyunsdkccc.endpoint import endpoint_data

class BlindTransferRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCC', '2020-07-01', 'BlindTransfer','CCC')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Transferee(self): # String
		return self.get_query_params().get('Transferee')

	def set_Transferee(self, Transferee):  # String
		self.add_query_param('Transferee', Transferee)
	def get_Transferor(self): # String
		return self.get_query_params().get('Transferor')

	def set_Transferor(self, Transferor):  # String
		self.add_query_param('Transferor', Transferor)
	def get_UserId(self): # String
		return self.get_query_params().get('UserId')

	def set_UserId(self, UserId):  # String
		self.add_query_param('UserId', UserId)
	def get_DeviceId(self): # String
		return self.get_query_params().get('DeviceId')

	def set_DeviceId(self, DeviceId):  # String
		self.add_query_param('DeviceId', DeviceId)
	def get_StrategyName(self): # String
		return self.get_query_params().get('StrategyName')

	def set_StrategyName(self, StrategyName):  # String
		self.add_query_param('StrategyName', StrategyName)
	def get_TimeoutSeconds(self): # Integer
		return self.get_query_params().get('TimeoutSeconds')

	def set_TimeoutSeconds(self, TimeoutSeconds):  # Integer
		self.add_query_param('TimeoutSeconds', TimeoutSeconds)
	def get_JobId(self): # String
		return self.get_query_params().get('JobId')

	def set_JobId(self, JobId):  # String
		self.add_query_param('JobId', JobId)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_StrategyParams(self): # String
		return self.get_query_params().get('StrategyParams')

	def set_StrategyParams(self, StrategyParams):  # String
		self.add_query_param('StrategyParams', StrategyParams)
	def get_CallPriority(self): # Integer
		return self.get_query_params().get('CallPriority')

	def set_CallPriority(self, CallPriority):  # Integer
		self.add_query_param('CallPriority', CallPriority)
