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

from aliyunsdkcore.request import RoaRequest

class PostDataRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Metering', '2020-09-21', 'PostData','pai')
		self.set_uri_pattern('/api/dataPost')
		self.set_method('POST')

	def get_InstanceId(self):
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_body_params('InstanceId', InstanceId)

	def get_Data(self):
		return self.get_body_params().get('Data')

	def set_Data(self,Data):
		self.add_body_params('Data', Data)

	def get_DataType(self):
		return self.get_body_params().get('DataType')

	def set_DataType(self,DataType):
		self.add_body_params('DataType', DataType)

	def get_EndTime(self):
		return self.get_body_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_body_params('EndTime', EndTime)

	def get_StartTime(self):
		return self.get_body_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_body_params('StartTime', StartTime)

	def get_CommodityCode(self):
		return self.get_body_params().get('CommodityCode')

	def set_CommodityCode(self,CommodityCode):
		self.add_body_params('CommodityCode', CommodityCode)

	def get_Region(self):
		return self.get_body_params().get('Region')

	def set_Region(self,Region):
		self.add_body_params('Region', Region)

	def get_UserId(self):
		return self.get_body_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_body_params('UserId', UserId)