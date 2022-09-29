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
from aliyunsdkvideoenhan.endpoint import endpoint_data

class GenerateVideoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'videoenhan', '2020-03-20', 'GenerateVideo','videoenhan')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TransitionStyle(self): # String
		return self.get_body_params().get('TransitionStyle')

	def set_TransitionStyle(self, TransitionStyle):  # String
		self.add_body_params('TransitionStyle', TransitionStyle)
	def get_Scene(self): # String
		return self.get_body_params().get('Scene')

	def set_Scene(self, Scene):  # String
		self.add_body_params('Scene', Scene)
	def get_Duration(self): # Float
		return self.get_body_params().get('Duration')

	def set_Duration(self, Duration):  # Float
		self.add_body_params('Duration', Duration)
	def get_PuzzleEffect(self): # Boolean
		return self.get_body_params().get('PuzzleEffect')

	def set_PuzzleEffect(self, PuzzleEffect):  # Boolean
		self.add_body_params('PuzzleEffect', PuzzleEffect)
	def get_Height(self): # Integer
		return self.get_body_params().get('Height')

	def set_Height(self, Height):  # Integer
		self.add_body_params('Height', Height)
	def get_DurationAdaption(self): # Boolean
		return self.get_body_params().get('DurationAdaption')

	def set_DurationAdaption(self, DurationAdaption):  # Boolean
		self.add_body_params('DurationAdaption', DurationAdaption)
	def get_FileLists(self): # RepeatList
		return self.get_body_params().get('FileList')

	def set_FileLists(self, FileList):  # RepeatList
		for depth1 in range(len(FileList)):
			if FileList[depth1].get('FileName') is not None:
				self.add_body_params('FileList.' + str(depth1 + 1) + '.FileName', FileList[depth1].get('FileName'))
			if FileList[depth1].get('FileUrl') is not None:
				self.add_body_params('FileList.' + str(depth1 + 1) + '.FileUrl', FileList[depth1].get('FileUrl'))
			if FileList[depth1].get('Type') is not None:
				self.add_body_params('FileList.' + str(depth1 + 1) + '.Type', FileList[depth1].get('Type'))
	def get_Mute(self): # Boolean
		return self.get_body_params().get('Mute')

	def set_Mute(self, Mute):  # Boolean
		self.add_body_params('Mute', Mute)
	def get_SmartEffect(self): # Boolean
		return self.get_body_params().get('SmartEffect')

	def set_SmartEffect(self, SmartEffect):  # Boolean
		self.add_body_params('SmartEffect', SmartEffect)
	def get_Width(self): # Integer
		return self.get_body_params().get('Width')

	def set_Width(self, Width):  # Integer
		self.add_body_params('Width', Width)
	def get_Style(self): # String
		return self.get_body_params().get('Style')

	def set_Style(self, Style):  # String
		self.add_body_params('Style', Style)
