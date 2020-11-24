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
from aliyunsdkaliyuncvc.endpoint import endpoint_data

class SendMeetingCommandRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'aliyuncvc', '2019-10-30', 'SendMeetingCommand','aliyuncvc')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_OperatorMemberUUID(self):
		return self.get_body_params().get('OperatorMemberUUID')

	def set_OperatorMemberUUID(self,OperatorMemberUUID):
		self.add_body_params('OperatorMemberUUID', OperatorMemberUUID)

	def get_MemberUUID(self):
		return self.get_query_params().get('MemberUUID')

	def set_MemberUUID(self,MemberUUID):
		self.add_query_param('MemberUUID',MemberUUID)

	def get_SendType(self):
		return self.get_body_params().get('SendType')

	def set_SendType(self,SendType):
		self.add_body_params('SendType', SendType)

	def get_Command(self):
		return self.get_body_params().get('Command')

	def set_Command(self,Command):
		self.add_body_params('Command', Command)

	def get_MeetingUUID(self):
		return self.get_query_params().get('MeetingUUID')

	def set_MeetingUUID(self,MeetingUUID):
		self.add_query_param('MeetingUUID',MeetingUUID)