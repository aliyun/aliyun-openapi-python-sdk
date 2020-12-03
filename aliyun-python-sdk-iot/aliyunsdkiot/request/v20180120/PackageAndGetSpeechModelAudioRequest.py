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

class PackageAndGetSpeechModelAudioRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'PackageAndGetSpeechModelAudio','iot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ProjectCode(self):
		return self.get_body_params().get('ProjectCode')

	def set_ProjectCode(self,ProjectCode):
		self.add_body_params('ProjectCode', ProjectCode)

	def get_SpeechModelCodeLists(self):
		return self.get_body_params().get('SpeechModelCodeList')

	def set_SpeechModelCodeLists(self, SpeechModelCodeLists):
		for depth1 in range(len(SpeechModelCodeLists)):
			if SpeechModelCodeLists[depth1] is not None:
				self.add_body_params('SpeechModelCodeList.' + str(depth1 + 1) , SpeechModelCodeLists[depth1])