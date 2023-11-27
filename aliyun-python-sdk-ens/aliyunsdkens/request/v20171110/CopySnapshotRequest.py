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

class CopySnapshotRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'CopySnapshot','ens')
		self.set_method('POST')

	def get_SnapshotId(self): # String
		return self.get_query_params().get('SnapshotId')

	def set_SnapshotId(self, SnapshotId):  # String
		self.add_query_param('SnapshotId', SnapshotId)
	def get_DestinationRegionIds(self): # Array
		return self.get_query_params().get('DestinationRegionIds')

	def set_DestinationRegionIds(self, DestinationRegionIds):  # Array
		self.add_query_param("DestinationRegionIds", json.dumps(DestinationRegionIds))
	def get_DestinationSnapshotName(self): # String
		return self.get_query_params().get('DestinationSnapshotName')

	def set_DestinationSnapshotName(self, DestinationSnapshotName):  # String
		self.add_query_param('DestinationSnapshotName', DestinationSnapshotName)
	def get_DestinationSnapshotDescription(self): # String
		return self.get_query_params().get('DestinationSnapshotDescription')

	def set_DestinationSnapshotDescription(self, DestinationSnapshotDescription):  # String
		self.add_query_param('DestinationSnapshotDescription', DestinationSnapshotDescription)
