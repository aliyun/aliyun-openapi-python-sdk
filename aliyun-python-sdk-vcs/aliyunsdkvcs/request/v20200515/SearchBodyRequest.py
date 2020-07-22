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
from aliyunsdkvcs.endpoint import endpoint_data

class SearchBodyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vcs', '2020-05-15', 'SearchBody','vcs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CorpId(self):
		return self.get_body_params().get('CorpId')

	def set_CorpId(self,CorpId):
		self.add_body_params('CorpId', CorpId)

	def get_GbId(self):
		return self.get_body_params().get('GbId')

	def set_GbId(self,GbId):
		self.add_body_params('GbId', GbId)

	def get_StartTimeStamp(self):
		return self.get_body_params().get('StartTimeStamp')

	def set_StartTimeStamp(self,StartTimeStamp):
		self.add_body_params('StartTimeStamp', StartTimeStamp)

	def get_EndTimeStamp(self):
		return self.get_body_params().get('EndTimeStamp')

	def set_EndTimeStamp(self,EndTimeStamp):
		self.add_body_params('EndTimeStamp', EndTimeStamp)

	def get_PageNo(self):
		return self.get_body_params().get('PageNo')

	def set_PageNo(self,PageNo):
		self.add_body_params('PageNo', PageNo)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_OptionList(self):
		return self.get_body_params().get('OptionList')

	def set_OptionList(self,OptionList):
		self.add_body_params('OptionList', OptionList)