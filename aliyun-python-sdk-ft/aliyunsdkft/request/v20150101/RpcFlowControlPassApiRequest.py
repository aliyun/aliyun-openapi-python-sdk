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
class RpcFlowControlPassApiRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ft', '2015-01-01', 'RpcFlowControlPassApi')

	def get_IntValue(self):
		return self.get_query_params().get('IntValue')

	def set_IntValue(self,IntValue):
		self.add_query_param('IntValue',IntValue)

	def get_NumberRange(self):
		return self.get_query_params().get('NumberRange')

	def set_NumberRange(self,NumberRange):
		self.add_query_param('NumberRange',NumberRange)

	def get_StringValue(self):
		return self.get_query_params().get('StringValue')

	def set_StringValue(self,StringValue):
		self.add_query_param('StringValue',StringValue)

	def get_SwitchValue(self):
		return self.get_query_params().get('SwitchValue')

	def set_SwitchValue(self,SwitchValue):
		self.add_query_param('SwitchValue',SwitchValue)

	def get_EnumValue(self):
		return self.get_query_params().get('EnumValue')

	def set_EnumValue(self,EnumValue):
		self.add_query_param('EnumValue',EnumValue)

	def get_RequiredValue(self):
		return self.get_query_params().get('RequiredValue')

	def set_RequiredValue(self,RequiredValue):
		self.add_query_param('RequiredValue',RequiredValue)

	def get_DefaultValue(self):
		return self.get_query_params().get('DefaultValue')

	def set_DefaultValue(self,DefaultValue):
		self.add_query_param('DefaultValue',DefaultValue)

	def get_HttpStatusCode(self):
		return self.get_query_params().get('HttpStatusCode')

	def set_HttpStatusCode(self,HttpStatusCode):
		self.add_query_param('HttpStatusCode',HttpStatusCode)

	def get_Success(self):
		return self.get_query_params().get('Success')

	def set_Success(self,Success):
		self.add_query_param('Success',Success)

	def get_Code(self):
		return self.get_query_params().get('Code')

	def set_Code(self,Code):
		self.add_query_param('Code',Code)

	def get_Message(self):
		return self.get_query_params().get('Message')

	def set_Message(self,Message):
		self.add_query_param('Message',Message)

	def get_ResultSwitchValue(self):
		return self.get_query_params().get('ResultSwitchValue')

	def set_ResultSwitchValue(self,ResultSwitchValue):
		self.add_query_param('ResultSwitchValue',ResultSwitchValue)