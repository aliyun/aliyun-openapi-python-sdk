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
from aliyunsdksddp.endpoint import endpoint_data

class CreateDataLimitRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sddp', '2019-01-03', 'CreateDataLimit','sddp')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_OcrStatus(self): # Integer
		return self.get_query_params().get('OcrStatus')

	def set_OcrStatus(self, OcrStatus):  # Integer
		self.add_query_param('OcrStatus', OcrStatus)
	def get_ParentId(self): # String
		return self.get_query_params().get('ParentId')

	def set_ParentId(self, ParentId):  # String
		self.add_query_param('ParentId', ParentId)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_ServiceRegionId(self): # String
		return self.get_query_params().get('ServiceRegionId')

	def set_ServiceRegionId(self, ServiceRegionId):  # String
		self.add_query_param('ServiceRegionId', ServiceRegionId)
	def get_EngineType(self): # String
		return self.get_query_params().get('EngineType')

	def set_EngineType(self, EngineType):  # String
		self.add_query_param('EngineType', EngineType)
	def get_AuditStatus(self): # Integer
		return self.get_query_params().get('AuditStatus')

	def set_AuditStatus(self, AuditStatus):  # Integer
		self.add_query_param('AuditStatus', AuditStatus)
	def get_AutoScan(self): # Integer
		return self.get_query_params().get('AutoScan')

	def set_AutoScan(self, AutoScan):  # Integer
		self.add_query_param('AutoScan', AutoScan)
	def get_LogStoreDay(self): # Integer
		return self.get_query_params().get('LogStoreDay')

	def set_LogStoreDay(self, LogStoreDay):  # Integer
		self.add_query_param('LogStoreDay', LogStoreDay)
	def get_ResourceType(self): # Integer
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self, ResourceType):  # Integer
		self.add_query_param('ResourceType', ResourceType)
	def get_Port(self): # Integer
		return self.get_query_params().get('Port')

	def set_Port(self, Port):  # Integer
		self.add_query_param('Port', Port)
	def get_EventStatus(self): # Integer
		return self.get_query_params().get('EventStatus')

	def set_EventStatus(self, EventStatus):  # Integer
		self.add_query_param('EventStatus', EventStatus)
	def get_UserName(self): # String
		return self.get_query_params().get('UserName')

	def set_UserName(self, UserName):  # String
		self.add_query_param('UserName', UserName)
