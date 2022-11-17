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
from aliyunsdkoceanbasepro.endpoint import endpoint_data
import json

class SearchOmsOpenAPIProjectsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OceanBasePro', '2019-09-01', 'SearchOmsOpenAPIProjects','oceanbase')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DestDbTypes(self): # Array
		return self.get_body_params().get('DestDbTypes')

	def set_DestDbTypes(self, DestDbTypes):  # Array
		self.add_body_params("DestDbTypes", json.dumps(DestDbTypes))
	def get_StatusList(self): # Array
		return self.get_body_params().get('StatusList')

	def set_StatusList(self, StatusList):  # Array
		self.add_body_params("StatusList", json.dumps(StatusList))
	def get_SearchKey(self): # String
		return self.get_body_params().get('SearchKey')

	def set_SearchKey(self, SearchKey):  # String
		self.add_body_params('SearchKey', SearchKey)
	def get_PageNumber(self): # Integer
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_body_params('PageNumber', PageNumber)
	def get_SourceDbTypes(self): # Array
		return self.get_body_params().get('SourceDbTypes')

	def set_SourceDbTypes(self, SourceDbTypes):  # Array
		self.add_body_params("SourceDbTypes", json.dumps(SourceDbTypes))
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_WorkerGradeId(self): # String
		return self.get_body_params().get('WorkerGradeId')

	def set_WorkerGradeId(self, WorkerGradeId):  # String
		self.add_body_params('WorkerGradeId', WorkerGradeId)
	def get_LabelIds(self): # Array
		return self.get_body_params().get('LabelIds')

	def set_LabelIds(self, LabelIds):  # Array
		self.add_body_params("LabelIds", json.dumps(LabelIds))
