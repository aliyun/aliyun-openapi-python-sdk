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

class CreateOrUpdateAlertRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'CreateOrUpdateAlertRule','arms')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AlertGroup(self): # Long
		return self.get_body_params().get('AlertGroup')

	def set_AlertGroup(self, AlertGroup):  # Long
		self.add_body_params('AlertGroup', AlertGroup)
	def get_AlertName(self): # String
		return self.get_body_params().get('AlertName')

	def set_AlertName(self, AlertName):  # String
		self.add_body_params('AlertName', AlertName)
	def get_AlertStatus(self): # String
		return self.get_body_params().get('AlertStatus')

	def set_AlertStatus(self, AlertStatus):  # String
		self.add_body_params('AlertStatus', AlertStatus)
	def get_Annotations(self): # String
		return self.get_body_params().get('Annotations')

	def set_Annotations(self, Annotations):  # String
		self.add_body_params('Annotations', Annotations)
	def get_DataConfig(self): # String
		return self.get_body_params().get('DataConfig')

	def set_DataConfig(self, DataConfig):  # String
		self.add_body_params('DataConfig', DataConfig)
	def get_Duration(self): # Long
		return self.get_body_params().get('Duration')

	def set_Duration(self, Duration):  # Long
		self.add_body_params('Duration', Duration)
	def get_AutoAddTargetConfig(self): # String
		return self.get_body_params().get('AutoAddTargetConfig')

	def set_AutoAddTargetConfig(self, AutoAddTargetConfig):  # String
		self.add_body_params('AutoAddTargetConfig', AutoAddTargetConfig)
	def get_MetricsKey(self): # String
		return self.get_body_params().get('MetricsKey')

	def set_MetricsKey(self, MetricsKey):  # String
		self.add_body_params('MetricsKey', MetricsKey)
	def get_AlertPiplines(self): # String
		return self.get_body_params().get('AlertPiplines')

	def set_AlertPiplines(self, AlertPiplines):  # String
		self.add_body_params('AlertPiplines', AlertPiplines)
	def get_MarkTagss(self): # RepeatList
		return self.get_body_params().get('MarkTags')

	def set_MarkTagss(self, MarkTags):  # RepeatList
		for depth1 in range(len(MarkTags)):
			if MarkTags[depth1].get('Value') is not None:
				self.add_body_params('MarkTags.' + str(depth1 + 1) + '.Value', MarkTags[depth1].get('Value'))
			if MarkTags[depth1].get('Key') is not None:
				self.add_body_params('MarkTags.' + str(depth1 + 1) + '.Key', MarkTags[depth1].get('Key'))
	def get_Notice(self): # String
		return self.get_body_params().get('Notice')

	def set_Notice(self, Notice):  # String
		self.add_body_params('Notice', Notice)
	def get_AlertRuleContent(self): # String
		return self.get_body_params().get('AlertRuleContent')

	def set_AlertRuleContent(self, AlertRuleContent):  # String
		self.add_body_params('AlertRuleContent', AlertRuleContent)
	def get_PromQL(self): # String
		return self.get_body_params().get('PromQL')

	def set_PromQL(self, PromQL):  # String
		self.add_body_params('PromQL', PromQL)
	def get_Product(self): # String
		return self.get_body_params().get('Product')

	def set_Product(self, Product):  # String
		self.add_body_params('Product', Product)
	def get_Level(self): # String
		return self.get_body_params().get('Level')

	def set_Level(self, Level):  # String
		self.add_body_params('Level', Level)
	def get_AutoAddNewApplication(self): # Boolean
		return self.get_body_params().get('AutoAddNewApplication')

	def set_AutoAddNewApplication(self, AutoAddNewApplication):  # Boolean
		self.add_body_params('AutoAddNewApplication', AutoAddNewApplication)
	def get_Filters(self): # String
		return self.get_body_params().get('Filters')

	def set_Filters(self, Filters):  # String
		self.add_body_params('Filters', Filters)
	def get_ClusterId(self): # String
		return self.get_body_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_body_params('ClusterId', ClusterId)
	def get_Message(self): # String
		return self.get_body_params().get('Message')

	def set_Message(self, Message):  # String
		self.add_body_params('Message', Message)
	def get_NotifyStrategy(self): # String
		return self.get_body_params().get('NotifyStrategy')

	def set_NotifyStrategy(self, NotifyStrategy):  # String
		self.add_body_params('NotifyStrategy', NotifyStrategy)
	def get_Labels(self): # String
		return self.get_body_params().get('Labels')

	def set_Labels(self, Labels):  # String
		self.add_body_params('Labels', Labels)
	def get_Tagss(self): # RepeatList
		return self.get_body_params().get('Tags')

	def set_Tagss(self, Tags):  # RepeatList
		for depth1 in range(len(Tags)):
			if Tags[depth1].get('Value') is not None:
				self.add_body_params('Tags.' + str(depth1 + 1) + '.Value', Tags[depth1].get('Value'))
			if Tags[depth1].get('Key') is not None:
				self.add_body_params('Tags.' + str(depth1 + 1) + '.Key', Tags[depth1].get('Key'))
	def get_NotifyMode(self): # String
		return self.get_body_params().get('NotifyMode')

	def set_NotifyMode(self, NotifyMode):  # String
		self.add_body_params('NotifyMode', NotifyMode)
	def get_AlertType(self): # String
		return self.get_body_params().get('AlertType')

	def set_AlertType(self, AlertType):  # String
		self.add_body_params('AlertType', AlertType)
	def get_AlertCheckType(self): # String
		return self.get_body_params().get('AlertCheckType')

	def set_AlertCheckType(self, AlertCheckType):  # String
		self.add_body_params('AlertCheckType', AlertCheckType)
	def get_MetricsType(self): # String
		return self.get_body_params().get('MetricsType')

	def set_MetricsType(self, MetricsType):  # String
		self.add_body_params('MetricsType', MetricsType)
	def get_AlertId(self): # Long
		return self.get_body_params().get('AlertId')

	def set_AlertId(self, AlertId):  # Long
		self.add_body_params('AlertId', AlertId)
	def get_Pids(self): # String
		return self.get_body_params().get('Pids')

	def set_Pids(self, Pids):  # String
		self.add_body_params('Pids', Pids)
