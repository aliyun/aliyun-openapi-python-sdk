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

class AddAssetSelectionCriteriaRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'AddAssetSelectionCriteria','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CriteriaOperation(self): # String
		return self.get_query_params().get('CriteriaOperation')

	def set_CriteriaOperation(self, CriteriaOperation):  # String
		self.add_query_param('CriteriaOperation', CriteriaOperation)
	def get_Criteria(self): # String
		return self.get_query_params().get('Criteria')

	def set_Criteria(self, Criteria):  # String
		self.add_query_param('Criteria', Criteria)
	def get_TargetOperationLists(self): # RepeatList
		return self.get_query_params().get('TargetOperationList')

	def set_TargetOperationLists(self, TargetOperationList):  # RepeatList
		for depth1 in range(len(TargetOperationList)):
			if TargetOperationList[depth1].get('Operation') is not None:
				self.add_query_param('TargetOperationList.' + str(depth1 + 1) + '.Operation', TargetOperationList[depth1].get('Operation'))
			if TargetOperationList[depth1].get('Target') is not None:
				self.add_query_param('TargetOperationList.' + str(depth1 + 1) + '.Target', TargetOperationList[depth1].get('Target'))
	def get_SelectionKey(self): # String
		return self.get_query_params().get('SelectionKey')

	def set_SelectionKey(self, SelectionKey):  # String
		self.add_query_param('SelectionKey', SelectionKey)
