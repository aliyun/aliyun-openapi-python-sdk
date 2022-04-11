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
from aliyunsdkvod.endpoint import endpoint_data

class UpdateTranscodeTemplateGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vod', '2017-03-21', 'UpdateTranscodeTemplateGroup','vod')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TranscodeTemplateList(self): # String
		return self.get_query_params().get('TranscodeTemplateList')

	def set_TranscodeTemplateList(self, TranscodeTemplateList):  # String
		self.add_query_param('TranscodeTemplateList', TranscodeTemplateList)
	def get_TranscodeTemplateGroupId(self): # String
		return self.get_query_params().get('TranscodeTemplateGroupId')

	def set_TranscodeTemplateGroupId(self, TranscodeTemplateGroupId):  # String
		self.add_query_param('TranscodeTemplateGroupId', TranscodeTemplateGroupId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_Locked(self): # String
		return self.get_query_params().get('Locked')

	def set_Locked(self, Locked):  # String
		self.add_query_param('Locked', Locked)
