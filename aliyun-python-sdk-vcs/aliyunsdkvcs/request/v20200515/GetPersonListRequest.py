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

class GetPersonListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vcs', '2020-05-15', 'GetPersonList','vcs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CorpId(self):
		return self.get_body_params().get('CorpId')

	def set_CorpId(self,CorpId):
		self.add_body_params('CorpId', CorpId)

	def get_FaceMatchingRateThreshold(self):
		return self.get_body_params().get('FaceMatchingRateThreshold')

	def set_FaceMatchingRateThreshold(self,FaceMatchingRateThreshold):
		self.add_body_params('FaceMatchingRateThreshold', FaceMatchingRateThreshold)

	def get_PageNumber(self):
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_body_params('PageNumber', PageNumber)

	def get_CorpIdList(self):
		return self.get_body_params().get('CorpIdList')

	def set_CorpIdList(self,CorpIdList):
		self.add_body_params('CorpIdList', CorpIdList)

	def get_FaceUrl(self):
		return self.get_body_params().get('FaceUrl')

	def set_FaceUrl(self,FaceUrl):
		self.add_body_params('FaceUrl', FaceUrl)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_PersonIdList(self):
		return self.get_body_params().get('PersonIdList')

	def set_PersonIdList(self,PersonIdList):
		self.add_body_params('PersonIdList', PersonIdList)