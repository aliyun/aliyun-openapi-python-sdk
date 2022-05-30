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
from aliyunsdkarms.endpoint import endpoint_data

class UpdatePrometheusAlertRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'UpdatePrometheusAlertRule','arms')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Expression(self): # String
		return self.get_query_params().get('Expression')

	def set_Expression(self, Expression):  # String
		self.add_query_param('Expression', Expression)
	def get_AlertName(self): # String
		return self.get_query_params().get('AlertName')

	def set_AlertName(self, AlertName):  # String
		self.add_query_param('AlertName', AlertName)
	def get_Annotations(self): # String
		return self.get_query_params().get('Annotations')

	def set_Annotations(self, Annotations):  # String
		self.add_query_param('Annotations', Annotations)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_DispatchRuleId(self): # Long
		return self.get_query_params().get('DispatchRuleId')

	def set_DispatchRuleId(self, DispatchRuleId):  # Long
		self.add_query_param('DispatchRuleId', DispatchRuleId)
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_Message(self): # String
		return self.get_query_params().get('Message')

	def set_Message(self, Message):  # String
		self.add_query_param('Message', Message)
	def get_Labels(self): # String
		return self.get_query_params().get('Labels')

	def set_Labels(self, Labels):  # String
		self.add_query_param('Labels', Labels)
	def get_Duration(self): # String
		return self.get_query_params().get('Duration')

	def set_Duration(self, Duration):  # String
		self.add_query_param('Duration', Duration)
	def get_AlertId(self): # Long
		return self.get_query_params().get('AlertId')

	def set_AlertId(self, AlertId):  # Long
		self.add_query_param('AlertId', AlertId)
	def get_NotifyType(self): # String
		return self.get_query_params().get('NotifyType')

	def set_NotifyType(self, NotifyType):  # String
		self.add_query_param('NotifyType', NotifyType)
