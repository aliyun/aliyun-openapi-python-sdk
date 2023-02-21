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

class GetQccSearchCertificationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dt-oc-info', '2022-08-29', 'GetQccSearchCertification')
		self.set_method('POST')

	def get_CertCategory(self): # String
		return self.get_body_params().get('CertCategory')

	def set_CertCategory(self, CertCategory):  # String
		self.add_body_params('CertCategory', CertCategory)
	def get_EntName(self): # String
		return self.get_body_params().get('EntName')

	def set_EntName(self, EntName):  # String
		self.add_body_params('EntName', EntName)
	def get_PageNo(self): # Integer
		return self.get_body_params().get('PageNo')

	def set_PageNo(self, PageNo):  # Integer
		self.add_body_params('PageNo', PageNo)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
