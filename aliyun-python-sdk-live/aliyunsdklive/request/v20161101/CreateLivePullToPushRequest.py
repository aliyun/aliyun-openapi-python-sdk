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
from aliyunsdklive.endpoint import endpoint_data
import json

class CreateLivePullToPushRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'CreateLivePullToPush','live')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_FileIndex(self): # Integer
		return self.get_query_params().get('FileIndex')

	def set_FileIndex(self, FileIndex):  # Integer
		self.add_query_param('FileIndex', FileIndex)
	def get_RetryCount(self): # Integer
		return self.get_query_params().get('RetryCount')

	def set_RetryCount(self, RetryCount):  # Integer
		self.add_query_param('RetryCount', RetryCount)
	def get_TaskName(self): # String
		return self.get_query_params().get('TaskName')

	def set_TaskName(self, TaskName):  # String
		self.add_query_param('TaskName', TaskName)
	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
	def get_RepeatNumber(self): # Integer
		return self.get_query_params().get('RepeatNumber')

	def set_RepeatNumber(self, RepeatNumber):  # Integer
		self.add_query_param('RepeatNumber', RepeatNumber)
	def get_SourceProtocol(self): # String
		return self.get_query_params().get('SourceProtocol')

	def set_SourceProtocol(self, SourceProtocol):  # String
		self.add_query_param('SourceProtocol', SourceProtocol)
	def get_SourceType(self): # String
		return self.get_query_params().get('SourceType')

	def set_SourceType(self, SourceType):  # String
		self.add_query_param('SourceType', SourceType)
	def get_Offset(self): # Integer
		return self.get_query_params().get('Offset')

	def set_Offset(self, Offset):  # Integer
		self.add_query_param('Offset', Offset)
	def get_DstUrl(self): # String
		return self.get_query_params().get('DstUrl')

	def set_DstUrl(self, DstUrl):  # String
		self.add_query_param('DstUrl', DstUrl)
	def get_EndTime(self): # String
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_query_param('EndTime', EndTime)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_SourceUrls(self): # Array
		return self.get_query_params().get('SourceUrls')

	def set_SourceUrls(self, SourceUrls):  # Array
		self.add_query_param("SourceUrls", json.dumps(SourceUrls))
	def get_RetryInterval(self): # Integer
		return self.get_query_params().get('RetryInterval')

	def set_RetryInterval(self, RetryInterval):  # Integer
		self.add_query_param('RetryInterval', RetryInterval)
	def get_CallbackUrl(self): # String
		return self.get_query_params().get('CallbackUrl')

	def set_CallbackUrl(self, CallbackUrl):  # String
		self.add_query_param('CallbackUrl', CallbackUrl)
	def get_Region(self): # String
		return self.get_query_params().get('Region')

	def set_Region(self, Region):  # String
		self.add_query_param('Region', Region)
