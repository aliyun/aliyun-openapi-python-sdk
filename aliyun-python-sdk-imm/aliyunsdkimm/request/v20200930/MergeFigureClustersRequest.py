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
from aliyunsdkimm.endpoint import endpoint_data

class MergeFigureClustersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2020-09-30', 'MergeFigureClusters','imm')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CustomMessage(self): # String
		return self.get_query_params().get('CustomMessage')

	def set_CustomMessage(self, CustomMessage):  # String
		self.add_query_param('CustomMessage', CustomMessage)
	def get_ClusterIdFrom(self): # String
		return self.get_query_params().get('ClusterIdFrom')

	def set_ClusterIdFrom(self, ClusterIdFrom):  # String
		self.add_query_param('ClusterIdFrom', ClusterIdFrom)
	def get_ProjectName(self): # String
		return self.get_query_params().get('ProjectName')

	def set_ProjectName(self, ProjectName):  # String
		self.add_query_param('ProjectName', ProjectName)
	def get_NotifyTopicName(self): # String
		return self.get_query_params().get('NotifyTopicName')

	def set_NotifyTopicName(self, NotifyTopicName):  # String
		self.add_query_param('NotifyTopicName', NotifyTopicName)
	def get_DatasetName(self): # String
		return self.get_query_params().get('DatasetName')

	def set_DatasetName(self, DatasetName):  # String
		self.add_query_param('DatasetName', DatasetName)
	def get_FigureType(self): # String
		return self.get_query_params().get('FigureType')

	def set_FigureType(self, FigureType):  # String
		self.add_query_param('FigureType', FigureType)
	def get_ClusterIdTo(self): # String
		return self.get_query_params().get('ClusterIdTo')

	def set_ClusterIdTo(self, ClusterIdTo):  # String
		self.add_query_param('ClusterIdTo', ClusterIdTo)
	def get_NotifyTopicEndpoint(self): # String
		return self.get_query_params().get('NotifyTopicEndpoint')

	def set_NotifyTopicEndpoint(self, NotifyTopicEndpoint):  # String
		self.add_query_param('NotifyTopicEndpoint', NotifyTopicEndpoint)
