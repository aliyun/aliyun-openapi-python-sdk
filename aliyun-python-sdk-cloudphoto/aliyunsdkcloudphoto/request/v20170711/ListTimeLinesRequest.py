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
class ListTimeLinesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudPhoto', '2017-07-11', 'ListTimeLines','cloudphoto')
		self.set_protocol_type('https');

	def get_Cursor(self):
		return self.get_query_params().get('Cursor')

	def set_Cursor(self,Cursor):
		self.add_query_param('Cursor',Cursor)

	def get_PhotoSize(self):
		return self.get_query_params().get('PhotoSize')

	def set_PhotoSize(self,PhotoSize):
		self.add_query_param('PhotoSize',PhotoSize)

	def get_TimeLineCount(self):
		return self.get_query_params().get('TimeLineCount')

	def set_TimeLineCount(self,TimeLineCount):
		self.add_query_param('TimeLineCount',TimeLineCount)

	def get_LibraryId(self):
		return self.get_query_params().get('LibraryId')

	def set_LibraryId(self,LibraryId):
		self.add_query_param('LibraryId',LibraryId)

	def get_StoreName(self):
		return self.get_query_params().get('StoreName')

	def set_StoreName(self,StoreName):
		self.add_query_param('StoreName',StoreName)

	def get_TimeLineUnit(self):
		return self.get_query_params().get('TimeLineUnit')

	def set_TimeLineUnit(self,TimeLineUnit):
		self.add_query_param('TimeLineUnit',TimeLineUnit)

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