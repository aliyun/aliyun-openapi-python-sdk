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
from aliyunsdkimageaudit.endpoint import endpoint_data

class ScanImageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imageaudit', '2019-12-30', 'ScanImage','imageaudit')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Scenes(self): # RepeatList
		return self.get_body_params().get('Scene')

	def set_Scenes(self, Scene):  # RepeatList
		for depth1 in range(len(Scene)):
			self.add_body_params('Scene.' + str(depth1 + 1), Scene[depth1])
	def get_Tasks(self): # RepeatList
		return self.get_body_params().get('Task')

	def set_Tasks(self, Task):  # RepeatList
		for depth1 in range(len(Task)):
			if Task[depth1].get('DataId') is not None:
				self.add_body_params('Task.' + str(depth1 + 1) + '.DataId', Task[depth1].get('DataId'))
			if Task[depth1].get('ImageURL') is not None:
				self.add_body_params('Task.' + str(depth1 + 1) + '.ImageURL', Task[depth1].get('ImageURL'))
			if Task[depth1].get('MaxFrames') is not None:
				self.add_body_params('Task.' + str(depth1 + 1) + '.MaxFrames', Task[depth1].get('MaxFrames'))
			if Task[depth1].get('Interval') is not None:
				self.add_body_params('Task.' + str(depth1 + 1) + '.Interval', Task[depth1].get('Interval'))
			if Task[depth1].get('ImageTimeMillisecond') is not None:
				self.add_body_params('Task.' + str(depth1 + 1) + '.ImageTimeMillisecond', Task[depth1].get('ImageTimeMillisecond'))
