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

class DescribeSampleSqlRawTextsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OceanBasePro', '2019-09-01', 'DescribeSampleSqlRawTexts','oceanbase')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TraceId(self): # String
		return self.get_body_params().get('TraceId')

	def set_TraceId(self, TraceId):  # String
		self.add_body_params('TraceId', TraceId)
	def get_StartTime(self): # String
		return self.get_body_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_body_params('StartTime', StartTime)
	def get_TenantId(self): # String
		return self.get_body_params().get('TenantId')

	def set_TenantId(self, TenantId):  # String
		self.add_body_params('TenantId', TenantId)
	def get_Limit(self): # String
		return self.get_body_params().get('Limit')

	def set_Limit(self, Limit):  # String
		self.add_body_params('Limit', Limit)
	def get_SqlId(self): # String
		return self.get_body_params().get('SqlId')

	def set_SqlId(self, SqlId):  # String
		self.add_body_params('SqlId', SqlId)
	def get_EndTime(self): # String
		return self.get_body_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_body_params('EndTime', EndTime)
	def get_InstanceId(self): # String
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_body_params('InstanceId', InstanceId)
	def get_DbName(self): # String
		return self.get_body_params().get('DbName')

	def set_DbName(self, DbName):  # String
		self.add_body_params('DbName', DbName)
