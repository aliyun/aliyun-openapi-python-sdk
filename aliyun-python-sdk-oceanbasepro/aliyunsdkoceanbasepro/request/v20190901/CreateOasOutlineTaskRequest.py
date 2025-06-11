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
from aliyunsdkoceanbasepro.endpoint import endpoint_data

class CreateOasOutlineTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OceanBasePro', '2019-09-01', 'CreateOasOutlineTask','oceanbase')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_StartTime(self): # String
		return self.get_body_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_body_params('StartTime', StartTime)
	def get_UId(self): # String
		return self.get_body_params().get('UId')

	def set_UId(self, UId):  # String
		self.add_body_params('UId', UId)
	def get_DynamicSql(self): # Boolean
		return self.get_body_params().get('DynamicSql')

	def set_DynamicSql(self, DynamicSql):  # Boolean
		self.add_body_params('DynamicSql', DynamicSql)
	def get_SqlText(self): # String
		return self.get_body_params().get('SqlText')

	def set_SqlText(self, SqlText):  # String
		self.add_body_params('SqlText', SqlText)
	def get_BySqlId(self): # Boolean
		return self.get_body_params().get('BySqlId')

	def set_BySqlId(self, BySqlId):  # Boolean
		self.add_body_params('BySqlId', BySqlId)
	def get_MaxConcurrent(self): # Integer
		return self.get_body_params().get('MaxConcurrent')

	def set_MaxConcurrent(self, MaxConcurrent):  # Integer
		self.add_body_params('MaxConcurrent', MaxConcurrent)
	def get_TenantId(self): # String
		return self.get_body_params().get('TenantId')

	def set_TenantId(self, TenantId):  # String
		self.add_body_params('TenantId', TenantId)
	def get_StatementId(self): # String
		return self.get_body_params().get('StatementId')

	def set_StatementId(self, StatementId):  # String
		self.add_body_params('StatementId', StatementId)
	def get_TableName(self): # String
		return self.get_body_params().get('TableName')

	def set_TableName(self, TableName):  # String
		self.add_body_params('TableName', TableName)
	def get_SqlId(self): # String
		return self.get_body_params().get('SqlId')

	def set_SqlId(self, SqlId):  # String
		self.add_body_params('SqlId', SqlId)
	def get_EndTime(self): # String
		return self.get_body_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_body_params('EndTime', EndTime)
	def get_InstanceId(self): # String
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_body_params('InstanceId', InstanceId)
	def get_PlanData(self): # String
		return self.get_body_params().get('PlanData')

	def set_PlanData(self, PlanData):  # String
		self.add_body_params('PlanData', PlanData)
	def get_IndexName(self): # String
		return self.get_body_params().get('IndexName')

	def set_IndexName(self, IndexName):  # String
		self.add_body_params('IndexName', IndexName)
	def get_DatabaseName(self): # String
		return self.get_body_params().get('DatabaseName')

	def set_DatabaseName(self, DatabaseName):  # String
		self.add_body_params('DatabaseName', DatabaseName)
	def get_IsConcurrentLimit(self): # Boolean
		return self.get_body_params().get('IsConcurrentLimit')

	def set_IsConcurrentLimit(self, IsConcurrentLimit):  # Boolean
		self.add_body_params('IsConcurrentLimit', IsConcurrentLimit)
