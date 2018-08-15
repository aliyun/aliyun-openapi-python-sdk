# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class ModifyCasterProgramRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'ModifyCasterProgram','live')

	def get_CasterId(self):
		return self.get_query_params().get('CasterId')

	def set_CasterId(self,CasterId):
		self.add_query_param('CasterId',CasterId)

	def get_Episodes(self):
		return self.get_query_params().get('Episodes')

	def set_Episodes(self,Episodes):
		for i in range(len(Episodes)):	
			if Episodes[i].get('ResourceId') is not None:
				self.add_query_param('Episode.' + str(i + 1) + '.ResourceId' , Episodes[i].get('ResourceId'))
			for j in range(len(Episodes[i].get('ComponentIds'))):
				if Episodes[i].get('ComponentIds')[j] is not None:
					self.add_query_param('Episode.' + str(i + 1) + '.ComponentId.'+str(j + 1), Episodes[i].get('ComponentIds')[j])
			if Episodes[i].get('SwitchType') is not None:
				self.add_query_param('Episode.' + str(i + 1) + '.SwitchType' , Episodes[i].get('SwitchType'))
			if Episodes[i].get('EpisodeType') is not None:
				self.add_query_param('Episode.' + str(i + 1) + '.EpisodeType' , Episodes[i].get('EpisodeType'))
			if Episodes[i].get('EpisodeName') is not None:
				self.add_query_param('Episode.' + str(i + 1) + '.EpisodeName' , Episodes[i].get('EpisodeName'))
			if Episodes[i].get('EndTime') is not None:
				self.add_query_param('Episode.' + str(i + 1) + '.EndTime' , Episodes[i].get('EndTime'))
			if Episodes[i].get('StartTime') is not None:
				self.add_query_param('Episode.' + str(i + 1) + '.StartTime' , Episodes[i].get('StartTime'))
			if Episodes[i].get('EpisodeId') is not None:
				self.add_query_param('Episode.' + str(i + 1) + '.EpisodeId' , Episodes[i].get('EpisodeId'))


	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)