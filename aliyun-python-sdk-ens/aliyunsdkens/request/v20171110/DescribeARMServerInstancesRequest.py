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
import json

class DescribeARMServerInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'DescribeARMServerInstances','ens')
		self.set_method('GET')

	def get_AICSpecs(self): # Array
		return self.get_query_params().get('AICSpecs')

	def set_AICSpecs(self, AICSpecs):  # Array
		self.add_query_param("AICSpecs", json.dumps(AICSpecs))
	def get_OrderByParams(self): # String
		return self.get_query_params().get('OrderByParams')

	def set_OrderByParams(self, OrderByParams):  # String
		self.add_query_param('OrderByParams', OrderByParams)
	def get_DescribeAICInstances(self): # Boolean
		return self.get_query_params().get('DescribeAICInstances')

	def set_DescribeAICInstances(self, DescribeAICInstances):  # Boolean
		self.add_query_param('DescribeAICInstances', DescribeAICInstances)
	def get_ServerIds(self): # Array
		return self.get_query_params().get('ServerIds')

	def set_ServerIds(self, ServerIds):  # Array
		self.add_query_param("ServerIds", json.dumps(ServerIds))
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_MaxDate(self): # String
		return self.get_query_params().get('MaxDate')

	def set_MaxDate(self, MaxDate):  # String
		self.add_query_param('MaxDate', MaxDate)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_States(self): # Array
		return self.get_query_params().get('States')

	def set_States(self, States):  # Array
		self.add_query_param("States", json.dumps(States))
	def get_ServerSpecs(self): # Array
		return self.get_query_params().get('ServerSpecs')

	def set_ServerSpecs(self, ServerSpecs):  # Array
		self.add_query_param("ServerSpecs", json.dumps(ServerSpecs))
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_EnsRegionIds(self): # Array
		return self.get_query_params().get('EnsRegionIds')

	def set_EnsRegionIds(self, EnsRegionIds):  # Array
		self.add_query_param("EnsRegionIds", json.dumps(EnsRegionIds))
	def get_MinDate(self): # String
		return self.get_query_params().get('MinDate')

	def set_MinDate(self, MinDate):  # String
		self.add_query_param('MinDate', MinDate)
	def get_Namespace(self): # String
		return self.get_query_params().get('Namespace')

	def set_Namespace(self, Namespace):  # String
		self.add_query_param('Namespace', Namespace)
