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

class QuerySqlAnalysisDataRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DAS', '2020-01-16', 'QuerySqlAnalysisData')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TaskId(self): # String
		return self.get_body_params().get('TaskId')

	def set_TaskId(self, TaskId):  # String
		self.add_body_params('TaskId', TaskId)
	def get_SqlIdList(self): # String
		return self.get_body_params().get('SqlIdList')

	def set_SqlIdList(self, SqlIdList):  # String
		self.add_body_params('SqlIdList', SqlIdList)
	def get_Type(self): # String
		return self.get_body_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_body_params('Type', Type)
	def get_SqlTextFeature(self): # String
		return self.get_body_params().get('SqlTextFeature')

	def set_SqlTextFeature(self, SqlTextFeature):  # String
		self.add_body_params('SqlTextFeature', SqlTextFeature)
	def get_SqlType(self): # String
		return self.get_body_params().get('SqlType')

	def set_SqlType(self, SqlType):  # String
		self.add_body_params('SqlType', SqlType)
	def get_PageNo(self): # Integer
		return self.get_body_params().get('PageNo')

	def set_PageNo(self, PageNo):  # Integer
		self.add_body_params('PageNo', PageNo)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
