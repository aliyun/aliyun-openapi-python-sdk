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
class EchoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Actiontrail', '2017-12-04', 'Echo','actiontrail')

	def get_StartLoggingTime(self):
		return self.get_query_params().get('StartLoggingTime')

	def set_StartLoggingTime(self,StartLoggingTime):
		self.add_query_param('StartLoggingTime',StartLoggingTime)

	def get_KeyPrefix(self):
		return self.get_query_params().get('KeyPrefix')

	def set_KeyPrefix(self,KeyPrefix):
		self.add_query_param('KeyPrefix',KeyPrefix)

	def get_Format(self):
		return self.get_query_params().get('Format')

	def set_Format(self,Format):
		self.add_query_param('Format',Format)

	def get_LatestDeliveryError(self):
		return self.get_query_params().get('LatestDeliveryError')

	def set_LatestDeliveryError(self,LatestDeliveryError):
		self.add_query_param('LatestDeliveryError',LatestDeliveryError)

	def get_IsLogging(self):
		return self.get_query_params().get('IsLogging')

	def set_IsLogging(self,IsLogging):
		self.add_query_param('IsLogging',IsLogging)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_Version(self):
		return self.get_query_params().get('Version')

	def set_Version(self,Version):
		self.add_query_param('Version',Version)

	def get_LatestDeliveryTime(self):
		return self.get_query_params().get('LatestDeliveryTime')

	def set_LatestDeliveryTime(self,LatestDeliveryTime):
		self.add_query_param('LatestDeliveryTime',LatestDeliveryTime)

	def get_Help(self):
		return self.get_query_params().get('Help')

	def set_Help(self,Help):
		self.add_query_param('Help',Help)

	def get_BucketName(self):
		return self.get_query_params().get('BucketName')

	def set_BucketName(self,BucketName):
		self.add_query_param('BucketName',BucketName)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_StopLoggingTime(self):
		return self.get_query_params().get('StopLoggingTime')

	def set_StopLoggingTime(self,StopLoggingTime):
		self.add_query_param('StopLoggingTime',StopLoggingTime)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)