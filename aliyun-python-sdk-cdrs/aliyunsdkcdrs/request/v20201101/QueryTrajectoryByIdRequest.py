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

class QueryTrajectoryByIdRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CDRS', '2020-11-01', 'QueryTrajectoryById')
		self.set_method('POST')

	def get_CorpId(self):
		return self.get_body_params().get('CorpId')

	def set_CorpId(self,CorpId):
		self.add_body_params('CorpId', CorpId)

	def get_EndTime(self):
		return self.get_body_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_body_params('EndTime', EndTime)

	def get_StartTime(self):
		return self.get_body_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_body_params('StartTime', StartTime)

	def get_DeviceList(self):
		return self.get_body_params().get('DeviceList')

	def set_DeviceList(self, DeviceLists):
		for depth1 in range(len(DeviceLists)):
			if DeviceLists[depth1].get('DeviceId') is not None:
				self.add_body_params('DeviceList.' + str(depth1 + 1) + '.DeviceId', DeviceLists[depth1].get('DeviceId'))

	def get_IdList(self):
		return self.get_body_params().get('IdList')

	def set_IdList(self, IdLists):
		for depth1 in range(len(IdLists)):
			if IdLists[depth1].get('IdType') is not None:
				self.add_body_params('IdList.' + str(depth1 + 1) + '.IdType', IdLists[depth1].get('IdType'))
			if IdLists[depth1].get('IdValue') is not None:
				self.add_body_params('IdList.' + str(depth1 + 1) + '.IdValue', IdLists[depth1].get('IdValue'))