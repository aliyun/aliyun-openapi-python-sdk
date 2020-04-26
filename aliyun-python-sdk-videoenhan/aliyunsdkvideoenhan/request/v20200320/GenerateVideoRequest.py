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


	def get_TransitionStyle(self):
		return self.get_body_params().get('TransitionStyle')

	def set_TransitionStyle(self,TransitionStyle):
		self.add_body_params('TransitionStyle', TransitionStyle)

	def get_Scene(self):
		return self.get_body_params().get('Scene')

	def set_Scene(self,Scene):
		self.add_body_params('Scene', Scene)

	def get_Duration(self):
		return self.get_body_params().get('Duration')

	def set_Duration(self,Duration):
		self.add_body_params('Duration', Duration)

	def get_PuzzleEffect(self):
		return self.get_body_params().get('PuzzleEffect')

	def set_PuzzleEffect(self,PuzzleEffect):
		self.add_body_params('PuzzleEffect', PuzzleEffect)

	def get_Height(self):
		return self.get_body_params().get('Height')

	def set_Height(self,Height):
		self.add_body_params('Height', Height)

	def get_DurationAdaption(self):
		return self.get_body_params().get('DurationAdaption')

	def set_DurationAdaption(self,DurationAdaption):
		self.add_body_params('DurationAdaption', DurationAdaption)

	def get_FileLists(self):
		return self.get_body_params().get('FileLists')

	def set_FileLists(self,FileLists):
		for i in range(len(FileLists)):	
			if FileLists[i].get('FileName') is not None:
				self.add_body_params('FileList.' + str(i + 1) + '.FileName' , FileLists[i].get('FileName'))
			if FileLists[i].get('FileUrl') is not None:
				self.add_body_params('FileList.' + str(i + 1) + '.FileUrl' , FileLists[i].get('FileUrl'))
			if FileLists[i].get('Type') is not None:
				self.add_body_params('FileList.' + str(i + 1) + '.Type' , FileLists[i].get('Type'))


	def get_Mute(self):
		return self.get_body_params().get('Mute')

	def set_Mute(self,Mute):
		self.add_body_params('Mute', Mute)

	def get_SmartEffect(self):
		return self.get_body_params().get('SmartEffect')

	def set_SmartEffect(self,SmartEffect):
		self.add_body_params('SmartEffect', SmartEffect)

	def get_Width(self):
		return self.get_body_params().get('Width')

	def set_Width(self,Width):
		self.add_body_params('Width', Width)

	def get_Style(self):
		return self.get_body_params().get('Style')

	def set_Style(self,Style):
		self.add_body_params('Style', Style)