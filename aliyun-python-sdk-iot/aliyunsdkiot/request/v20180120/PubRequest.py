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
from aliyunsdkiot.endpoint import endpoint_data

class PubRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'Pub','iot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_UserProps(self):
		return self.get_query_params().get('UserProp')

	def set_UserProps(self, UserProps):
		for depth1 in range(len(UserProps)):
			if UserProps[depth1].get('Value') is not None:
				self.add_query_param('UserProp.' + str(depth1 + 1) + '.Value', UserProps[depth1].get('Value'))
			if UserProps[depth1].get('Key') is not None:
				self.add_query_param('UserProp.' + str(depth1 + 1) + '.Key', UserProps[depth1].get('Key'))

	def get_MessageContent(self):
		return self.get_body_params().get('MessageContent')

	def set_MessageContent(self,MessageContent):
		self.add_body_params('MessageContent', MessageContent)

	def get_Qos(self):
		return self.get_query_params().get('Qos')

	def set_Qos(self,Qos):
		self.add_query_param('Qos',Qos)

	def get_CorrelationData(self):
		return self.get_query_params().get('CorrelationData')

	def set_CorrelationData(self,CorrelationData):
		self.add_query_param('CorrelationData',CorrelationData)

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_MessageExpiryInterval(self):
		return self.get_query_params().get('MessageExpiryInterval')

	def set_MessageExpiryInterval(self,MessageExpiryInterval):
		self.add_query_param('MessageExpiryInterval',MessageExpiryInterval)

	def get_ResponseTopic(self):
		return self.get_query_params().get('ResponseTopic')

	def set_ResponseTopic(self,ResponseTopic):
		self.add_query_param('ResponseTopic',ResponseTopic)

	def get_TopicFullName(self):
		return self.get_query_params().get('TopicFullName')

	def set_TopicFullName(self,TopicFullName):
		self.add_query_param('TopicFullName',TopicFullName)

	def get_PayloadFormatIndicator(self):
		return self.get_query_params().get('PayloadFormatIndicator')

	def set_PayloadFormatIndicator(self,PayloadFormatIndicator):
		self.add_query_param('PayloadFormatIndicator',PayloadFormatIndicator)

	def get_ProductKey(self):
		return self.get_query_params().get('ProductKey')

	def set_ProductKey(self,ProductKey):
		self.add_query_param('ProductKey',ProductKey)

	def get_ContentType(self):
		return self.get_query_params().get('ContentType')

	def set_ContentType(self,ContentType):
		self.add_query_param('ContentType',ContentType)

	def get_Retained(self):
		return self.get_query_params().get('Retained')

	def set_Retained(self,Retained):
		self.add_query_param('Retained',Retained)

	def get_DeviceName(self):
		return self.get_query_params().get('DeviceName')

	def set_DeviceName(self,DeviceName):
		self.add_query_param('DeviceName',DeviceName)