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
from aliyunsdkmse.endpoint import endpoint_data

class ModifyLosslessRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mse', '2019-05-31', 'ModifyLosslessRule','mse')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_MseSessionId(self): # String
		return self.get_query_params().get('MseSessionId')

	def set_MseSessionId(self, MseSessionId):  # String
		self.add_query_param('MseSessionId', MseSessionId)
	def get_DelayTime(self): # Long
		return self.get_query_params().get('DelayTime')

	def set_DelayTime(self, DelayTime):  # Long
		self.add_query_param('DelayTime', DelayTime)
	def get_Source(self): # String
		return self.get_query_params().get('Source')

	def set_Source(self, Source):  # String
		self.add_query_param('Source', Source)
	def get_WarmupTime(self): # Long
		return self.get_query_params().get('WarmupTime')

	def set_WarmupTime(self, WarmupTime):  # Long
		self.add_query_param('WarmupTime', WarmupTime)
	def get_AppName(self): # String
		return self.get_query_params().get('AppName')

	def set_AppName(self, AppName):  # String
		self.add_query_param('AppName', AppName)
	def get_Related(self): # Boolean
		return self.get_query_params().get('Related')

	def set_Related(self, Related):  # Boolean
		self.add_query_param('Related', Related)
	def get_Enable(self): # Boolean
		return self.get_query_params().get('Enable')

	def set_Enable(self, Enable):  # Boolean
		self.add_query_param('Enable', Enable)
	def get_Aligned(self): # Boolean
		return self.get_query_params().get('Aligned')

	def set_Aligned(self, Aligned):  # Boolean
		self.add_query_param('Aligned', Aligned)
	def get_ShutdownWaitSeconds(self): # Integer
		return self.get_query_params().get('ShutdownWaitSeconds')

	def set_ShutdownWaitSeconds(self, ShutdownWaitSeconds):  # Integer
		self.add_query_param('ShutdownWaitSeconds', ShutdownWaitSeconds)
	def get_FuncType(self): # Long
		return self.get_query_params().get('FuncType')

	def set_FuncType(self, FuncType):  # Long
		self.add_query_param('FuncType', FuncType)
	def get_AppId(self): # String
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_query_param('AppId', AppId)
	def get_AcceptLanguage(self): # String
		return self.get_query_params().get('AcceptLanguage')

	def set_AcceptLanguage(self, AcceptLanguage):  # String
		self.add_query_param('AcceptLanguage', AcceptLanguage)
