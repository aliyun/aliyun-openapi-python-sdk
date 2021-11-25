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
from aliyunsdkwaf_openapi.endpoint import endpoint_data

class CreateCertAndKeyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'waf-openapi', '2018-01-17', 'CreateCertAndKey','waf')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Cert(self):
		return self.get_query_params().get('Cert')

	def set_Cert(self,Cert):
		self.add_query_param('Cert',Cert)

	def get_HttpsCertName(self):
		return self.get_query_params().get('HttpsCertName')

	def set_HttpsCertName(self,HttpsCertName):
		self.add_query_param('HttpsCertName',HttpsCertName)

	def get_Key(self):
		return self.get_query_params().get('Key')

	def set_Key(self,Key):
		self.add_query_param('Key',Key)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_Domain(self):
		return self.get_query_params().get('Domain')

	def set_Domain(self,Domain):
		self.add_query_param('Domain',Domain)

	def get_Region(self):
		return self.get_query_params().get('Region')

	def set_Region(self,Region):
		self.add_query_param('Region',Region)