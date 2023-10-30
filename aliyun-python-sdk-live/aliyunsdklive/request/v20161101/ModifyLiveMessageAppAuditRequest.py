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
from aliyunsdklive.endpoint import endpoint_data

class ModifyLiveMessageAppAuditRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'ModifyLiveMessageAppAudit','live')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DataCenter(self): # String
		return self.get_query_params().get('DataCenter')

	def set_DataCenter(self, DataCenter):  # String
		self.add_query_param('DataCenter', DataCenter)
	def get_AppId(self): # String
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_query_param('AppId', AppId)
	def get_AuditType(self): # Integer
		return self.get_query_params().get('AuditType')

	def set_AuditType(self, AuditType):  # Integer
		self.add_query_param('AuditType', AuditType)
	def get_AuditUrl(self): # String
		return self.get_query_params().get('AuditUrl')

	def set_AuditUrl(self, AuditUrl):  # String
		self.add_query_param('AuditUrl', AuditUrl)
