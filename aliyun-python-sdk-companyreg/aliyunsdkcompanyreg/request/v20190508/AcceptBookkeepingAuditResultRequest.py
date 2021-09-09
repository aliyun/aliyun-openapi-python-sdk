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
from aliyunsdkcompanyreg.endpoint import endpoint_data

class AcceptBookkeepingAuditResultRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'companyreg', '2019-05-08', 'AcceptBookkeepingAuditResult','companyreg')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Note(self):
		return self.get_query_params().get('Note')

	def set_Note(self,Note):
		self.add_query_param('Note',Note)

	def get_OrgCode(self):
		return self.get_query_params().get('OrgCode')

	def set_OrgCode(self,OrgCode):
		self.add_query_param('OrgCode',OrgCode)

	def get_OrgAddress(self):
		return self.get_query_params().get('OrgAddress')

	def set_OrgAddress(self,OrgAddress):
		self.add_query_param('OrgAddress',OrgAddress)

	def get_OrgName(self):
		return self.get_query_params().get('OrgName')

	def set_OrgName(self,OrgName):
		self.add_query_param('OrgName',OrgName)

	def get_ServiceStartTime(self):
		return self.get_query_params().get('ServiceStartTime')

	def set_ServiceStartTime(self,ServiceStartTime):
		self.add_query_param('ServiceStartTime',ServiceStartTime)

	def get_AuditResult(self):
		return self.get_query_params().get('AuditResult')

	def set_AuditResult(self,AuditResult):
		self.add_query_param('AuditResult',AuditResult)

	def get_BizId(self):
		return self.get_query_params().get('BizId')

	def set_BizId(self,BizId):
		self.add_query_param('BizId',BizId)

	def get_OrgMobile(self):
		return self.get_query_params().get('OrgMobile')

	def set_OrgMobile(self,OrgMobile):
		self.add_query_param('OrgMobile',OrgMobile)