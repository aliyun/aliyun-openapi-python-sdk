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
from aliyunsdkalidns.endpoint import endpoint_data

class ValidateDnsGtmCnameRrCanUseRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alidns', '2015-01-09', 'ValidateDnsGtmCnameRrCanUse','alidns')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CnameMode(self):
		return self.get_query_params().get('CnameMode')

	def set_CnameMode(self,CnameMode):
		self.add_query_param('CnameMode',CnameMode)

	def get_CnameZone(self):
		return self.get_query_params().get('CnameZone')

	def set_CnameZone(self,CnameZone):
		self.add_query_param('CnameZone',CnameZone)

	def get_CnameRr(self):
		return self.get_query_params().get('CnameRr')

	def set_CnameRr(self,CnameRr):
		self.add_query_param('CnameRr',CnameRr)

	def get_CnameType(self):
		return self.get_query_params().get('CnameType')

	def set_CnameType(self,CnameType):
		self.add_query_param('CnameType',CnameType)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)