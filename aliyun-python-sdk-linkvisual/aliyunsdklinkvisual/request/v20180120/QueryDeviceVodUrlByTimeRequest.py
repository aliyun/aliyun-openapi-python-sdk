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
from aliyunsdklinkvisual.endpoint import endpoint_data

class QueryDeviceVodUrlByTimeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Linkvisual', '2018-01-20', 'QueryDeviceVodUrlByTime','Linkvisual')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Scheme(self): # String
		return self.get_query_params().get('Scheme')

	def set_Scheme(self, Scheme):  # String
		self.add_query_param('Scheme', Scheme)
	def get_PlayUnLimited(self): # Boolean
		return self.get_query_params().get('PlayUnLimited')

	def set_PlayUnLimited(self, PlayUnLimited):  # Boolean
		self.add_query_param('PlayUnLimited', PlayUnLimited)
	def get_EncryptType(self): # Integer
		return self.get_query_params().get('EncryptType')

	def set_EncryptType(self, EncryptType):  # Integer
		self.add_query_param('EncryptType', EncryptType)
	def get_IotId(self): # String
		return self.get_query_params().get('IotId')

	def set_IotId(self, IotId):  # String
		self.add_query_param('IotId', IotId)
	def get_IotInstanceId(self): # String
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self, IotInstanceId):  # String
		self.add_query_param('IotInstanceId', IotInstanceId)
	def get_ShouldEncrypt(self): # Boolean
		return self.get_query_params().get('ShouldEncrypt')

	def set_ShouldEncrypt(self, ShouldEncrypt):  # Boolean
		self.add_query_param('ShouldEncrypt', ShouldEncrypt)
	def get_EnableStun(self): # Boolean
		return self.get_query_params().get('EnableStun')

	def set_EnableStun(self, EnableStun):  # Boolean
		self.add_query_param('EnableStun', EnableStun)
	def get_EndTime(self): # Integer
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Integer
		self.add_query_param('EndTime', EndTime)
	def get_BeginTime(self): # Integer
		return self.get_query_params().get('BeginTime')

	def set_BeginTime(self, BeginTime):  # Integer
		self.add_query_param('BeginTime', BeginTime)
	def get_ProductKey(self): # String
		return self.get_query_params().get('ProductKey')

	def set_ProductKey(self, ProductKey):  # String
		self.add_query_param('ProductKey', ProductKey)
	def get_SeekTime(self): # Integer
		return self.get_query_params().get('SeekTime')

	def set_SeekTime(self, SeekTime):  # Integer
		self.add_query_param('SeekTime', SeekTime)
	def get_DeviceName(self): # String
		return self.get_query_params().get('DeviceName')

	def set_DeviceName(self, DeviceName):  # String
		self.add_query_param('DeviceName', DeviceName)
	def get_UrlValidDuration(self): # Integer
		return self.get_query_params().get('UrlValidDuration')

	def set_UrlValidDuration(self, UrlValidDuration):  # Integer
		self.add_query_param('UrlValidDuration', UrlValidDuration)
