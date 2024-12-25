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
import json

class DescribeInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'DescribeInstances','ens')
		self.set_method('POST')

	def get_ServiceStatus(self): # Array
		return self.get_query_params().get('ServiceStatus')

	def set_ServiceStatus(self, ServiceStatus):  # Array
		self.add_query_param("ServiceStatus", json.dumps(ServiceStatus))
	def get_OrderByParams(self): # String
		return self.get_query_params().get('OrderByParams')

	def set_OrderByParams(self, OrderByParams):  # String
		self.add_query_param('OrderByParams', OrderByParams)
	def get_EnsRegionId(self): # String
		return self.get_query_params().get('EnsRegionId')

	def set_EnsRegionId(self, EnsRegionId):  # String
		self.add_query_param('EnsRegionId', EnsRegionId)
	def get_InstanceResourceType(self): # String
		return self.get_query_params().get('InstanceResourceType')

	def set_InstanceResourceType(self, InstanceResourceType):  # String
		self.add_query_param('InstanceResourceType', InstanceResourceType)
	def get_EnsServiceId(self): # String
		return self.get_query_params().get('EnsServiceId')

	def set_EnsServiceId(self, EnsServiceId):  # String
		self.add_query_param('EnsServiceId', EnsServiceId)
	def get_Tags(self): # Array
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):  # Array
		self.add_query_param("Tags", json.dumps(Tags))
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_InstanceName(self): # String
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self, InstanceName):  # String
		self.add_query_param('InstanceName', InstanceName)
	def get_InstanceIds(self): # String
		return self.get_query_params().get('InstanceIds')

	def set_InstanceIds(self, InstanceIds):  # String
		self.add_query_param('InstanceIds', InstanceIds)
	def get_NetworkId(self): # String
		return self.get_query_params().get('NetworkId')

	def set_NetworkId(self, NetworkId):  # String
		self.add_query_param('NetworkId', NetworkId)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
	def get_IntranetIp(self): # String
		return self.get_query_params().get('IntranetIp')

	def set_IntranetIp(self, IntranetIp):  # String
		self.add_query_param('IntranetIp', IntranetIp)
	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
	def get_SecurityGroupId(self): # String
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self, SecurityGroupId):  # String
		self.add_query_param('SecurityGroupId', SecurityGroupId)
	def get_SearchKey(self): # String
		return self.get_query_params().get('SearchKey')

	def set_SearchKey(self, SearchKey):  # String
		self.add_query_param('SearchKey', SearchKey)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_PageSize(self): # String
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # String
		self.add_query_param('PageSize', PageSize)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
	def get_EnsRegionIds(self): # String
		return self.get_query_params().get('EnsRegionIds')

	def set_EnsRegionIds(self, EnsRegionIds):  # String
		self.add_query_param('EnsRegionIds', EnsRegionIds)
