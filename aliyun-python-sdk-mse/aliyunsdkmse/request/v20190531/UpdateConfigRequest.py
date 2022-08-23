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
from aliyunsdkmse.endpoint import endpoint_data

class UpdateConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mse', '2019-05-31', 'UpdateConfig','mse')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_OpenSuperAcl(self): # String
		return self.get_body_params().get('OpenSuperAcl')

	def set_OpenSuperAcl(self, OpenSuperAcl):  # String
		self.add_body_params('OpenSuperAcl', OpenSuperAcl)
	def get_MseSessionId(self): # String
		return self.get_query_params().get('MseSessionId')

	def set_MseSessionId(self, MseSessionId):  # String
		self.add_query_param('MseSessionId', MseSessionId)
	def get_ConfigAuthEnabled(self): # Boolean
		return self.get_query_params().get('ConfigAuthEnabled')

	def set_ConfigAuthEnabled(self, ConfigAuthEnabled):  # Boolean
		self.add_query_param('ConfigAuthEnabled', ConfigAuthEnabled)
	def get_PassWord(self): # String
		return self.get_query_params().get('PassWord')

	def set_PassWord(self, PassWord):  # String
		self.add_query_param('PassWord', PassWord)
	def get_SnapshotCount(self): # String
		return self.get_query_params().get('SnapshotCount')

	def set_SnapshotCount(self, SnapshotCount):  # String
		self.add_query_param('SnapshotCount', SnapshotCount)
	def get_MinSessionTimeout(self): # String
		return self.get_query_params().get('MinSessionTimeout')

	def set_MinSessionTimeout(self, MinSessionTimeout):  # String
		self.add_query_param('MinSessionTimeout', MinSessionTimeout)
	def get_MaxClientCnxns(self): # String
		return self.get_query_params().get('MaxClientCnxns')

	def set_MaxClientCnxns(self, MaxClientCnxns):  # String
		self.add_query_param('MaxClientCnxns', MaxClientCnxns)
	def get_RequestPars(self): # String
		return self.get_query_params().get('RequestPars')

	def set_RequestPars(self, RequestPars):  # String
		self.add_query_param('RequestPars', RequestPars)
	def get_JuteMaxbuffer(self): # String
		return self.get_query_params().get('JuteMaxbuffer')

	def set_JuteMaxbuffer(self, JuteMaxbuffer):  # String
		self.add_query_param('JuteMaxbuffer', JuteMaxbuffer)
	def get_ConfigType(self): # String
		return self.get_query_params().get('ConfigType')

	def set_ConfigType(self, ConfigType):  # String
		self.add_query_param('ConfigType', ConfigType)
	def get_AutopurgeSnapRetainCount(self): # String
		return self.get_query_params().get('AutopurgeSnapRetainCount')

	def set_AutopurgeSnapRetainCount(self, AutopurgeSnapRetainCount):  # String
		self.add_query_param('AutopurgeSnapRetainCount', AutopurgeSnapRetainCount)
	def get_MaxSessionTimeout(self): # String
		return self.get_query_params().get('MaxSessionTimeout')

	def set_MaxSessionTimeout(self, MaxSessionTimeout):  # String
		self.add_query_param('MaxSessionTimeout', MaxSessionTimeout)
	def get_ConfigSecretEnabled(self): # Boolean
		return self.get_query_params().get('ConfigSecretEnabled')

	def set_ConfigSecretEnabled(self, ConfigSecretEnabled):  # Boolean
		self.add_query_param('ConfigSecretEnabled', ConfigSecretEnabled)
	def get_MCPEnabled(self): # Boolean
		return self.get_query_params().get('MCPEnabled')

	def set_MCPEnabled(self, MCPEnabled):  # Boolean
		self.add_query_param('MCPEnabled', MCPEnabled)
	def get_TickTime(self): # String
		return self.get_query_params().get('TickTime')

	def set_TickTime(self, TickTime):  # String
		self.add_query_param('TickTime', TickTime)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_SyncLimit(self): # String
		return self.get_query_params().get('SyncLimit')

	def set_SyncLimit(self, SyncLimit):  # String
		self.add_query_param('SyncLimit', SyncLimit)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_AutopurgePurgeInterval(self): # String
		return self.get_query_params().get('AutopurgePurgeInterval')

	def set_AutopurgePurgeInterval(self, AutopurgePurgeInterval):  # String
		self.add_query_param('AutopurgePurgeInterval', AutopurgePurgeInterval)
	def get_AcceptLanguage(self): # String
		return self.get_query_params().get('AcceptLanguage')

	def set_AcceptLanguage(self, AcceptLanguage):  # String
		self.add_query_param('AcceptLanguage', AcceptLanguage)
	def get_InitLimit(self): # String
		return self.get_query_params().get('InitLimit')

	def set_InitLimit(self, InitLimit):  # String
		self.add_query_param('InitLimit', InitLimit)
	def get_UserName(self): # String
		return self.get_query_params().get('UserName')

	def set_UserName(self, UserName):  # String
		self.add_query_param('UserName', UserName)
