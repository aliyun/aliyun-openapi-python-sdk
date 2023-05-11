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

class CreatePictureSearchJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Linkvisual', '2018-01-20', 'CreatePictureSearchJob','Linkvisual')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Threshold(self): # Float
		return self.get_query_params().get('Threshold')

	def set_Threshold(self, Threshold):  # Float
		self.add_query_param('Threshold', Threshold)
	def get_SearchPicUrl(self): # String
		return self.get_query_params().get('SearchPicUrl')

	def set_SearchPicUrl(self, SearchPicUrl):  # String
		self.add_query_param('SearchPicUrl', SearchPicUrl)
	def get_StartTime(self): # Long
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # Long
		self.add_query_param('StartTime', StartTime)
	def get_PictureSearchType(self): # Integer
		return self.get_query_params().get('PictureSearchType')

	def set_PictureSearchType(self, PictureSearchType):  # Integer
		self.add_query_param('PictureSearchType', PictureSearchType)
	def get_BodyThreshold(self): # Float
		return self.get_query_params().get('BodyThreshold')

	def set_BodyThreshold(self, BodyThreshold):  # Float
		self.add_query_param('BodyThreshold', BodyThreshold)
	def get_EndTime(self): # Long
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_query_param('EndTime', EndTime)
	def get_AppInstanceId(self): # String
		return self.get_query_params().get('AppInstanceId')

	def set_AppInstanceId(self, AppInstanceId):  # String
		self.add_query_param('AppInstanceId', AppInstanceId)
