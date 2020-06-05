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

class SearchLogRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'SearchLog','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Line(self):
		return self.get_query_params().get('Line')

	def set_Line(self,Line):
		self.add_query_param('Line',Line)

	def get_HostName(self):
		return self.get_query_params().get('HostName')

	def set_HostName(self,HostName):
		self.add_query_param('HostName',HostName)

	def get_LogstoreName(self):
		return self.get_query_params().get('LogstoreName')

	def set_LogstoreName(self,LogstoreName):
		self.add_query_param('LogstoreName',LogstoreName)

	def get_FromTimestamp(self):
		return self.get_query_params().get('FromTimestamp')

	def set_FromTimestamp(self,FromTimestamp):
		self.add_query_param('FromTimestamp',FromTimestamp)

	def get_Offset(self):
		return self.get_query_params().get('Offset')

	def set_Offset(self,Offset):
		self.add_query_param('Offset',Offset)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_Reverse(self):
		return self.get_query_params().get('Reverse')

	def set_Reverse(self,Reverse):
		self.add_query_param('Reverse',Reverse)

	def get_HostInnerIp(self):
		return self.get_query_params().get('HostInnerIp')

	def set_HostInnerIp(self,HostInnerIp):
		self.add_query_param('HostInnerIp',HostInnerIp)

	def get_ToTimestamp(self):
		return self.get_query_params().get('ToTimestamp')

	def set_ToTimestamp(self,ToTimestamp):
		self.add_query_param('ToTimestamp',ToTimestamp)

	def get_SlsQueryString(self):
		return self.get_query_params().get('SlsQueryString')

	def set_SlsQueryString(self,SlsQueryString):
		self.add_query_param('SlsQueryString',SlsQueryString)