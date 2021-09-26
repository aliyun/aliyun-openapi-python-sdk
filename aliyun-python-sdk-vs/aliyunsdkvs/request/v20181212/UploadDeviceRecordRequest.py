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

class UploadDeviceRecordRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vs', '2018-12-12', 'UploadDeviceRecord','vs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SearchCriteria(self):
		return self.get_query_params().get('SearchCriteria')

	def set_SearchCriteria(self,SearchCriteria):
		self.add_query_param('SearchCriteria',SearchCriteria)

	def get_UploadParams(self):
		return self.get_query_params().get('UploadParams')

	def set_UploadParams(self,UploadParams):
		self.add_query_param('UploadParams',UploadParams)

	def get_StreamId(self):
		return self.get_query_params().get('StreamId')

	def set_StreamId(self,StreamId):
		self.add_query_param('StreamId',StreamId)

	def get_UploadId(self):
		return self.get_query_params().get('UploadId')

	def set_UploadId(self,UploadId):
		self.add_query_param('UploadId',UploadId)

	def get_UploadType(self):
		return self.get_query_params().get('UploadType')

	def set_UploadType(self,UploadType):
		self.add_query_param('UploadType',UploadType)

	def get_UploadMode(self):
		return self.get_query_params().get('UploadMode')

	def set_UploadMode(self,UploadMode):
		self.add_query_param('UploadMode',UploadMode)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_DeviceId(self):
		return self.get_query_params().get('DeviceId')

	def set_DeviceId(self,DeviceId):
		self.add_query_param('DeviceId',DeviceId)