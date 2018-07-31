# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class MoPenDoRecognizeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'MoPen', '2018-02-11', 'MoPenDoRecognize')
		self.set_protocol_type('https');
		self.set_method('POST')

	def get_CanvasId(self):
		return self.get_body_params().get('CanvasId')

	def set_CanvasId(self,CanvasId):
		self.add_body_params('CanvasId', CanvasId)

	def get_EndY(self):
		return self.get_body_params().get('EndY')

	def set_EndY(self,EndY):
		self.add_body_params('EndY', EndY)

	def get_EndX(self):
		return self.get_body_params().get('EndX')

	def set_EndX(self,EndX):
		self.add_body_params('EndX', EndX)

	def get_JsonConf(self):
		return self.get_body_params().get('JsonConf')

	def set_JsonConf(self,JsonConf):
		self.add_body_params('JsonConf', JsonConf)

	def get_ExportType(self):
		return self.get_body_params().get('ExportType')

	def set_ExportType(self,ExportType):
		self.add_body_params('ExportType', ExportType)

	def get_StartY(self):
		return self.get_body_params().get('StartY')

	def set_StartY(self,StartY):
		self.add_body_params('StartY', StartY)

	def get_StartX(self):
		return self.get_body_params().get('StartX')

	def set_StartX(self,StartX):
		self.add_body_params('StartX', StartX)