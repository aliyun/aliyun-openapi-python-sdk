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

class UpdateUserDeliveryTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ESA', '2024-09-10', 'UpdateUserDeliveryTask')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_FieldName(self): # String
		return self.get_body_params().get('FieldName')

	def set_FieldName(self, FieldName):  # String
		self.add_body_params('FieldName', FieldName)
	def get_TaskName(self): # String
		return self.get_body_params().get('TaskName')

	def set_TaskName(self, TaskName):  # String
		self.add_body_params('TaskName', TaskName)
	def get_DiscardRate(self): # Float
		return self.get_body_params().get('DiscardRate')

	def set_DiscardRate(self, DiscardRate):  # Float
		self.add_body_params('DiscardRate', DiscardRate)
	def get_BusinessType(self): # String
		return self.get_body_params().get('BusinessType')

	def set_BusinessType(self, BusinessType):  # String
		self.add_body_params('BusinessType', BusinessType)
