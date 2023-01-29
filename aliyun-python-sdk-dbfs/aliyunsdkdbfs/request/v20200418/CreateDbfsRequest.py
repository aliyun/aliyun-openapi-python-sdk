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
from aliyunsdkdbfs.endpoint import endpoint_data

class CreateDbfsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DBFS', '2020-04-18', 'CreateDbfs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SizeG(self): # Integer
		return self.get_query_params().get('SizeG')

	def set_SizeG(self, SizeG):  # Integer
		self.add_query_param('SizeG', SizeG)
	def get_SnapshotId(self): # String
		return self.get_query_params().get('SnapshotId')

	def set_SnapshotId(self, SnapshotId):  # String
		self.add_query_param('SnapshotId', SnapshotId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_UsedScene(self): # String
		return self.get_query_params().get('UsedScene')

	def set_UsedScene(self, UsedScene):  # String
		self.add_query_param('UsedScene', UsedScene)
	def get_FsName(self): # String
		return self.get_query_params().get('FsName')

	def set_FsName(self, FsName):  # String
		self.add_query_param('FsName', FsName)
	def get_RaidStripeUnitNumber(self): # Integer
		return self.get_query_params().get('RaidStripeUnitNumber')

	def set_RaidStripeUnitNumber(self, RaidStripeUnitNumber):  # Integer
		self.add_query_param('RaidStripeUnitNumber', RaidStripeUnitNumber)
	def get_Encryption(self): # Boolean
		return self.get_query_params().get('Encryption')

	def set_Encryption(self, Encryption):  # Boolean
		self.add_query_param('Encryption', Encryption)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
	def get_AdvancedFeatures(self): # String
		return self.get_query_params().get('AdvancedFeatures')

	def set_AdvancedFeatures(self, AdvancedFeatures):  # String
		self.add_query_param('AdvancedFeatures', AdvancedFeatures)
	def get_PerformanceLevel(self): # String
		return self.get_query_params().get('PerformanceLevel')

	def set_PerformanceLevel(self, PerformanceLevel):  # String
		self.add_query_param('PerformanceLevel', PerformanceLevel)
	def get_EnableRaid(self): # Boolean
		return self.get_query_params().get('EnableRaid')

	def set_EnableRaid(self, EnableRaid):  # Boolean
		self.add_query_param('EnableRaid', EnableRaid)
	def get_DeleteSnapshot(self): # Boolean
		return self.get_query_params().get('DeleteSnapshot')

	def set_DeleteSnapshot(self, DeleteSnapshot):  # Boolean
		self.add_query_param('DeleteSnapshot', DeleteSnapshot)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
	def get_Category(self): # String
		return self.get_query_params().get('Category')

	def set_Category(self, Category):  # String
		self.add_query_param('Category', Category)
	def get_KMSKeyId(self): # String
		return self.get_query_params().get('KMSKeyId')

	def set_KMSKeyId(self, KMSKeyId):  # String
		self.add_query_param('KMSKeyId', KMSKeyId)
