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
import json

class UpdateEventStreamingRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eventbridge', '2020-04-01', 'UpdateEventStreaming')
		self.set_method('POST')

	def get_Sink(self): # Struct
		return self.get_body_params().get('Sink')

	def set_Sink(self, Sink):  # Struct
		self.add_body_params("Sink", json.dumps(Sink))
	def get_Transforms(self): # Array
		return self.get_body_params().get('Transforms')

	def set_Transforms(self, Transforms):  # Array
		self.add_body_params("Transforms", json.dumps(Transforms))
	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_FilterPattern(self): # String
		return self.get_body_params().get('FilterPattern')

	def set_FilterPattern(self, FilterPattern):  # String
		self.add_body_params('FilterPattern', FilterPattern)
	def get_Source(self): # Struct
		return self.get_body_params().get('Source')

	def set_Source(self, Source):  # Struct
		self.add_body_params("Source", json.dumps(Source))
	def get_RunOptions(self): # Struct
		return self.get_body_params().get('RunOptions')

	def set_RunOptions(self, RunOptions):  # Struct
		self.add_body_params("RunOptions", json.dumps(RunOptions))
	def get_EventStreamingName(self): # String
		return self.get_body_params().get('EventStreamingName')

	def set_EventStreamingName(self, EventStreamingName):  # String
		self.add_body_params('EventStreamingName', EventStreamingName)
