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
from aliyunsdkmts.endpoint import endpoint_data

class AddMCTemplateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Mts', '2014-06-18', 'AddMCTemplate')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Politics(self):
		return self.get_query_params().get('Politics')

	def set_Politics(self,Politics):
		self.add_query_param('Politics',Politics)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Abuse(self):
		return self.get_query_params().get('Abuse')

	def set_Abuse(self,Abuse):
		self.add_query_param('Abuse',Abuse)

	def get_Qrcode(self):
		return self.get_query_params().get('Qrcode')

	def set_Qrcode(self,Qrcode):
		self.add_query_param('Qrcode',Qrcode)

	def get_Porn(self):
		return self.get_query_params().get('Porn')

	def set_Porn(self,Porn):
		self.add_query_param('Porn',Porn)

	def get_Terrorism(self):
		return self.get_query_params().get('Terrorism')

	def set_Terrorism(self,Terrorism):
		self.add_query_param('Terrorism',Terrorism)

	def get_Logo(self):
		return self.get_query_params().get('Logo')

	def set_Logo(self,Logo):
		self.add_query_param('Logo',Logo)

	def get_Live(self):
		return self.get_query_params().get('Live')

	def set_Live(self,Live):
		self.add_query_param('Live',Live)

	def get_Contraband(self):
		return self.get_query_params().get('Contraband')

	def set_Contraband(self,Contraband):
		self.add_query_param('Contraband',Contraband)

	def get_Ad(self):
		return self.get_query_params().get('Ad')

	def set_Ad(self,Ad):
		self.add_query_param('Ad',Ad)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_spam(self):
		return self.get_query_params().get('spam')

	def set_spam(self,spam):
		self.add_query_param('spam',spam)