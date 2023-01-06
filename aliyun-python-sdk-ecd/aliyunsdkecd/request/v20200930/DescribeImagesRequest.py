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
from aliyunsdkecd.endpoint import endpoint_data

class DescribeImagesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'DescribeImages')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ImageIds(self): # RepeatList
		return self.get_query_params().get('ImageId')

	def set_ImageIds(self, ImageId):  # RepeatList
		for depth1 in range(len(ImageId)):
			self.add_query_param('ImageId.' + str(depth1 + 1), ImageId[depth1])
	def get_GpuCategory(self): # Boolean
		return self.get_query_params().get('GpuCategory')

	def set_GpuCategory(self, GpuCategory):  # Boolean
		self.add_query_param('GpuCategory', GpuCategory)
	def get_DesktopInstanceType(self): # String
		return self.get_query_params().get('DesktopInstanceType')

	def set_DesktopInstanceType(self, DesktopInstanceType):  # String
		self.add_query_param('DesktopInstanceType', DesktopInstanceType)
	def get_LanguageType(self): # String
		return self.get_query_params().get('LanguageType')

	def set_LanguageType(self, LanguageType):  # String
		self.add_query_param('LanguageType', LanguageType)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_ImageType(self): # String
		return self.get_query_params().get('ImageType')

	def set_ImageType(self, ImageType):  # String
		self.add_query_param('ImageType', ImageType)
	def get_OsType(self): # String
		return self.get_query_params().get('OsType')

	def set_OsType(self, OsType):  # String
		self.add_query_param('OsType', OsType)
	def get_ImageStatus(self): # String
		return self.get_query_params().get('ImageStatus')

	def set_ImageStatus(self, ImageStatus):  # String
		self.add_query_param('ImageStatus', ImageStatus)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
	def get_ProtocolType(self): # String
		return self.get_query_params().get('ProtocolType')

	def set_ProtocolType(self, ProtocolType):  # String
		self.add_query_param('ProtocolType', ProtocolType)
	def get_GpuDriverVersion(self): # String
		return self.get_query_params().get('GpuDriverVersion')

	def set_GpuDriverVersion(self, GpuDriverVersion):  # String
		self.add_query_param('GpuDriverVersion', GpuDriverVersion)
