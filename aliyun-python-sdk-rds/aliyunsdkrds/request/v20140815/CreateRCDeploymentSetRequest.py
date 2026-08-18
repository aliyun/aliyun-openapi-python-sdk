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
from aliyunsdkrds.endpoint import endpoint_data

class CreateRCDeploymentSetRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'CreateRCDeploymentSet','rds')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_GroupCount(self): # Long
		return self.get_query_params().get('GroupCount')

	def set_GroupCount(self, GroupCount):  # Long
		self.add_query_param('GroupCount', GroupCount)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_DeploymentSetName(self): # String
		return self.get_query_params().get('DeploymentSetName')

	def set_DeploymentSetName(self, DeploymentSetName):  # String
		self.add_query_param('DeploymentSetName', DeploymentSetName)
	def get_OnUnableToRedeployFailedInstance(self): # String
		return self.get_query_params().get('OnUnableToRedeployFailedInstance')

	def set_OnUnableToRedeployFailedInstance(self, OnUnableToRedeployFailedInstance):  # String
		self.add_query_param('OnUnableToRedeployFailedInstance', OnUnableToRedeployFailedInstance)
	def get_Strategy(self): # String
		return self.get_query_params().get('Strategy')

	def set_Strategy(self, Strategy):  # String
		self.add_query_param('Strategy', Strategy)
