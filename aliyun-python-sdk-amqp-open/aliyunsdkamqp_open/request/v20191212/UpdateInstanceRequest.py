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
from aliyunsdkamqp_open.endpoint import endpoint_data

class UpdateInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'amqp-open', '2019-12-12', 'UpdateInstance','onsproxy')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_MaxPrivateTps(self): # Long
		return self.get_query_params().get('MaxPrivateTps')

	def set_MaxPrivateTps(self, MaxPrivateTps):  # Long
		self.add_query_param('MaxPrivateTps', MaxPrivateTps)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_StorageSize(self): # Integer
		return self.get_query_params().get('StorageSize')

	def set_StorageSize(self, StorageSize):  # Integer
		self.add_query_param('StorageSize', StorageSize)
	def get_QueueCapacity(self): # Integer
		return self.get_query_params().get('QueueCapacity')

	def set_QueueCapacity(self, QueueCapacity):  # Integer
		self.add_query_param('QueueCapacity', QueueCapacity)
	def get_TracingStorageTime(self): # Integer
		return self.get_query_params().get('TracingStorageTime')

	def set_TracingStorageTime(self, TracingStorageTime):  # Integer
		self.add_query_param('TracingStorageTime', TracingStorageTime)
	def get_MaxConnections(self): # Integer
		return self.get_query_params().get('MaxConnections')

	def set_MaxConnections(self, MaxConnections):  # Integer
		self.add_query_param('MaxConnections', MaxConnections)
	def get_SupportTracing(self): # Boolean
		return self.get_query_params().get('SupportTracing')

	def set_SupportTracing(self, SupportTracing):  # Boolean
		self.add_query_param('SupportTracing', SupportTracing)
	def get_ServerlessChargeType(self): # String
		return self.get_query_params().get('ServerlessChargeType')

	def set_ServerlessChargeType(self, ServerlessChargeType):  # String
		self.add_query_param('ServerlessChargeType', ServerlessChargeType)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_SupportEip(self): # Boolean
		return self.get_query_params().get('SupportEip')

	def set_SupportEip(self, SupportEip):  # Boolean
		self.add_query_param('SupportEip', SupportEip)
	def get_ModifyType(self): # String
		return self.get_query_params().get('ModifyType')

	def set_ModifyType(self, ModifyType):  # String
		self.add_query_param('ModifyType', ModifyType)
	def get_MaxEipTps(self): # Long
		return self.get_query_params().get('MaxEipTps')

	def set_MaxEipTps(self, MaxEipTps):  # Long
		self.add_query_param('MaxEipTps', MaxEipTps)
