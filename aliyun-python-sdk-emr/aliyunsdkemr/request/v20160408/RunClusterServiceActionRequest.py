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

class RunClusterServiceActionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'RunClusterServiceAction','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_HostGroupIdLists(self):
		return self.get_query_params().get('HostGroupIdLists')

	def set_HostGroupIdLists(self, HostGroupIdLists):
		for depth1 in range(len(HostGroupIdLists)):
			if HostGroupIdLists[depth1] is not None:
				self.add_query_param('HostGroupIdList.' + str(depth1 + 1) , HostGroupIdLists[depth1])

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ServiceActionName(self):
		return self.get_query_params().get('ServiceActionName')

	def set_ServiceActionName(self,ServiceActionName):
		self.add_query_param('ServiceActionName',ServiceActionName)

	def get_IsRolling(self):
		return self.get_query_params().get('IsRolling')

	def set_IsRolling(self,IsRolling):
		self.add_query_param('IsRolling',IsRolling)

	def get_TotlerateFailCount(self):
		return self.get_query_params().get('TotlerateFailCount')

	def set_TotlerateFailCount(self,TotlerateFailCount):
		self.add_query_param('TotlerateFailCount',TotlerateFailCount)

	def get_ServiceName(self):
		return self.get_query_params().get('ServiceName')

	def set_ServiceName(self,ServiceName):
		self.add_query_param('ServiceName',ServiceName)

	def get_ExecuteStrategy(self):
		return self.get_query_params().get('ExecuteStrategy')

	def set_ExecuteStrategy(self,ExecuteStrategy):
		self.add_query_param('ExecuteStrategy',ExecuteStrategy)

	def get_OnlyRestartStaleConfigNodes(self):
		return self.get_query_params().get('OnlyRestartStaleConfigNodes')

	def set_OnlyRestartStaleConfigNodes(self,OnlyRestartStaleConfigNodes):
		self.add_query_param('OnlyRestartStaleConfigNodes',OnlyRestartStaleConfigNodes)

	def get_NodeCountPerBatch(self):
		return self.get_query_params().get('NodeCountPerBatch')

	def set_NodeCountPerBatch(self,NodeCountPerBatch):
		self.add_query_param('NodeCountPerBatch',NodeCountPerBatch)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_CustomCommand(self):
		return self.get_query_params().get('CustomCommand')

	def set_CustomCommand(self,CustomCommand):
		self.add_query_param('CustomCommand',CustomCommand)

	def get_ComponentNameList(self):
		return self.get_query_params().get('ComponentNameList')

	def set_ComponentNameList(self,ComponentNameList):
		self.add_query_param('ComponentNameList',ComponentNameList)

	def get_Comment(self):
		return self.get_query_params().get('Comment')

	def set_Comment(self,Comment):
		self.add_query_param('Comment',Comment)

	def get_CustomParams(self):
		return self.get_query_params().get('CustomParams')

	def set_CustomParams(self,CustomParams):
		self.add_query_param('CustomParams',CustomParams)

	def get_Interval(self):
		return self.get_query_params().get('Interval')

	def set_Interval(self,Interval):
		self.add_query_param('Interval',Interval)

	def get_HostIdList(self):
		return self.get_query_params().get('HostIdList')

	def set_HostIdList(self,HostIdList):
		self.add_query_param('HostIdList',HostIdList)

	def get_TurnOnMaintenanceMode(self):
		return self.get_query_params().get('TurnOnMaintenanceMode')

	def set_TurnOnMaintenanceMode(self,TurnOnMaintenanceMode):
		self.add_query_param('TurnOnMaintenanceMode',TurnOnMaintenanceMode)