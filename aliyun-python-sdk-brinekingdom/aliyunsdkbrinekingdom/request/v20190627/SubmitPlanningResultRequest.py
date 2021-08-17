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
from aliyunsdkbrinekingdom.endpoint import endpoint_data

class SubmitPlanningResultRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'brinekingdom', '2019-06-27', 'SubmitPlanningResult')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_RequireCnt(self):
		return self.get_query_params().get('RequireCnt')

	def set_RequireCnt(self,RequireCnt):
		self.add_query_param('RequireCnt',RequireCnt)

	def get_DemandId(self):
		return self.get_query_params().get('DemandId')

	def set_DemandId(self,DemandId):
		self.add_query_param('DemandId',DemandId)

	def get_SubDemandId(self):
		return self.get_query_params().get('SubDemandId')

	def set_SubDemandId(self,SubDemandId):
		self.add_query_param('SubDemandId',SubDemandId)

	def get_BufferCnt(self):
		return self.get_query_params().get('BufferCnt')

	def set_BufferCnt(self,BufferCnt):
		self.add_query_param('BufferCnt',BufferCnt)

	def get_DemandCount(self):
		return self.get_query_params().get('DemandCount')

	def set_DemandCount(self,DemandCount):
		self.add_query_param('DemandCount',DemandCount)

	def get_ResourceMethods(self):
		return self.get_query_params().get('ResourceMethod')

	def set_ResourceMethods(self, ResourceMethods):
		for depth1 in range(len(ResourceMethods)):
			if ResourceMethods[depth1].get('FinalAvzone') is not None:
				self.add_query_param('ResourceMethod.' + str(depth1 + 1) + '.FinalAvzone', ResourceMethods[depth1].get('FinalAvzone'))
			if ResourceMethods[depth1].get('Cluster') is not None:
				self.add_query_param('ResourceMethod.' + str(depth1 + 1) + '.Cluster', ResourceMethods[depth1].get('Cluster'))
			if ResourceMethods[depth1].get('ConvertHostCnt') is not None:
				self.add_query_param('ResourceMethod.' + str(depth1 + 1) + '.ConvertHostCnt', ResourceMethods[depth1].get('ConvertHostCnt'))
			if ResourceMethods[depth1].get('BufferCnt') is not None:
				self.add_query_param('ResourceMethod.' + str(depth1 + 1) + '.BufferCnt', ResourceMethods[depth1].get('BufferCnt'))
			if ResourceMethods[depth1].get('SupplyPlan') is not None:
				for depth2 in range(len(ResourceMethods[depth1].get('SupplyPlan'))):
					if ResourceMethods[depth1].get('SupplyPlan')[depth2].get('SafeZone') is not None:
						self.add_query_param('ResourceMethod.' + str(depth1 + 1) + '.SupplyPlan.' + str(depth2 + 1) + '.SafeZone', ResourceMethods[depth1].get('SupplyPlan')[depth2].get('SafeZone'))
					if ResourceMethods[depth1].get('SupplyPlan')[depth2].get('NetArch') is not None:
						self.add_query_param('ResourceMethod.' + str(depth1 + 1) + '.SupplyPlan.' + str(depth2 + 1) + '.NetArch', ResourceMethods[depth1].get('SupplyPlan')[depth2].get('NetArch'))
					if ResourceMethods[depth1].get('SupplyPlan')[depth2].get('SupplyType') is not None:
						self.add_query_param('ResourceMethod.' + str(depth1 + 1) + '.SupplyPlan.' + str(depth2 + 1) + '.SupplyType', ResourceMethods[depth1].get('SupplyPlan')[depth2].get('SupplyType'))
					if ResourceMethods[depth1].get('SupplyPlan')[depth2].get('LogicZone') is not None:
						self.add_query_param('ResourceMethod.' + str(depth1 + 1) + '.SupplyPlan.' + str(depth2 + 1) + '.LogicZone', ResourceMethods[depth1].get('SupplyPlan')[depth2].get('LogicZone'))
					if ResourceMethods[depth1].get('SupplyPlan')[depth2].get('SupplyAmount') is not None:
						self.add_query_param('ResourceMethod.' + str(depth1 + 1) + '.SupplyPlan.' + str(depth2 + 1) + '.SupplyAmount', ResourceMethods[depth1].get('SupplyPlan')[depth2].get('SupplyAmount'))
					if ResourceMethods[depth1].get('SupplyPlan')[depth2].get('SupplyDate') is not None:
						self.add_query_param('ResourceMethod.' + str(depth1 + 1) + '.SupplyPlan.' + str(depth2 + 1) + '.SupplyDate', ResourceMethods[depth1].get('SupplyPlan')[depth2].get('SupplyDate'))
					if ResourceMethods[depth1].get('SupplyPlan')[depth2].get('Nic') is not None:
						self.add_query_param('ResourceMethod.' + str(depth1 + 1) + '.SupplyPlan.' + str(depth2 + 1) + '.Nic', ResourceMethods[depth1].get('SupplyPlan')[depth2].get('Nic'))
					if ResourceMethods[depth1].get('SupplyPlan')[depth2].get('ClassZone') is not None:
						self.add_query_param('ResourceMethod.' + str(depth1 + 1) + '.SupplyPlan.' + str(depth2 + 1) + '.ClassZone', ResourceMethods[depth1].get('SupplyPlan')[depth2].get('ClassZone'))
					if ResourceMethods[depth1].get('SupplyPlan')[depth2].get('ConvertHostType') is not None:
						self.add_query_param('ResourceMethod.' + str(depth1 + 1) + '.SupplyPlan.' + str(depth2 + 1) + '.ConvertHostType', ResourceMethods[depth1].get('SupplyPlan')[depth2].get('ConvertHostType'))
					if ResourceMethods[depth1].get('SupplyPlan')[depth2].get('Product3') is not None:
						self.add_query_param('ResourceMethod.' + str(depth1 + 1) + '.SupplyPlan.' + str(depth2 + 1) + '.Product3', ResourceMethods[depth1].get('SupplyPlan')[depth2].get('Product3'))
			if ResourceMethods[depth1].get('RoomCode') is not None:
				self.add_query_param('ResourceMethod.' + str(depth1 + 1) + '.RoomCode', ResourceMethods[depth1].get('RoomCode'))
			if ResourceMethods[depth1].get('Comment') is not None:
				self.add_query_param('ResourceMethod.' + str(depth1 + 1) + '.Comment', ResourceMethods[depth1].get('Comment'))
			if ResourceMethods[depth1].get('Region') is not None:
				self.add_query_param('ResourceMethod.' + str(depth1 + 1) + '.Region', ResourceMethods[depth1].get('Region'))
			if ResourceMethods[depth1].get('ConvertHostType') is not None:
				self.add_query_param('ResourceMethod.' + str(depth1 + 1) + '.ConvertHostType', ResourceMethods[depth1].get('ConvertHostType'))
			if ResourceMethods[depth1].get('Azone') is not None:
				self.add_query_param('ResourceMethod.' + str(depth1 + 1) + '.Azone', ResourceMethods[depth1].get('Azone'))
			if ResourceMethods[depth1].get('GapCnt') is not None:
				self.add_query_param('ResourceMethod.' + str(depth1 + 1) + '.GapCnt', ResourceMethods[depth1].get('GapCnt'))