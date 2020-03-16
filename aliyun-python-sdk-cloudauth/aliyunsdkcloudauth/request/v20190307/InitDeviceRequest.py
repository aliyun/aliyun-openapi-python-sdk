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
from aliyunsdkcloudauth.endpoint import endpoint_data

class InitDeviceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudauth', '2019-03-07', 'InitDevice','cloudauth')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Channel(self):
		return self.get_query_params().get('Channel')

	def set_Channel(self,Channel):
		self.add_query_param('Channel',Channel)

	def get_BizData(self):
		return self.get_query_params().get('BizData')

	def set_BizData(self,BizData):
		self.add_query_param('BizData',BizData)

	def get_Merchant(self):
		return self.get_query_params().get('Merchant')

	def set_Merchant(self,Merchant):
		self.add_query_param('Merchant',Merchant)

	def get_AppVersion(self):
		return self.get_query_params().get('AppVersion')

	def set_AppVersion(self,AppVersion):
		self.add_query_param('AppVersion',AppVersion)

	def get_DeviceToken(self):
		return self.get_query_params().get('DeviceToken')

	def set_DeviceToken(self,DeviceToken):
		self.add_query_param('DeviceToken',DeviceToken)

	def get_CertifyId(self):
		return self.get_query_params().get('CertifyId')

	def set_CertifyId(self,CertifyId):
		self.add_query_param('CertifyId',CertifyId)

	def get_OuterOrderNo(self):
		return self.get_query_params().get('OuterOrderNo')

	def set_OuterOrderNo(self,OuterOrderNo):
		self.add_query_param('OuterOrderNo',OuterOrderNo)

	def get_ProduceNode(self):
		return self.get_query_params().get('ProduceNode')

	def set_ProduceNode(self,ProduceNode):
		self.add_query_param('ProduceNode',ProduceNode)

	def get_ProductName(self):
		return self.get_query_params().get('ProductName')

	def set_ProductName(self,ProductName):
		self.add_query_param('ProductName',ProductName)

	def get_CertifyPrincipal(self):
		return self.get_query_params().get('CertifyPrincipal')

	def set_CertifyPrincipal(self,CertifyPrincipal):
		self.add_query_param('CertifyPrincipal',CertifyPrincipal)

	def get_MetaInfo(self):
		return self.get_query_params().get('MetaInfo')

	def set_MetaInfo(self,MetaInfo):
		self.add_query_param('MetaInfo',MetaInfo)