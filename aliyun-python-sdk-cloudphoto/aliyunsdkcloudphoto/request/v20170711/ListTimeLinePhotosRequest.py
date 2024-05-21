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
class ListTimeLinePhotosRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudPhoto', '2017-07-11', 'ListTimeLinePhotos','cloudphoto')
		self.set_protocol_type('https');

	def get_Size(self):
		return self.get_query_params().get('Size')

	def set_Size(self,Size):
		self.add_query_param('Size',Size)

	def get_LibraryId(self):
		return self.get_query_params().get('LibraryId')

	def set_LibraryId(self,LibraryId):
		self.add_query_param('LibraryId',LibraryId)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_StoreName(self):
		return self.get_query_params().get('StoreName')

	def set_StoreName(self,StoreName):
		self.add_query_param('StoreName',StoreName)

	def get_Page(self):
		return self.get_query_params().get('Page')

	def set_Page(self,Page):
		self.add_query_param('Page',Page)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_FilterBy(self):
		return self.get_query_params().get('FilterBy')

	def set_FilterBy(self,FilterBy):
		self.add_query_param('FilterBy',FilterBy)

	def get_Direction(self):
		return self.get_query_params().get('Direction')

	def set_Direction(self,Direction):
		self.add_query_param('Direction',Direction)

	def get_Order(self):
		return self.get_query_params().get('Order')

	def set_Order(self,Order):
		self.add_query_param('Order',Order)