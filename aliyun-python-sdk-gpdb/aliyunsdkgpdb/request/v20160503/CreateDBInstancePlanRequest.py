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
from aliyunsdkgpdb.endpoint import endpoint_data

class CreateDBInstancePlanRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'gpdb', '2016-05-03', 'CreateDBInstancePlan')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PlanType(self): # String
		return self.get_query_params().get('PlanType')

	def set_PlanType(self, PlanType):  # String
		self.add_query_param('PlanType', PlanType)
	def get_PlanStartDate(self): # String
		return self.get_query_params().get('PlanStartDate')

	def set_PlanStartDate(self, PlanStartDate):  # String
		self.add_query_param('PlanStartDate', PlanStartDate)
	def get_PlanConfig(self): # String
		return self.get_query_params().get('PlanConfig')

	def set_PlanConfig(self, PlanConfig):  # String
		self.add_query_param('PlanConfig', PlanConfig)
	def get_PlanName(self): # String
		return self.get_query_params().get('PlanName')

	def set_PlanName(self, PlanName):  # String
		self.add_query_param('PlanName', PlanName)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_PlanDesc(self): # String
		return self.get_query_params().get('PlanDesc')

	def set_PlanDesc(self, PlanDesc):  # String
		self.add_query_param('PlanDesc', PlanDesc)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_PlanEndDate(self): # String
		return self.get_query_params().get('PlanEndDate')

	def set_PlanEndDate(self, PlanEndDate):  # String
		self.add_query_param('PlanEndDate', PlanEndDate)
	def get_PlanScheduleType(self): # String
		return self.get_query_params().get('PlanScheduleType')

	def set_PlanScheduleType(self, PlanScheduleType):  # String
		self.add_query_param('PlanScheduleType', PlanScheduleType)
