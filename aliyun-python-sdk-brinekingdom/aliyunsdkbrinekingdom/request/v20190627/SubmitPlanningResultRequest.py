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
		RpcRequest.__init__(self, 'brinekingdom', '2019-06-27', 'SubmitPlanningResult','python')
		self.set_protocol_type('https')
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
		return self.get_query_params().get('ResourceMethods')

	def set_ResourceMethods(self,ResourceMethods):
		for i in range(len(ResourceMethods)):	
			if ResourceMethods[i].get('FinalAvzone') is not None:
				self.add_query_param('ResourceMethod.' + str(i + 1) + '.FinalAvzone' , ResourceMethods[i].get('FinalAvzone'))
			if ResourceMethods[i].get('Cluster') is not None:
				self.add_query_param('ResourceMethod.' + str(i + 1) + '.Cluster' , ResourceMethods[i].get('Cluster'))
			if ResourceMethods[i].get('ConvertHostCnt') is not None:
				self.add_query_param('ResourceMethod.' + str(i + 1) + '.ConvertHostCnt' , ResourceMethods[i].get('ConvertHostCnt'))
			if ResourceMethods[i].get('BufferCnt') is not None:
				self.add_query_param('ResourceMethod.' + str(i + 1) + '.BufferCnt' , ResourceMethods[i].get('BufferCnt'))
			for j in range(len(ResourceMethods[i].get('SupplyPlans'))):
				if ResourceMethods[i].get('SupplyPlans')[j] is not None:
					if ResourceMethods[i].get('SupplyPlans')[j].get('SafeZone') is not None:
						self.add_query_param('ResourceMethod.' + str(i + 1) + '.SupplyPlan.'+str(j + 1)+ '.SafeZone', ResourceMethods[i].get('SupplyPlans')[j].get('SafeZone'))
					if ResourceMethods[i].get('SupplyPlans')[j].get('NetArch') is not None:
						self.add_query_param('ResourceMethod.' + str(i + 1) + '.SupplyPlan.'+str(j + 1)+ '.NetArch', ResourceMethods[i].get('SupplyPlans')[j].get('NetArch'))
					if ResourceMethods[i].get('SupplyPlans')[j].get('SupplyType') is not None:
						self.add_query_param('ResourceMethod.' + str(i + 1) + '.SupplyPlan.'+str(j + 1)+ '.SupplyType', ResourceMethods[i].get('SupplyPlans')[j].get('SupplyType'))
					if ResourceMethods[i].get('SupplyPlans')[j].get('LogicZone') is not None:
						self.add_query_param('ResourceMethod.' + str(i + 1) + '.SupplyPlan.'+str(j + 1)+ '.LogicZone', ResourceMethods[i].get('SupplyPlans')[j].get('LogicZone'))
					if ResourceMethods[i].get('SupplyPlans')[j].get('SupplyAmount') is not None:
						self.add_query_param('ResourceMethod.' + str(i + 1) + '.SupplyPlan.'+str(j + 1)+ '.SupplyAmount', ResourceMethods[i].get('SupplyPlans')[j].get('SupplyAmount'))
					if ResourceMethods[i].get('SupplyPlans')[j].get('SupplyDate') is not None:
						self.add_query_param('ResourceMethod.' + str(i + 1) + '.SupplyPlan.'+str(j + 1)+ '.SupplyDate', ResourceMethods[i].get('SupplyPlans')[j].get('SupplyDate'))
					if ResourceMethods[i].get('SupplyPlans')[j].get('Nic') is not None:
						self.add_query_param('ResourceMethod.' + str(i + 1) + '.SupplyPlan.'+str(j + 1)+ '.Nic', ResourceMethods[i].get('SupplyPlans')[j].get('Nic'))
					if ResourceMethods[i].get('SupplyPlans')[j].get('ClassZone') is not None:
						self.add_query_param('ResourceMethod.' + str(i + 1) + '.SupplyPlan.'+str(j + 1)+ '.ClassZone', ResourceMethods[i].get('SupplyPlans')[j].get('ClassZone'))
					if ResourceMethods[i].get('SupplyPlans')[j].get('ConvertHostType') is not None:
						self.add_query_param('ResourceMethod.' + str(i + 1) + '.SupplyPlan.'+str(j + 1)+ '.ConvertHostType', ResourceMethods[i].get('SupplyPlans')[j].get('ConvertHostType'))
					if ResourceMethods[i].get('SupplyPlans')[j].get('Product3') is not None:
						self.add_query_param('ResourceMethod.' + str(i + 1) + '.SupplyPlan.'+str(j + 1)+ '.Product3', ResourceMethods[i].get('SupplyPlans')[j].get('Product3'))
			if ResourceMethods[i].get('RoomCode') is not None:
				self.add_query_param('ResourceMethod.' + str(i + 1) + '.RoomCode' , ResourceMethods[i].get('RoomCode'))
			if ResourceMethods[i].get('Comment') is not None:
				self.add_query_param('ResourceMethod.' + str(i + 1) + '.Comment' , ResourceMethods[i].get('Comment'))
			if ResourceMethods[i].get('Region') is not None:
				self.add_query_param('ResourceMethod.' + str(i + 1) + '.Region' , ResourceMethods[i].get('Region'))
			if ResourceMethods[i].get('ConvertHostType') is not None:
				self.add_query_param('ResourceMethod.' + str(i + 1) + '.ConvertHostType' , ResourceMethods[i].get('ConvertHostType'))
			if ResourceMethods[i].get('Azone') is not None:
				self.add_query_param('ResourceMethod.' + str(i + 1) + '.Azone' , ResourceMethods[i].get('Azone'))
			if ResourceMethods[i].get('GapCnt') is not None:
				self.add_query_param('ResourceMethod.' + str(i + 1) + '.GapCnt' , ResourceMethods[i].get('GapCnt'))
