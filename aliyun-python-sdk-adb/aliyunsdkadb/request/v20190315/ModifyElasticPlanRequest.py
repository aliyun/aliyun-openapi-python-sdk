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
from aliyunsdkadb.endpoint import endpoint_data

class ModifyElasticPlanRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'adb', '2019-03-15', 'ModifyElasticPlan','ads')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ElasticPlanType(self): # String
		return self.get_query_params().get('ElasticPlanType')

	def set_ElasticPlanType(self, ElasticPlanType):  # String
		self.add_query_param('ElasticPlanType', ElasticPlanType)
	def get_ElasticPlanTimeStart(self): # String
		return self.get_query_params().get('ElasticPlanTimeStart')

	def set_ElasticPlanTimeStart(self, ElasticPlanTimeStart):  # String
		self.add_query_param('ElasticPlanTimeStart', ElasticPlanTimeStart)
	def get_ElasticPlanEndDay(self): # String
		return self.get_query_params().get('ElasticPlanEndDay')

	def set_ElasticPlanEndDay(self, ElasticPlanEndDay):  # String
		self.add_query_param('ElasticPlanEndDay', ElasticPlanEndDay)
	def get_ElasticPlanWeeklyRepeat(self): # String
		return self.get_query_params().get('ElasticPlanWeeklyRepeat')

	def set_ElasticPlanWeeklyRepeat(self, ElasticPlanWeeklyRepeat):  # String
		self.add_query_param('ElasticPlanWeeklyRepeat', ElasticPlanWeeklyRepeat)
	def get_ElasticPlanWorkerSpec(self): # String
		return self.get_query_params().get('ElasticPlanWorkerSpec')

	def set_ElasticPlanWorkerSpec(self, ElasticPlanWorkerSpec):  # String
		self.add_query_param('ElasticPlanWorkerSpec', ElasticPlanWorkerSpec)
	def get_ElasticPlanEnable(self): # Boolean
		return self.get_query_params().get('ElasticPlanEnable')

	def set_ElasticPlanEnable(self, ElasticPlanEnable):  # Boolean
		self.add_query_param('ElasticPlanEnable', ElasticPlanEnable)
	def get_ElasticPlanTimeEnd(self): # String
		return self.get_query_params().get('ElasticPlanTimeEnd')

	def set_ElasticPlanTimeEnd(self, ElasticPlanTimeEnd):  # String
		self.add_query_param('ElasticPlanTimeEnd', ElasticPlanTimeEnd)
	def get_ElasticPlanStartDay(self): # String
		return self.get_query_params().get('ElasticPlanStartDay')

	def set_ElasticPlanStartDay(self, ElasticPlanStartDay):  # String
		self.add_query_param('ElasticPlanStartDay', ElasticPlanStartDay)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_DBClusterId(self): # String
		return self.get_query_params().get('DBClusterId')

	def set_DBClusterId(self, DBClusterId):  # String
		self.add_query_param('DBClusterId', DBClusterId)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ElasticPlanName(self): # String
		return self.get_query_params().get('ElasticPlanName')

	def set_ElasticPlanName(self, ElasticPlanName):  # String
		self.add_query_param('ElasticPlanName', ElasticPlanName)
	def get_ResourcePoolName(self): # String
		return self.get_query_params().get('ResourcePoolName')

	def set_ResourcePoolName(self, ResourcePoolName):  # String
		self.add_query_param('ResourcePoolName', ResourcePoolName)
	def get_ElasticPlanNodeNum(self): # Integer
		return self.get_query_params().get('ElasticPlanNodeNum')

	def set_ElasticPlanNodeNum(self, ElasticPlanNodeNum):  # Integer
		self.add_query_param('ElasticPlanNodeNum', ElasticPlanNodeNum)
