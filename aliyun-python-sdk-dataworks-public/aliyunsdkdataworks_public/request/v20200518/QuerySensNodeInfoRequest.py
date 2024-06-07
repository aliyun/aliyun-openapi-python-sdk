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
from aliyunsdkdataworks_public.endpoint import endpoint_data

class QuerySensNodeInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'QuerySensNodeInfo')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PageNo(self): # Integer
		return self.get_body_params().get('PageNo')

	def set_PageNo(self, PageNo):  # Integer
		self.add_body_params('PageNo', PageNo)
	def get_TenantId(self): # String
		return self.get_body_params().get('TenantId')

	def set_TenantId(self, TenantId):  # String
		self.add_body_params('TenantId', TenantId)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_SensitiveName(self): # String
		return self.get_body_params().get('SensitiveName')

	def set_SensitiveName(self, SensitiveName):  # String
		self.add_body_params('SensitiveName', SensitiveName)
	def get_TemplateId(self): # String
		return self.get_body_params().get('TemplateId')

	def set_TemplateId(self, TemplateId):  # String
		self.add_body_params('TemplateId', TemplateId)
	def get_NodeId(self): # String
		return self.get_body_params().get('NodeId')

	def set_NodeId(self, NodeId):  # String
		self.add_body_params('NodeId', NodeId)
	def get_status(self): # Integer
		return self.get_body_params().get('status')

	def set_status(self, status):  # Integer
		self.add_body_params('status', status)
