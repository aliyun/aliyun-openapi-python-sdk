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

class EncodeBlindWatermarkRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2017-09-06', 'EncodeBlindWatermark','imm')

	def get_ImageQuality(self):
		return self.get_query_params().get('ImageQuality')

	def set_ImageQuality(self,ImageQuality):
		self.add_query_param('ImageQuality',ImageQuality)

	def get_WatermarkUri(self):
		return self.get_query_params().get('WatermarkUri')

	def set_WatermarkUri(self,WatermarkUri):
		self.add_query_param('WatermarkUri',WatermarkUri)

	def get_Project(self):
		return self.get_query_params().get('Project')

	def set_Project(self,Project):
		self.add_query_param('Project',Project)

	def get_Content(self):
		return self.get_query_params().get('Content')

	def set_Content(self,Content):
		self.add_query_param('Content',Content)

	def get_TargetUri(self):
		return self.get_query_params().get('TargetUri')

	def set_TargetUri(self,TargetUri):
		self.add_query_param('TargetUri',TargetUri)

	def get_TargetImageType(self):
		return self.get_query_params().get('TargetImageType')

	def set_TargetImageType(self,TargetImageType):
		self.add_query_param('TargetImageType',TargetImageType)

	def get_ImageUri(self):
		return self.get_query_params().get('ImageUri')

	def set_ImageUri(self,ImageUri):
		self.add_query_param('ImageUri',ImageUri)