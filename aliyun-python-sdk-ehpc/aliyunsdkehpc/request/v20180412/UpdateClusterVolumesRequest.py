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
from aliyunsdkehpc.endpoint import endpoint_data

class UpdateClusterVolumesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2018-04-12', 'UpdateClusterVolumes','ehs')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AdditionalVolumess(self):
		return self.get_query_params().get('AdditionalVolumess')

	def set_AdditionalVolumess(self,AdditionalVolumess):
		for i in range(len(AdditionalVolumess)):	
			if AdditionalVolumess[i].get('VolumeType') is not None:
				self.add_query_param('AdditionalVolumes.' + str(i + 1) + '.VolumeType' , AdditionalVolumess[i].get('VolumeType'))
			if AdditionalVolumess[i].get('VolumeProtocol') is not None:
				self.add_query_param('AdditionalVolumes.' + str(i + 1) + '.VolumeProtocol' , AdditionalVolumess[i].get('VolumeProtocol'))
			if AdditionalVolumess[i].get('LocalDirectory') is not None:
				self.add_query_param('AdditionalVolumes.' + str(i + 1) + '.LocalDirectory' , AdditionalVolumess[i].get('LocalDirectory'))
			if AdditionalVolumess[i].get('RemoteDirectory') is not None:
				self.add_query_param('AdditionalVolumes.' + str(i + 1) + '.RemoteDirectory' , AdditionalVolumess[i].get('RemoteDirectory'))
			for j in range(len(AdditionalVolumess[i].get('Roless'))):
				if AdditionalVolumess[i].get('Roless')[j] is not None:
					if AdditionalVolumess[i].get('Roless')[j].get('Name') is not None:
						self.add_query_param('AdditionalVolumes.' + str(i + 1) + '.Roles.'+str(j + 1)+ '.Name', AdditionalVolumess[i].get('Roless')[j].get('Name'))
			if AdditionalVolumess[i].get('VolumeId') is not None:
				self.add_query_param('AdditionalVolumes.' + str(i + 1) + '.VolumeId' , AdditionalVolumess[i].get('VolumeId'))
			if AdditionalVolumess[i].get('VolumeMountpoint') is not None:
				self.add_query_param('AdditionalVolumes.' + str(i + 1) + '.VolumeMountpoint' , AdditionalVolumess[i].get('VolumeMountpoint'))
			if AdditionalVolumess[i].get('Location') is not None:
				self.add_query_param('AdditionalVolumes.' + str(i + 1) + '.Location' , AdditionalVolumess[i].get('Location'))
			if AdditionalVolumess[i].get('JobQueue') is not None:
				self.add_query_param('AdditionalVolumes.' + str(i + 1) + '.JobQueue' , AdditionalVolumess[i].get('JobQueue'))


	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)