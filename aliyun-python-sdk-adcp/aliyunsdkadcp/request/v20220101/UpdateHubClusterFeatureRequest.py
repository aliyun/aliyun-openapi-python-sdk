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
from aliyunsdkadcp.endpoint import endpoint_data
import json

class UpdateHubClusterFeatureRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'adcp', '2022-01-01', 'UpdateHubClusterFeature','adcp')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AccessControlList(self): # Array
		return self.get_query_params().get('AccessControlList')

	def set_AccessControlList(self, AccessControlList):  # Array
		self.add_query_param("AccessControlList", json.dumps(AccessControlList))
	def get_MonitorEnabled(self): # Boolean
		return self.get_query_params().get('MonitorEnabled')

	def set_MonitorEnabled(self, MonitorEnabled):  # Boolean
		self.add_query_param('MonitorEnabled', MonitorEnabled)
	def get_DeletionProtection(self): # Boolean
		return self.get_query_params().get('DeletionProtection')

	def set_DeletionProtection(self, DeletionProtection):  # Boolean
		self.add_query_param('DeletionProtection', DeletionProtection)
	def get_EnableMesh(self): # Boolean
		return self.get_query_params().get('EnableMesh')

	def set_EnableMesh(self, EnableMesh):  # Boolean
		self.add_query_param('EnableMesh', EnableMesh)
	def get_ArgoCDHAEnabled(self): # Boolean
		return self.get_query_params().get('ArgoCDHAEnabled')

	def set_ArgoCDHAEnabled(self, ArgoCDHAEnabled):  # Boolean
		self.add_query_param('ArgoCDHAEnabled', ArgoCDHAEnabled)
	def get_ArgoCDEnabled(self): # Boolean
		return self.get_query_params().get('ArgoCDEnabled')

	def set_ArgoCDEnabled(self, ArgoCDEnabled):  # Boolean
		self.add_query_param('ArgoCDEnabled', ArgoCDEnabled)
	def get_VSwitches(self): # Array
		return self.get_query_params().get('VSwitches')

	def set_VSwitches(self, VSwitches):  # Array
		self.add_query_param("VSwitches", json.dumps(VSwitches))
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_PublicAccessEnabled(self): # Boolean
		return self.get_query_params().get('PublicAccessEnabled')

	def set_PublicAccessEnabled(self, PublicAccessEnabled):  # Boolean
		self.add_query_param('PublicAccessEnabled', PublicAccessEnabled)
	def get_PublicApiServerEnabled(self): # Boolean
		return self.get_query_params().get('PublicApiServerEnabled')

	def set_PublicApiServerEnabled(self, PublicApiServerEnabled):  # Boolean
		self.add_query_param('PublicApiServerEnabled', PublicApiServerEnabled)
	def get_ArgoServerEnabled(self): # Boolean
		return self.get_query_params().get('ArgoServerEnabled')

	def set_ArgoServerEnabled(self, ArgoServerEnabled):  # Boolean
		self.add_query_param('ArgoServerEnabled', ArgoServerEnabled)
	def get_WorkflowScheduleMode(self): # String
		return self.get_query_params().get('WorkflowScheduleMode')

	def set_WorkflowScheduleMode(self, WorkflowScheduleMode):  # String
		self.add_query_param('WorkflowScheduleMode', WorkflowScheduleMode)
	def get_AuditLogEnabled(self): # Boolean
		return self.get_query_params().get('AuditLogEnabled')

	def set_AuditLogEnabled(self, AuditLogEnabled):  # Boolean
		self.add_query_param('AuditLogEnabled', AuditLogEnabled)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_PriceLimit(self): # String
		return self.get_query_params().get('PriceLimit')

	def set_PriceLimit(self, PriceLimit):  # String
		self.add_query_param('PriceLimit', PriceLimit)
	def get_ApiServerEipId(self): # String
		return self.get_query_params().get('ApiServerEipId')

	def set_ApiServerEipId(self, ApiServerEipId):  # String
		self.add_query_param('ApiServerEipId', ApiServerEipId)
