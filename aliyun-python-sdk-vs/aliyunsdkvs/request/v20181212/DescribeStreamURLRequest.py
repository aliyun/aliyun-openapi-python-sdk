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
from aliyunsdkvs.endpoint import endpoint_data

class DescribeStreamURLRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vs', '2018-12-12', 'DescribeStreamURL','vs')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AuthKey(self):
		return self.get_query_params().get('AuthKey')

	def set_AuthKey(self,AuthKey):
		self.add_query_param('AuthKey',AuthKey)

	def get_Auth(self):
		return self.get_query_params().get('Auth')

	def set_Auth(self,Auth):
		self.add_query_param('Auth',Auth)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_OutHostType(self):
		return self.get_query_params().get('OutHostType')

	def set_OutHostType(self,OutHostType):
		self.add_query_param('OutHostType',OutHostType)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)

	def get_OutProtocol(self):
		return self.get_query_params().get('OutProtocol')

	def set_OutProtocol(self,OutProtocol):
		self.add_query_param('OutProtocol',OutProtocol)

	def get_Transcode(self):
		return self.get_query_params().get('Transcode')

	def set_Transcode(self,Transcode):
		self.add_query_param('Transcode',Transcode)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Expire(self):
		return self.get_query_params().get('Expire')

	def set_Expire(self,Expire):
		self.add_query_param('Expire',Expire)

	def get_Location(self):
		return self.get_query_params().get('Location')

	def set_Location(self,Location):
		self.add_query_param('Location',Location)