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
from aliyunsdkcompanyreg.endpoint import endpoint_data

class PhotoInvoiceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'companyreg', '2020-10-22', 'PhotoInvoice')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_UploadedNum(self): # Integer
		return self.get_query_params().get('UploadedNum')

	def set_UploadedNum(self, UploadedNum):  # Integer
		self.add_query_param('UploadedNum', UploadedNum)
	def get_FileUrlList(self): # String
		return self.get_query_params().get('FileUrlList')

	def set_FileUrlList(self, FileUrlList):  # String
		self.add_query_param('FileUrlList', FileUrlList)
	def get_UploadedStamp(self): # Long
		return self.get_query_params().get('UploadedStamp')

	def set_UploadedStamp(self, UploadedStamp):  # Long
		self.add_query_param('UploadedStamp', UploadedStamp)
	def get_BizId(self): # String
		return self.get_query_params().get('BizId')

	def set_BizId(self, BizId):  # String
		self.add_query_param('BizId', BizId)
	def get_FileUrl(self): # String
		return self.get_query_params().get('FileUrl')

	def set_FileUrl(self, FileUrl):  # String
		self.add_query_param('FileUrl', FileUrl)
	def get_IsMobile(self): # Boolean
		return self.get_query_params().get('IsMobile')

	def set_IsMobile(self, IsMobile):  # Boolean
		self.add_query_param('IsMobile', IsMobile)
