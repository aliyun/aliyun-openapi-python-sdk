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

class CreatePrometheusAlertRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'CreatePrometheusAlertRule','arms')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Expression(self):
		return self.get_query_params().get('Expression')

	def set_Expression(self,Expression):
		self.add_query_param('Expression',Expression)

	def get_AlertName(self):
		return self.get_query_params().get('AlertName')

	def set_AlertName(self,AlertName):
		self.add_query_param('AlertName',AlertName)

	def get_Annotations(self):
		return self.get_query_params().get('Annotations')

	def set_Annotations(self,Annotations):
		self.add_query_param('Annotations',Annotations)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_DispatchRuleId(self):
		return self.get_query_params().get('DispatchRuleId')

	def set_DispatchRuleId(self,DispatchRuleId):
		self.add_query_param('DispatchRuleId',DispatchRuleId)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_Message(self):
		return self.get_query_params().get('Message')

	def set_Message(self,Message):
		self.add_query_param('Message',Message)

	def get_Labels(self):
		return self.get_query_params().get('Labels')

	def set_Labels(self,Labels):
		self.add_query_param('Labels',Labels)

	def get_Duration(self):
		return self.get_query_params().get('Duration')

	def set_Duration(self,Duration):
		self.add_query_param('Duration',Duration)

	def get_NotifyType(self):
		return self.get_query_params().get('NotifyType')

	def set_NotifyType(self,NotifyType):
		self.add_query_param('NotifyType',NotifyType)