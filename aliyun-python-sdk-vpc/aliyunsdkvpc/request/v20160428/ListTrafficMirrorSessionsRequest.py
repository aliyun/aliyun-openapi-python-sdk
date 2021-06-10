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
from aliyunsdkvpc.endpoint import endpoint_data

class ListTrafficMirrorSessionsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'ListTrafficMirrorSessions','vpc')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_TrafficMirrorSourceId(self):
		return self.get_query_params().get('TrafficMirrorSourceId')

	def set_TrafficMirrorSourceId(self,TrafficMirrorSourceId):
		self.add_query_param('TrafficMirrorSourceId',TrafficMirrorSourceId)

	def get_Enabled(self):
		return self.get_query_params().get('Enabled')

	def set_Enabled(self,Enabled):
		self.add_query_param('Enabled',Enabled)

	def get_TrafficMirrorSessionName(self):
		return self.get_query_params().get('TrafficMirrorSessionName')

	def set_TrafficMirrorSessionName(self,TrafficMirrorSessionName):
		self.add_query_param('TrafficMirrorSessionName',TrafficMirrorSessionName)

	def get_NextToken(self):
		return self.get_query_params().get('NextToken')

	def set_NextToken(self,NextToken):
		self.add_query_param('NextToken',NextToken)

	def get_TrafficMirrorSessionIdss(self):
		return self.get_query_params().get('TrafficMirrorSessionIds')

	def set_TrafficMirrorSessionIdss(self, TrafficMirrorSessionIdss):
		for depth1 in range(len(TrafficMirrorSessionIdss)):
			if TrafficMirrorSessionIdss[depth1] is not None:
				self.add_query_param('TrafficMirrorSessionIds.' + str(depth1 + 1) , TrafficMirrorSessionIdss[depth1])

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_Priority(self):
		return self.get_query_params().get('Priority')

	def set_Priority(self,Priority):
		self.add_query_param('Priority',Priority)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_TrafficMirrorTargetId(self):
		return self.get_query_params().get('TrafficMirrorTargetId')

	def set_TrafficMirrorTargetId(self,TrafficMirrorTargetId):
		self.add_query_param('TrafficMirrorTargetId',TrafficMirrorTargetId)

	def get_TrafficMirrorFilterId(self):
		return self.get_query_params().get('TrafficMirrorFilterId')

	def set_TrafficMirrorFilterId(self,TrafficMirrorFilterId):
		self.add_query_param('TrafficMirrorFilterId',TrafficMirrorFilterId)

	def get_MaxResults(self):
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self,MaxResults):
		self.add_query_param('MaxResults',MaxResults)

	def get_VirtualNetworkId(self):
		return self.get_query_params().get('VirtualNetworkId')

	def set_VirtualNetworkId(self,VirtualNetworkId):
		self.add_query_param('VirtualNetworkId',VirtualNetworkId)