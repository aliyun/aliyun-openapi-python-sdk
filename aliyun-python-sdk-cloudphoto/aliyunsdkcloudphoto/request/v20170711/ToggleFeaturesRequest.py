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
class ToggleFeaturesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudPhoto', '2017-07-11', 'ToggleFeatures','cloudphoto')
		self.set_protocol_type('https');

	def get_DisabledFeaturess(self):
		return self.get_query_params().get('DisabledFeaturess')

	def set_DisabledFeaturess(self,DisabledFeaturess):
		for i in range(len(DisabledFeaturess)):	
			if DisabledFeaturess[i] is not None:
				self.add_query_param('DisabledFeatures.' + str(i + 1) , DisabledFeaturess[i]);

	def get_StoreName(self):
		return self.get_query_params().get('StoreName')

	def set_StoreName(self,StoreName):
		self.add_query_param('StoreName',StoreName)

	def get_EnabledFeaturess(self):
		return self.get_query_params().get('EnabledFeaturess')

	def set_EnabledFeaturess(self,EnabledFeaturess):
		for i in range(len(EnabledFeaturess)):	
			if EnabledFeaturess[i] is not None:
				self.add_query_param('EnabledFeatures.' + str(i + 1) , EnabledFeaturess[i]);