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
from aliyunsdkltl.endpoint import endpoint_data

class AttachDataWithSignatureRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ltl', '2019-05-10', 'AttachDataWithSignature')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_IotSignature(self): # String
		return self.get_query_params().get('IotSignature')

	def set_IotSignature(self, IotSignature):  # String
		self.add_query_param('IotSignature', IotSignature)
	def get_IotAuthType(self): # String
		return self.get_query_params().get('IotAuthType')

	def set_IotAuthType(self, IotAuthType):  # String
		self.add_query_param('IotAuthType', IotAuthType)
	def get_IotIdSource(self): # String
		return self.get_query_params().get('IotIdSource')

	def set_IotIdSource(self, IotIdSource):  # String
		self.add_query_param('IotIdSource', IotIdSource)
	def get_BusinessId(self): # String
		return self.get_query_params().get('BusinessId')

	def set_BusinessId(self, BusinessId):  # String
		self.add_query_param('BusinessId', BusinessId)
	def get_ApiVersion(self): # String
		return self.get_query_params().get('ApiVersion')

	def set_ApiVersion(self, ApiVersion):  # String
		self.add_query_param('ApiVersion', ApiVersion)
	def get_ProductKey(self): # String
		return self.get_query_params().get('ProductKey')

	def set_ProductKey(self, ProductKey):  # String
		self.add_query_param('ProductKey', ProductKey)
	def get_IotId(self): # String
		return self.get_query_params().get('IotId')

	def set_IotId(self, IotId):  # String
		self.add_query_param('IotId', IotId)
	def get_IotDataDigest(self): # String
		return self.get_query_params().get('IotDataDigest')

	def set_IotDataDigest(self, IotDataDigest):  # String
		self.add_query_param('IotDataDigest', IotDataDigest)
	def get_IotIdServiceProvider(self): # String
		return self.get_query_params().get('IotIdServiceProvider')

	def set_IotIdServiceProvider(self, IotIdServiceProvider):  # String
		self.add_query_param('IotIdServiceProvider', IotIdServiceProvider)
	def get_Value(self): # String
		return self.get_query_params().get('Value')

	def set_Value(self, Value):  # String
		self.add_query_param('Value', Value)
	def get_Key(self): # String
		return self.get_query_params().get('Key')

	def set_Key(self, Key):  # String
		self.add_query_param('Key', Key)
