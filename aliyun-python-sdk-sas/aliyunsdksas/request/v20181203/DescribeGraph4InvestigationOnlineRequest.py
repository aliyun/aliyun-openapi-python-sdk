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
from aliyunsdksas.endpoint import endpoint_data

class DescribeGraph4InvestigationOnlineRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'DescribeGraph4InvestigationOnline','sas')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_VertexId(self):
		return self.get_query_params().get('VertexId')

	def set_VertexId(self,VertexId):
		self.add_query_param('VertexId',VertexId)

	def get_AnomalyId(self):
		return self.get_query_params().get('AnomalyId')

	def set_AnomalyId(self,AnomalyId):
		self.add_query_param('AnomalyId',AnomalyId)

	def get_AnomalyUuid(self):
		return self.get_query_params().get('AnomalyUuid')

	def set_AnomalyUuid(self,AnomalyUuid):
		self.add_query_param('AnomalyUuid',AnomalyUuid)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_Direction(self):
		return self.get_query_params().get('Direction')

	def set_Direction(self,Direction):
		self.add_query_param('Direction',Direction)

	def get_PathLength(self):
		return self.get_query_params().get('PathLength')

	def set_PathLength(self,PathLength):
		self.add_query_param('PathLength',PathLength)

	def get_Namespace(self):
		return self.get_query_params().get('Namespace')

	def set_Namespace(self,Namespace):
		self.add_query_param('Namespace',Namespace)