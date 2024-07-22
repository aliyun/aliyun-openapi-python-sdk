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
from aliyunsdkcomputenest.endpoint import endpoint_data

class CreateServiceInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ComputeNest', '2021-06-01', 'CreateServiceInstance','computenest')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Commodity(self): # Struct
		return self.get_query_params().get('Commodity')

	def set_Commodity(self, Commodity):  # Struct
		if Commodity.get('PayPeriod') is not None:
			self.add_query_param('Commodity.PayPeriod', Commodity.get('PayPeriod'))
		if Commodity.get('AutoPay') is not None:
			self.add_query_param('Commodity.AutoPay', Commodity.get('AutoPay'))
		if Commodity.get('AutoRenew') is not None:
			self.add_query_param('Commodity.AutoRenew', Commodity.get('AutoRenew'))
		if Commodity.get('PayPeriodUnit') is not None:
			self.add_query_param('Commodity.PayPeriodUnit', Commodity.get('PayPeriodUnit'))
	def get_ContactGroup(self): # String
		return self.get_query_params().get('ContactGroup')

	def set_ContactGroup(self, ContactGroup):  # String
		self.add_query_param('ContactGroup', ContactGroup)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_SpecificationCode(self): # String
		return self.get_query_params().get('SpecificationCode')

	def set_SpecificationCode(self, SpecificationCode):  # String
		self.add_query_param('SpecificationCode', SpecificationCode)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_ResourceAutoPay(self): # Boolean
		return self.get_query_params().get('ResourceAutoPay')

	def set_ResourceAutoPay(self, ResourceAutoPay):  # Boolean
		self.add_query_param('ResourceAutoPay', ResourceAutoPay)
	def get_EnableInstanceOps(self): # Boolean
		return self.get_query_params().get('EnableInstanceOps')

	def set_EnableInstanceOps(self, EnableInstanceOps):  # Boolean
		self.add_query_param('EnableInstanceOps', EnableInstanceOps)
	def get_TemplateName(self): # String
		return self.get_query_params().get('TemplateName')

	def set_TemplateName(self, TemplateName):  # String
		self.add_query_param('TemplateName', TemplateName)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_EnableUserPrometheus(self): # Boolean
		return self.get_query_params().get('EnableUserPrometheus')

	def set_EnableUserPrometheus(self, EnableUserPrometheus):  # Boolean
		self.add_query_param('EnableUserPrometheus', EnableUserPrometheus)
	def get_SpecificationName(self): # String
		return self.get_query_params().get('SpecificationName')

	def set_SpecificationName(self, SpecificationName):  # String
		self.add_query_param('SpecificationName', SpecificationName)
	def get_TrialType(self): # String
		return self.get_query_params().get('TrialType')

	def set_TrialType(self, TrialType):  # String
		self.add_query_param('TrialType', TrialType)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_ServiceVersion(self): # String
		return self.get_query_params().get('ServiceVersion')

	def set_ServiceVersion(self, ServiceVersion):  # String
		self.add_query_param('ServiceVersion', ServiceVersion)
	def get_ServiceId(self): # String
		return self.get_query_params().get('ServiceId')

	def set_ServiceId(self, ServiceId):  # String
		self.add_query_param('ServiceId', ServiceId)
	def get_Parameters(self): # String
		return self.get_query_params().get('Parameters')

	def set_Parameters(self, Parameters):  # String
		self.add_query_param('Parameters', Parameters)
	def get_OperationMetadata(self): # Struct
		return self.get_query_params().get('OperationMetadata')

	def set_OperationMetadata(self, OperationMetadata):  # Struct
		if OperationMetadata.get('EndTime') is not None:
			self.add_query_param('OperationMetadata.EndTime', OperationMetadata.get('EndTime'))
		if OperationMetadata.get('Resources') is not None:
			self.add_query_param('OperationMetadata.Resources', OperationMetadata.get('Resources'))
		if OperationMetadata.get('StartTime') is not None:
			self.add_query_param('OperationMetadata.StartTime', OperationMetadata.get('StartTime'))
		if OperationMetadata.get('ExtraInfo') is not None:
			self.add_query_param('OperationMetadata.ExtraInfo', OperationMetadata.get('ExtraInfo'))
		if OperationMetadata.get('ServiceInstanceId') is not None:
			self.add_query_param('OperationMetadata.ServiceInstanceId', OperationMetadata.get('ServiceInstanceId'))
