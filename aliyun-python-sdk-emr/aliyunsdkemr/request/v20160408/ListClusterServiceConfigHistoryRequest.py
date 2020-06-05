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

class ListClusterServiceConfigHistoryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'ListClusterServiceConfigHistory','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_HostInstanceId(self):
		return self.get_query_params().get('HostInstanceId')

	def set_HostInstanceId(self,HostInstanceId):
		self.add_query_param('HostInstanceId',HostInstanceId)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_ConfigVersion(self):
		return self.get_query_params().get('ConfigVersion')

	def set_ConfigVersion(self,ConfigVersion):
		self.add_query_param('ConfigVersion',ConfigVersion)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_ServiceName(self):
		return self.get_query_params().get('ServiceName')

	def set_ServiceName(self,ServiceName):
		self.add_query_param('ServiceName',ServiceName)

	def get_Author(self):
		return self.get_query_params().get('Author')

	def set_Author(self,Author):
		self.add_query_param('Author',Author)

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

	def get_HostGroupId(self):
		return self.get_query_params().get('HostGroupId')

	def set_HostGroupId(self,HostGroupId):
		self.add_query_param('HostGroupId',HostGroupId)

	def get_Comment(self):
		return self.get_query_params().get('Comment')

	def set_Comment(self,Comment):
		self.add_query_param('Comment',Comment)