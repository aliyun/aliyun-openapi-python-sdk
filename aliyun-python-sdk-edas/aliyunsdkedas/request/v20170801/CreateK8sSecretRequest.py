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

from aliyunsdkcore.request import RoaRequest
from aliyunsdkedas.endpoint import endpoint_data

class CreateK8sSecretRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'CreateK8sSecret','Edas')
		self.set_uri_pattern('/pop/v5/k8s/acs/k8s_secret')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Base64Encoded(self):
		return self.get_body_params().get('Base64Encoded')

	def set_Base64Encoded(self,Base64Encoded):
		self.add_body_params('Base64Encoded', Base64Encoded)

	def get_Data(self):
		return self.get_body_params().get('Data')

	def set_Data(self,Data):
		self.add_body_params('Data', Data)

	def get_Name(self):
		return self.get_body_params().get('Name')

	def set_Name(self,Name):
		self.add_body_params('Name', Name)

	def get_Namespace(self):
		return self.get_body_params().get('Namespace')

	def set_Namespace(self,Namespace):
		self.add_body_params('Namespace', Namespace)

	def get_ClusterId(self):
		return self.get_body_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_body_params('ClusterId', ClusterId)

	def get_CertId(self):
		return self.get_body_params().get('CertId')

	def set_CertId(self,CertId):
		self.add_body_params('CertId', CertId)

	def get_Type(self):
		return self.get_body_params().get('Type')

	def set_Type(self,Type):
		self.add_body_params('Type', Type)

	def get_CertRegionId(self):
		return self.get_body_params().get('CertRegionId')

	def set_CertRegionId(self,CertRegionId):
		self.add_body_params('CertRegionId', CertRegionId)