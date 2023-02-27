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
from aliyunsdkice.endpoint import endpoint_data

class SubmitLiveEditingJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ICE', '2020-11-09', 'SubmitLiveEditingJob','ice')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_LiveStreamConfig(self): # String
		return self.get_query_params().get('LiveStreamConfig')

	def set_LiveStreamConfig(self, LiveStreamConfig):  # String
		self.add_query_param('LiveStreamConfig', LiveStreamConfig)
	def get_Clips(self): # String
		return self.get_query_params().get('Clips')

	def set_Clips(self, Clips):  # String
		self.add_query_param('Clips', Clips)
	def get_OutputMediaTarget(self): # String
		return self.get_query_params().get('OutputMediaTarget')

	def set_OutputMediaTarget(self, OutputMediaTarget):  # String
		self.add_query_param('OutputMediaTarget', OutputMediaTarget)
	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_OutputMediaConfig(self): # String
		return self.get_query_params().get('OutputMediaConfig')

	def set_OutputMediaConfig(self, OutputMediaConfig):  # String
		self.add_query_param('OutputMediaConfig', OutputMediaConfig)
	def get_ProjectId(self): # String
		return self.get_query_params().get('ProjectId')

	def set_ProjectId(self, ProjectId):  # String
		self.add_query_param('ProjectId', ProjectId)
	def get_MediaProduceConfig(self): # String
		return self.get_query_params().get('MediaProduceConfig')

	def set_MediaProduceConfig(self, MediaProduceConfig):  # String
		self.add_query_param('MediaProduceConfig', MediaProduceConfig)
