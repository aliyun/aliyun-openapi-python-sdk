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
from aliyunsdkemr.endpoint import endpoint_data

class ModifyUserStatisticsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'ModifyUserStatistics','emr')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_JobMigratedNum(self):
		return self.get_query_params().get('JobMigratedNum')

	def set_JobMigratedNum(self,JobMigratedNum):
		self.add_query_param('JobMigratedNum',JobMigratedNum)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ExecutePlanNum(self):
		return self.get_query_params().get('ExecutePlanNum')

	def set_ExecutePlanNum(self,ExecutePlanNum):
		self.add_query_param('ExecutePlanNum',ExecutePlanNum)

	def get_JobNum(self):
		return self.get_query_params().get('JobNum')

	def set_JobNum(self,JobNum):
		self.add_query_param('JobNum',JobNum)

	def get_ExecutePlanMigratedNum(self):
		return self.get_query_params().get('ExecutePlanMigratedNum')

	def set_ExecutePlanMigratedNum(self,ExecutePlanMigratedNum):
		self.add_query_param('ExecutePlanMigratedNum',ExecutePlanMigratedNum)

	def get_InteractionJobMigratedNum(self):
		return self.get_query_params().get('InteractionJobMigratedNum')

	def set_InteractionJobMigratedNum(self,InteractionJobMigratedNum):
		self.add_query_param('InteractionJobMigratedNum',InteractionJobMigratedNum)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)

	def get_InteractionJobNum(self):
		return self.get_query_params().get('InteractionJobNum')

	def set_InteractionJobNum(self,InteractionJobNum):
		self.add_query_param('InteractionJobNum',InteractionJobNum)