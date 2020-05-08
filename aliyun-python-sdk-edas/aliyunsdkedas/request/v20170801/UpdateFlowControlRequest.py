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

from aliyunsdkcore.request import RoaRequest
from aliyunsdkedas.endpoint import endpoint_data

class UpdateFlowControlRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'UpdateFlowControl','edas')
		self.set_uri_pattern('/pop/v5/flowControl')
		self.set_method('PUT')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ConsumerAppId(self):
		return self.get_query_params().get('ConsumerAppId')

	def set_ConsumerAppId(self,ConsumerAppId):
		self.add_query_param('ConsumerAppId',ConsumerAppId)

	def get_Granularity(self):
		return self.get_query_params().get('Granularity')

	def set_Granularity(self,Granularity):
		self.add_query_param('Granularity',Granularity)

	def get_RuleType(self):
		return self.get_query_params().get('RuleType')

	def set_RuleType(self,RuleType):
		self.add_query_param('RuleType',RuleType)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_UrlVar(self):
		return self.get_query_params().get('UrlVar')

	def set_UrlVar(self,UrlVar):
		self.add_query_param('UrlVar',UrlVar)

	def get_ServiceName(self):
		return self.get_query_params().get('ServiceName')

	def set_ServiceName(self,ServiceName):
		self.add_query_param('ServiceName',ServiceName)

	def get_Threshold(self):
		return self.get_query_params().get('Threshold')

	def set_Threshold(self,Threshold):
		self.add_query_param('Threshold',Threshold)

	def get_RuleId(self):
		return self.get_query_params().get('RuleId')

	def set_RuleId(self,RuleId):
		self.add_query_param('RuleId',RuleId)

	def get_Strategy(self):
		return self.get_query_params().get('Strategy')

	def set_Strategy(self,Strategy):
		self.add_query_param('Strategy',Strategy)

	def get_MethodName(self):
		return self.get_query_params().get('MethodName')

	def set_MethodName(self,MethodName):
		self.add_query_param('MethodName',MethodName)