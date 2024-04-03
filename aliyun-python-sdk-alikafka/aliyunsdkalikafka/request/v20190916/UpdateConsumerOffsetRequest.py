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
from aliyunsdkalikafka.endpoint import endpoint_data
import json

class UpdateConsumerOffsetRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'alikafka', '2019-09-16', 'UpdateConsumerOffset','alikafka')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ConsumerId(self): # String
		return self.get_query_params().get('ConsumerId')

	def set_ConsumerId(self, ConsumerId):  # String
		self.add_query_param('ConsumerId', ConsumerId)
	def get_ResetType(self): # String
		return self.get_query_params().get('ResetType')

	def set_ResetType(self, ResetType):  # String
		self.add_query_param('ResetType', ResetType)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_Offsets(self): # Array
		return self.get_query_params().get('Offsets')

	def set_Offsets(self, Offsets):  # Array
		self.add_query_param("Offsets", json.dumps(Offsets))
	def get_Topic(self): # String
		return self.get_query_params().get('Topic')

	def set_Topic(self, Topic):  # String
		self.add_query_param('Topic', Topic)
	def get_Time(self): # String
		return self.get_query_params().get('Time')

	def set_Time(self, Time):  # String
		self.add_query_param('Time', Time)
