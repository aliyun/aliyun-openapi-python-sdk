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

class ListApplicationConfigsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2021-03-20', 'ListApplicationConfigs','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ConfigVersion(self):
		return self.get_query_params().get('ConfigVersion')

	def set_ConfigVersion(self,ConfigVersion):
		self.add_query_param('ConfigVersion',ConfigVersion)

	def get_NextToken(self):
		return self.get_query_params().get('NextToken')

	def set_NextToken(self,NextToken):
		self.add_query_param('NextToken',NextToken)

	def get_NodeId(self):
		return self.get_query_params().get('NodeId')

	def set_NodeId(self,NodeId):
		self.add_query_param('NodeId',NodeId)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_ConfigFileName(self):
		return self.get_query_params().get('ConfigFileName')

	def set_ConfigFileName(self,ConfigFileName):
		self.add_query_param('ConfigFileName',ConfigFileName)

	def get_ConfigItemKey(self):
		return self.get_query_params().get('ConfigItemKey')

	def set_ConfigItemKey(self,ConfigItemKey):
		self.add_query_param('ConfigItemKey',ConfigItemKey)

	def get_ApplicationName(self):
		return self.get_query_params().get('ApplicationName')

	def set_ApplicationName(self,ApplicationName):
		self.add_query_param('ApplicationName',ApplicationName)

	def get_Labels(self):
		return self.get_query_params().get('Labels')

	def set_Labels(self,Labels):
		self.add_query_param('Labels',Labels)

	def get_NodeGroupId(self):
		return self.get_query_params().get('NodeGroupId')

	def set_NodeGroupId(self,NodeGroupId):
		self.add_query_param('NodeGroupId',NodeGroupId)

	def get_MaxResults(self):
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self,MaxResults):
		self.add_query_param('MaxResults',MaxResults)