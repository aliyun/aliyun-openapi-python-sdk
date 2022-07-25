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
from aliyunsdkarms.endpoint import endpoint_data

class CreateOrUpdateIMRobotRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'CreateOrUpdateIMRobot','arms')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DailyNoc(self): # Boolean
		return self.get_body_params().get('DailyNoc')

	def set_DailyNoc(self, DailyNoc):  # Boolean
		self.add_body_params('DailyNoc', DailyNoc)
	def get_RobotAddress(self): # String
		return self.get_body_params().get('RobotAddress')

	def set_RobotAddress(self, RobotAddress):  # String
		self.add_body_params('RobotAddress', RobotAddress)
	def get_RobotName(self): # String
		return self.get_body_params().get('RobotName')

	def set_RobotName(self, RobotName):  # String
		self.add_body_params('RobotName', RobotName)
	def get_RobotId(self): # Long
		return self.get_body_params().get('RobotId')

	def set_RobotId(self, RobotId):  # Long
		self.add_body_params('RobotId', RobotId)
	def get_Type(self): # String
		return self.get_body_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_body_params('Type', Type)
	def get_DailyNocTime(self): # String
		return self.get_body_params().get('DailyNocTime')

	def set_DailyNocTime(self, DailyNocTime):  # String
		self.add_body_params('DailyNocTime', DailyNocTime)
	def get_Token(self): # String
		return self.get_body_params().get('Token')

	def set_Token(self, Token):  # String
		self.add_body_params('Token', Token)
	def get_CardTemplate(self): # String
		return self.get_body_params().get('CardTemplate')

	def set_CardTemplate(self, CardTemplate):  # String
		self.add_body_params('CardTemplate', CardTemplate)
	def get_EnableOutgoing(self): # Boolean
		return self.get_body_params().get('EnableOutgoing')

	def set_EnableOutgoing(self, EnableOutgoing):  # Boolean
		self.add_body_params('EnableOutgoing', EnableOutgoing)
