# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class ListExecutionPlansRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'ListExecutionPlans')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_JobId(self):
		return self.get_query_params().get('JobId')

	def set_JobId(self,JobId):
		self.add_query_param('JobId',JobId)

	def get_Strategy(self):
		return self.get_query_params().get('Strategy')

	def set_Strategy(self,Strategy):
		self.add_query_param('Strategy',Strategy)

	def get_StatusLists(self):
		return self.get_query_params().get('StatusLists')

	def set_StatusLists(self,StatusLists):
		for i in range(len(StatusLists)):	
			self.add_query_param('StatusList.' + str(i + 1) , StatusLists[i]);

	def get_IsDesc(self):
		return self.get_query_params().get('IsDesc')

	def set_IsDesc(self,IsDesc):
		self.add_query_param('IsDesc',IsDesc)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_QueryType(self):
		return self.get_query_params().get('QueryType')

	def set_QueryType(self,QueryType):
		self.add_query_param('QueryType',QueryType)

	def get_QueryString(self):
		return self.get_query_params().get('QueryString')

	def set_QueryString(self,QueryString):
		self.add_query_param('QueryString',QueryString)