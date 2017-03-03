# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class QueryPriceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'QueryPrice')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_MasterInstanceType(self):
		return self.get_query_params().get('MasterInstanceType')

	def set_MasterInstanceType(self,MasterInstanceType):
		self.add_query_param('MasterInstanceType',MasterInstanceType)

	def get_CoreInstanceType(self):
		return self.get_query_params().get('CoreInstanceType')

	def set_CoreInstanceType(self,CoreInstanceType):
		self.add_query_param('CoreInstanceType',CoreInstanceType)

	def get_TaskInstanceType(self):
		return self.get_query_params().get('TaskInstanceType')

	def set_TaskInstanceType(self,TaskInstanceType):
		self.add_query_param('TaskInstanceType',TaskInstanceType)

	def get_MasterInstanceQuantity(self):
		return self.get_query_params().get('MasterInstanceQuantity')

	def set_MasterInstanceQuantity(self,MasterInstanceQuantity):
		self.add_query_param('MasterInstanceQuantity',MasterInstanceQuantity)

	def get_CoreInstanceQuantity(self):
		return self.get_query_params().get('CoreInstanceQuantity')

	def set_CoreInstanceQuantity(self,CoreInstanceQuantity):
		self.add_query_param('CoreInstanceQuantity',CoreInstanceQuantity)

	def get_TaskInstanceQuantity(self):
		return self.get_query_params().get('TaskInstanceQuantity')

	def set_TaskInstanceQuantity(self,TaskInstanceQuantity):
		self.add_query_param('TaskInstanceQuantity',TaskInstanceQuantity)

	def get_MasterDiskType(self):
		return self.get_query_params().get('MasterDiskType')

	def set_MasterDiskType(self,MasterDiskType):
		self.add_query_param('MasterDiskType',MasterDiskType)

	def get_CoreDiskType(self):
		return self.get_query_params().get('CoreDiskType')

	def set_CoreDiskType(self,CoreDiskType):
		self.add_query_param('CoreDiskType',CoreDiskType)

	def get_TaskDiskType(self):
		return self.get_query_params().get('TaskDiskType')

	def set_TaskDiskType(self,TaskDiskType):
		self.add_query_param('TaskDiskType',TaskDiskType)

	def get_MasterDiskQuantity(self):
		return self.get_query_params().get('MasterDiskQuantity')

	def set_MasterDiskQuantity(self,MasterDiskQuantity):
		self.add_query_param('MasterDiskQuantity',MasterDiskQuantity)

	def get_CoreDiskQuantity(self):
		return self.get_query_params().get('CoreDiskQuantity')

	def set_CoreDiskQuantity(self,CoreDiskQuantity):
		self.add_query_param('CoreDiskQuantity',CoreDiskQuantity)

	def get_TaskDiskQuantity(self):
		return self.get_query_params().get('TaskDiskQuantity')

	def set_TaskDiskQuantity(self,TaskDiskQuantity):
		self.add_query_param('TaskDiskQuantity',TaskDiskQuantity)

	def get_Duration(self):
		return self.get_query_params().get('Duration')

	def set_Duration(self,Duration):
		self.add_query_param('Duration',Duration)

	def get_IoOptimized(self):
		return self.get_query_params().get('IoOptimized')

	def set_IoOptimized(self,IoOptimized):
		self.add_query_param('IoOptimized',IoOptimized)

	def get_ChargeType(self):
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self,ChargeType):
		self.add_query_param('ChargeType',ChargeType)

	def get_NetType(self):
		return self.get_query_params().get('NetType')

	def set_NetType(self,NetType):
		self.add_query_param('NetType',NetType)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)