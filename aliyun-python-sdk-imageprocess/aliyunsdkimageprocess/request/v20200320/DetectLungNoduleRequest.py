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
from aliyunsdkimageprocess.endpoint import endpoint_data

class DetectLungNoduleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imageprocess', '2020-03-20', 'DetectLungNodule','imageprocess')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DataFormat(self):
		return self.get_body_params().get('DataFormat')

	def set_DataFormat(self,DataFormat):
		self.add_body_params('DataFormat', DataFormat)

	def get_Threshold(self):
		return self.get_body_params().get('Threshold')

	def set_Threshold(self,Threshold):
		self.add_body_params('Threshold', Threshold)

	def get_URLLists(self):
		return self.get_body_params().get('URLList')

	def set_URLLists(self, URLLists):
		for depth1 in range(len(URLLists)):
			if URLLists[depth1].get('URL') is not None:
				self.add_body_params('URLList.' + str(depth1 + 1) + '.URL', URLLists[depth1].get('URL'))

	def get_OrgId(self):
		return self.get_body_params().get('OrgId')

	def set_OrgId(self,OrgId):
		self.add_body_params('OrgId', OrgId)

	def get_OrgName(self):
		return self.get_body_params().get('OrgName')

	def set_OrgName(self,OrgName):
		self.add_body_params('OrgName', OrgName)