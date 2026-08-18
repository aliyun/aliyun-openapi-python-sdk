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
from aliyunsdkresourcemanager.endpoint import endpoint_data

class UpdateAssociatedTransferSettingRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ResourceManager', '2020-03-31', 'UpdateAssociatedTransferSetting','resourcemanager')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RuleSettings(self): # Array
		return self.get_query_params().get('RuleSettings')

	def set_RuleSettings(self, RuleSettings):  # Array
		for index1, value1 in enumerate(RuleSettings):
			if value1.get('AssociatedService') is not None:
				self.add_query_param('RuleSettings.' + str(index1 + 1) + '.AssociatedService', value1.get('AssociatedService'))
			if value1.get('MasterService') is not None:
				self.add_query_param('RuleSettings.' + str(index1 + 1) + '.MasterService', value1.get('MasterService'))
			if value1.get('MasterResourceType') is not None:
				self.add_query_param('RuleSettings.' + str(index1 + 1) + '.MasterResourceType', value1.get('MasterResourceType'))
			if value1.get('AssociatedResourceType') is not None:
				self.add_query_param('RuleSettings.' + str(index1 + 1) + '.AssociatedResourceType', value1.get('AssociatedResourceType'))
			if value1.get('RuleId') is not None:
				self.add_query_param('RuleSettings.' + str(index1 + 1) + '.RuleId', value1.get('RuleId'))
			if value1.get('Status') is not None:
				self.add_query_param('RuleSettings.' + str(index1 + 1) + '.Status', value1.get('Status'))
	def get_EnableExistingResourcesTransfer(self): # String
		return self.get_query_params().get('EnableExistingResourcesTransfer')

	def set_EnableExistingResourcesTransfer(self, EnableExistingResourcesTransfer):  # String
		self.add_query_param('EnableExistingResourcesTransfer', EnableExistingResourcesTransfer)
