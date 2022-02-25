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
from aliyunsdkdas.endpoint import endpoint_data

class GetFullRequestStatResultByInstanceIdRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DAS', '2020-01-16', 'GetFullRequestStatResultByInstanceId')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_UserId(self): # String
		return self.get_query_params().get('UserId')

	def set_UserId(self, UserId):  # String
		self.add_query_param('UserId', UserId)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_NodeId(self): # String
		return self.get_query_params().get('NodeId')

	def set_NodeId(self, NodeId):  # String
		self.add_query_param('NodeId', NodeId)
	def get_SqlId(self): # String
		return self.get_query_params().get('SqlId')

	def set_SqlId(self, SqlId):  # String
		self.add_query_param('SqlId', SqlId)
	def get_OriginHost(self): # String
		return self.get_query_params().get('OriginHost')

	def set_OriginHost(self, OriginHost):  # String
		self.add_query_param('OriginHost', OriginHost)
	def get_Keyword(self): # String
		return self.get_query_params().get('Keyword')

	def set_Keyword(self, Keyword):  # String
		self.add_query_param('Keyword', Keyword)
	def get_Start(self): # Long
		return self.get_query_params().get('Start')

	def set_Start(self, Start):  # Long
		self.add_query_param('Start', Start)
	def get_End(self): # Long
		return self.get_query_params().get('End')

	def set_End(self, End):  # Long
		self.add_query_param('End', End)
	def get_OrderBy(self): # String
		return self.get_query_params().get('OrderBy')

	def set_OrderBy(self, OrderBy):  # String
		self.add_query_param('OrderBy', OrderBy)
	def get_Asc(self): # Boolean
		return self.get_query_params().get('Asc')

	def set_Asc(self, Asc):  # Boolean
		self.add_query_param('Asc', Asc)
	def get_PageNo(self): # Integer
		return self.get_query_params().get('PageNo')

	def set_PageNo(self, PageNo):  # Integer
		self.add_query_param('PageNo', PageNo)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_SqlType(self): # String
		return self.get_query_params().get('SqlType')

	def set_SqlType(self, SqlType):  # String
		self.add_query_param('SqlType', SqlType)
	def get_DbName(self): # String
		return self.get_query_params().get('DbName')

	def set_DbName(self, DbName):  # String
		self.add_query_param('DbName', DbName)
	def get_Role(self): # String
		return self.get_query_params().get('Role')

	def set_Role(self, Role):  # String
		self.add_query_param('Role', Role)
