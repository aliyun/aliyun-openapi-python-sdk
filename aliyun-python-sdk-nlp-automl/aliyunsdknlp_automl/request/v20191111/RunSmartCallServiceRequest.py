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
from aliyunsdknlp_automl.endpoint import endpoint_data

class RunSmartCallServiceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'nlp-automl', '2019-11-11', 'RunSmartCallService','nlpautoml')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SessionId(self):
		return self.get_body_params().get('SessionId')

	def set_SessionId(self,SessionId):
		self.add_body_params('SessionId', SessionId)

	def get_RobotId(self):
		return self.get_body_params().get('RobotId')

	def set_RobotId(self,RobotId):
		self.add_body_params('RobotId', RobotId)

	def get_ParamContent(self):
		return self.get_body_params().get('ParamContent')

	def set_ParamContent(self,ParamContent):
		self.add_body_params('ParamContent', ParamContent)

	def get_ServiceName(self):
		return self.get_body_params().get('ServiceName')

	def set_ServiceName(self,ServiceName):
		self.add_body_params('ServiceName', ServiceName)