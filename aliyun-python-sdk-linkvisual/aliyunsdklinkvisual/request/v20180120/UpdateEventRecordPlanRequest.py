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
from aliyunsdklinkvisual.endpoint import endpoint_data

class UpdateEventRecordPlanRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Linkvisual', '2018-01-20', 'UpdateEventRecordPlan','Linkvisual')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_EventTypes(self): # String
		return self.get_query_params().get('EventTypes')

	def set_EventTypes(self, EventTypes):  # String
		self.add_query_param('EventTypes', EventTypes)
	def get_PreRecordDuration(self): # Integer
		return self.get_query_params().get('PreRecordDuration')

	def set_PreRecordDuration(self, PreRecordDuration):  # Integer
		self.add_query_param('PreRecordDuration', PreRecordDuration)
	def get_RecordDuration(self): # Integer
		return self.get_query_params().get('RecordDuration')

	def set_RecordDuration(self, RecordDuration):  # Integer
		self.add_query_param('RecordDuration', RecordDuration)
	def get_TemplateId(self): # String
		return self.get_query_params().get('TemplateId')

	def set_TemplateId(self, TemplateId):  # String
		self.add_query_param('TemplateId', TemplateId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_PlanId(self): # String
		return self.get_query_params().get('PlanId')

	def set_PlanId(self, PlanId):  # String
		self.add_query_param('PlanId', PlanId)
