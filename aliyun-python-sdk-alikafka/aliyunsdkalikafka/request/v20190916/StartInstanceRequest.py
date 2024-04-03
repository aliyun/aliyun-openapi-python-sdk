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
from aliyunsdkalikafka.endpoint import endpoint_data

class StartInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'alikafka', '2019-09-16', 'StartInstance','alikafka')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_VSwitchIdss(self): # RepeatList
		return self.get_query_params().get('VSwitchIds')

	def set_VSwitchIdss(self, VSwitchIds):  # RepeatList
		for depth1 in range(len(VSwitchIds)):
			self.add_query_param('VSwitchIds.' + str(depth1 + 1), VSwitchIds[depth1])
	def get_SelectedZones(self): # String
		return self.get_query_params().get('SelectedZones')

	def set_SelectedZones(self, SelectedZones):  # String
		self.add_query_param('SelectedZones', SelectedZones)
	def get_IsEipInner(self): # Boolean
		return self.get_query_params().get('IsEipInner')

	def set_IsEipInner(self, IsEipInner):  # Boolean
		self.add_query_param('IsEipInner', IsEipInner)
	def get_SecurityGroup(self): # String
		return self.get_query_params().get('SecurityGroup')

	def set_SecurityGroup(self, SecurityGroup):  # String
		self.add_query_param('SecurityGroup', SecurityGroup)
	def get_DeployModule(self): # String
		return self.get_query_params().get('DeployModule')

	def set_DeployModule(self, DeployModule):  # String
		self.add_query_param('DeployModule', DeployModule)
	def get_IsSetUserAndPassword(self): # Boolean
		return self.get_query_params().get('IsSetUserAndPassword')

	def set_IsSetUserAndPassword(self, IsSetUserAndPassword):  # Boolean
		self.add_query_param('IsSetUserAndPassword', IsSetUserAndPassword)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_Notifier(self): # String
		return self.get_query_params().get('Notifier')

	def set_Notifier(self, Notifier):  # String
		self.add_query_param('Notifier', Notifier)
	def get_IsForceSelectedZones(self): # Boolean
		return self.get_query_params().get('IsForceSelectedZones')

	def set_IsForceSelectedZones(self, IsForceSelectedZones):  # Boolean
		self.add_query_param('IsForceSelectedZones', IsForceSelectedZones)
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_UserPhoneNum(self): # String
		return self.get_query_params().get('UserPhoneNum')

	def set_UserPhoneNum(self, UserPhoneNum):  # String
		self.add_query_param('UserPhoneNum', UserPhoneNum)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
	def get_CrossZone(self): # Boolean
		return self.get_query_params().get('CrossZone')

	def set_CrossZone(self, CrossZone):  # Boolean
		self.add_query_param('CrossZone', CrossZone)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_ServiceVersion(self): # String
		return self.get_query_params().get('ServiceVersion')

	def set_ServiceVersion(self, ServiceVersion):  # String
		self.add_query_param('ServiceVersion', ServiceVersion)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
	def get_KMSKeyId(self): # String
		return self.get_query_params().get('KMSKeyId')

	def set_KMSKeyId(self, KMSKeyId):  # String
		self.add_query_param('KMSKeyId', KMSKeyId)
	def get_Config(self): # String
		return self.get_query_params().get('Config')

	def set_Config(self, Config):  # String
		self.add_query_param('Config', Config)
	def get_Username(self): # String
		return self.get_query_params().get('Username')

	def set_Username(self, Username):  # String
		self.add_query_param('Username', Username)
