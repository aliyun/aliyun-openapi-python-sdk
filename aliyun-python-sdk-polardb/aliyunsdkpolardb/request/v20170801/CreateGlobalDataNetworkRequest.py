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
from aliyunsdkpolardb.endpoint import endpoint_data

class CreateGlobalDataNetworkRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardb', '2017-08-01', 'CreateGlobalDataNetwork','polardb')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DestinationType(self): # String
		return self.get_query_params().get('DestinationType')

	def set_DestinationType(self, DestinationType):  # String
		self.add_query_param('DestinationType', DestinationType)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_SourceType(self): # String
		return self.get_query_params().get('SourceType')

	def set_SourceType(self, SourceType):  # String
		self.add_query_param('SourceType', SourceType)
	def get_FreezeSourceDuringSync(self): # String
		return self.get_query_params().get('FreezeSourceDuringSync')

	def set_FreezeSourceDuringSync(self, FreezeSourceDuringSync):  # String
		self.add_query_param('FreezeSourceDuringSync', FreezeSourceDuringSync)
	def get_SourceId(self): # String
		return self.get_query_params().get('SourceId')

	def set_SourceId(self, SourceId):  # String
		self.add_query_param('SourceId', SourceId)
	def get_DestinationRegion(self): # String
		return self.get_query_params().get('DestinationRegion')

	def set_DestinationRegion(self, DestinationRegion):  # String
		self.add_query_param('DestinationRegion', DestinationRegion)
	def get_DestinationId(self): # String
		return self.get_query_params().get('DestinationId')

	def set_DestinationId(self, DestinationId):  # String
		self.add_query_param('DestinationId', DestinationId)
	def get_SourceFileSystemPath(self): # String
		return self.get_query_params().get('SourceFileSystemPath')

	def set_SourceFileSystemPath(self, SourceFileSystemPath):  # String
		self.add_query_param('SourceFileSystemPath', SourceFileSystemPath)
	def get_DestinationFileSystemPath(self): # String
		return self.get_query_params().get('DestinationFileSystemPath')

	def set_DestinationFileSystemPath(self, DestinationFileSystemPath):  # String
		self.add_query_param('DestinationFileSystemPath', DestinationFileSystemPath)
	def get_SourceRegion(self): # String
		return self.get_query_params().get('SourceRegion')

	def set_SourceRegion(self, SourceRegion):  # String
		self.add_query_param('SourceRegion', SourceRegion)
