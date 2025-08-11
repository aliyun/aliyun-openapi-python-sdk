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
import json

class DescribeRCResourcesModificationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'DescribeRCResourcesModification','rds')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Memory(self): # Float
		return self.get_query_params().get('Memory')

	def set_Memory(self, Memory):  # Float
		self.add_query_param('Memory', Memory)
	def get_Cores(self): # Integer
		return self.get_query_params().get('Cores')

	def set_Cores(self, Cores):  # Integer
		self.add_query_param('Cores', Cores)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
	def get_OperationType(self): # String
		return self.get_query_params().get('OperationType')

	def set_OperationType(self, OperationType):  # String
		self.add_query_param('OperationType', OperationType)
	def get_DestinationResource(self): # String
		return self.get_query_params().get('DestinationResource')

	def set_DestinationResource(self, DestinationResource):  # String
		self.add_query_param('DestinationResource', DestinationResource)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
	def get_Conditionss(self): # Array
		return self.get_query_params().get('Conditionss')

	def set_Conditionss(self, Conditionss):  # Array
		self.add_query_param("Conditionss", json.dumps(Conditionss))
