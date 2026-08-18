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

class CreateEnsRouteEntryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'CreateEnsRouteEntry','ens')
		self.set_method('POST')

	def get_RouteEntryName(self): # String
		return self.get_query_params().get('RouteEntryName')

	def set_RouteEntryName(self, RouteEntryName):  # String
		self.add_query_param('RouteEntryName', RouteEntryName)
	def get_NextHopId(self): # String
		return self.get_query_params().get('NextHopId')

	def set_NextHopId(self, NextHopId):  # String
		self.add_query_param('NextHopId', NextHopId)
	def get_NextHopType(self): # String
		return self.get_query_params().get('NextHopType')

	def set_NextHopType(self, NextHopType):  # String
		self.add_query_param('NextHopType', NextHopType)
	def get_RouteTableId(self): # String
		return self.get_query_params().get('RouteTableId')

	def set_RouteTableId(self, RouteTableId):  # String
		self.add_query_param('RouteTableId', RouteTableId)
	def get_DestinationCidrBlock(self): # String
		return self.get_query_params().get('DestinationCidrBlock')

	def set_DestinationCidrBlock(self, DestinationCidrBlock):  # String
		self.add_query_param('DestinationCidrBlock', DestinationCidrBlock)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_SourceCidrBlock(self): # String
		return self.get_query_params().get('SourceCidrBlock')

	def set_SourceCidrBlock(self, SourceCidrBlock):  # String
		self.add_query_param('SourceCidrBlock', SourceCidrBlock)
