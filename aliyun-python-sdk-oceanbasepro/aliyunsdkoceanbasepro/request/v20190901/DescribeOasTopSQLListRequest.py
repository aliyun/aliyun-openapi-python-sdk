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

class DescribeOasTopSQLListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OceanBasePro', '2019-09-01', 'DescribeOasTopSQLList','oceanbase')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_StartTime(self): # String
		return self.get_body_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_body_params('StartTime', StartTime)
	def get_SearchRule(self): # String
		return self.get_body_params().get('SearchRule')

	def set_SearchRule(self, SearchRule):  # String
		self.add_body_params('SearchRule', SearchRule)
	def get_MergeDynamicSql(self): # Boolean
		return self.get_body_params().get('MergeDynamicSql')

	def set_MergeDynamicSql(self, MergeDynamicSql):  # Boolean
		self.add_body_params('MergeDynamicSql', MergeDynamicSql)
	def get_DynamicSql(self): # Boolean
		return self.get_body_params().get('DynamicSql')

	def set_DynamicSql(self, DynamicSql):  # Boolean
		self.add_body_params('DynamicSql', DynamicSql)
	def get_SqlTextLength(self): # Long
		return self.get_body_params().get('SqlTextLength')

	def set_SqlTextLength(self, SqlTextLength):  # Long
		self.add_body_params('SqlTextLength', SqlTextLength)
	def get_TenantId(self): # String
		return self.get_body_params().get('TenantId')

	def set_TenantId(self, TenantId):  # String
		self.add_body_params('TenantId', TenantId)
	def get_SearchValue(self): # String
		return self.get_body_params().get('SearchValue')

	def set_SearchValue(self, SearchValue):  # String
		self.add_body_params('SearchValue', SearchValue)
	def get_SqlId(self): # String
		return self.get_body_params().get('SqlId')

	def set_SqlId(self, SqlId):  # String
		self.add_body_params('SqlId', SqlId)
	def get_FilterCondition(self): # String
		return self.get_body_params().get('FilterCondition')

	def set_FilterCondition(self, FilterCondition):  # String
		self.add_body_params('FilterCondition', FilterCondition)
	def get_SearchParam(self): # String
		return self.get_body_params().get('SearchParam')

	def set_SearchParam(self, SearchParam):  # String
		self.add_body_params('SearchParam', SearchParam)
	def get_EndTime(self): # String
		return self.get_body_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_body_params('EndTime', EndTime)
	def get_NodeIp(self): # String
		return self.get_body_params().get('NodeIp')

	def set_NodeIp(self, NodeIp):  # String
		self.add_body_params('NodeIp', NodeIp)
	def get_InstanceId(self): # String
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_body_params('InstanceId', InstanceId)
	def get_DbName(self): # String
		return self.get_body_params().get('DbName')

	def set_DbName(self, DbName):  # String
		self.add_body_params('DbName', DbName)
	def get_SearchKeyWord(self): # String
		return self.get_body_params().get('SearchKeyWord')

	def set_SearchKeyWord(self, SearchKeyWord):  # String
		self.add_body_params('SearchKeyWord', SearchKeyWord)
	def get_AcceptLanguage(self): # String
		return self.get_body_params().get('AcceptLanguage')

	def set_AcceptLanguage(self, AcceptLanguage):  # String
		self.add_body_params('AcceptLanguage', AcceptLanguage)
