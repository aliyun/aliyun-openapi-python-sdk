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
from aliyunsdkiot.endpoint import endpoint_data

class CreateOTAFirmwareRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'CreateOTAFirmware','iot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SignMethod(self):
		return self.get_query_params().get('SignMethod')

	def set_SignMethod(self,SignMethod):
		self.add_query_param('SignMethod',SignMethod)

	def get_MultiFiless(self):
		return self.get_query_params().get('MultiFiles')

	def set_MultiFiless(self, MultiFiless):
		for depth1 in range(len(MultiFiless)):
			if MultiFiless[depth1].get('Size') is not None:
				self.add_query_param('MultiFiles.' + str(depth1 + 1) + '.Size', MultiFiless[depth1].get('Size'))
			if MultiFiless[depth1].get('Name') is not None:
				self.add_query_param('MultiFiles.' + str(depth1 + 1) + '.Name', MultiFiless[depth1].get('Name'))
			if MultiFiless[depth1].get('SignValue') is not None:
				self.add_query_param('MultiFiles.' + str(depth1 + 1) + '.SignValue', MultiFiless[depth1].get('SignValue'))
			if MultiFiless[depth1].get('FileMd5') is not None:
				self.add_query_param('MultiFiles.' + str(depth1 + 1) + '.FileMd5', MultiFiless[depth1].get('FileMd5'))
			if MultiFiless[depth1].get('Url') is not None:
				self.add_query_param('MultiFiles.' + str(depth1 + 1) + '.Url', MultiFiless[depth1].get('Url'))

	def get_NeedToVerify(self):
		return self.get_query_params().get('NeedToVerify')

	def set_NeedToVerify(self,NeedToVerify):
		self.add_query_param('NeedToVerify',NeedToVerify)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_FirmwareUrl(self):
		return self.get_query_params().get('FirmwareUrl')

	def set_FirmwareUrl(self,FirmwareUrl):
		self.add_query_param('FirmwareUrl',FirmwareUrl)

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_FirmwareDesc(self):
		return self.get_query_params().get('FirmwareDesc')

	def set_FirmwareDesc(self,FirmwareDesc):
		self.add_query_param('FirmwareDesc',FirmwareDesc)

	def get_ModuleName(self):
		return self.get_query_params().get('ModuleName')

	def set_ModuleName(self,ModuleName):
		self.add_query_param('ModuleName',ModuleName)

	def get_FirmwareSign(self):
		return self.get_query_params().get('FirmwareSign')

	def set_FirmwareSign(self,FirmwareSign):
		self.add_query_param('FirmwareSign',FirmwareSign)

	def get_FirmwareSize(self):
		return self.get_query_params().get('FirmwareSize')

	def set_FirmwareSize(self,FirmwareSize):
		self.add_query_param('FirmwareSize',FirmwareSize)

	def get_FirmwareName(self):
		return self.get_query_params().get('FirmwareName')

	def set_FirmwareName(self,FirmwareName):
		self.add_query_param('FirmwareName',FirmwareName)

	def get_ProductKey(self):
		return self.get_query_params().get('ProductKey')

	def set_ProductKey(self,ProductKey):
		self.add_query_param('ProductKey',ProductKey)

	def get_SrcVersion(self):
		return self.get_query_params().get('SrcVersion')

	def set_SrcVersion(self,SrcVersion):
		self.add_query_param('SrcVersion',SrcVersion)

	def get_Udi(self):
		return self.get_query_params().get('Udi')

	def set_Udi(self,Udi):
		self.add_query_param('Udi',Udi)

	def get_DestVersion(self):
		return self.get_query_params().get('DestVersion')

	def set_DestVersion(self,DestVersion):
		self.add_query_param('DestVersion',DestVersion)