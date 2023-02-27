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
import json

class SubmitLiveSnapshotJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ICE', '2020-11-09', 'SubmitLiveSnapshotJob','ice')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_StreamInput(self): # Struct
		return self.get_body_params().get('StreamInput')

	def set_StreamInput(self, StreamInput):  # Struct
		self.add_body_params("StreamInput", json.dumps(StreamInput))
	def get_TemplateId(self): # String
		return self.get_body_params().get('TemplateId')

	def set_TemplateId(self, TemplateId):  # String
		self.add_body_params('TemplateId', TemplateId)
	def get_SnapshotOutput(self): # Struct
		return self.get_body_params().get('SnapshotOutput')

	def set_SnapshotOutput(self, SnapshotOutput):  # Struct
		self.add_body_params("SnapshotOutput", json.dumps(SnapshotOutput))
	def get_CallbackUrl(self): # String
		return self.get_body_params().get('CallbackUrl')

	def set_CallbackUrl(self, CallbackUrl):  # String
		self.add_body_params('CallbackUrl', CallbackUrl)
	def get_JobName(self): # String
		return self.get_body_params().get('JobName')

	def set_JobName(self, JobName):  # String
		self.add_body_params('JobName', JobName)
