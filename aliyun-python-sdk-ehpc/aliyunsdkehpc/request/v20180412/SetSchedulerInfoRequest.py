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

class SetSchedulerInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2018-04-12', 'SetSchedulerInfo')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SlurmInfos(self): # RepeatList
		return self.get_query_params().get('SlurmInfo')

	def set_SlurmInfos(self, SlurmInfo):  # RepeatList
		for depth1 in range(len(SlurmInfo)):
			if SlurmInfo[depth1].get('SchedInterval') is not None:
				self.add_query_param('SlurmInfo.' + str(depth1 + 1) + '.SchedInterval', SlurmInfo[depth1].get('SchedInterval'))
			if SlurmInfo[depth1].get('BackfillInterval') is not None:
				self.add_query_param('SlurmInfo.' + str(depth1 + 1) + '.BackfillInterval', SlurmInfo[depth1].get('BackfillInterval'))
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_Schedulers(self): # RepeatList
		return self.get_query_params().get('Scheduler')

	def set_Schedulers(self, Scheduler):  # RepeatList
		for depth1 in range(len(Scheduler)):
			if Scheduler[depth1].get('SchedName') is not None:
				self.add_query_param('Scheduler.' + str(depth1 + 1) + '.SchedName', Scheduler[depth1].get('SchedName'))
	def get_PbsInfos(self): # RepeatList
		return self.get_query_params().get('PbsInfo')

	def set_PbsInfos(self, PbsInfo):  # RepeatList
		for depth1 in range(len(PbsInfo)):
			if PbsInfo[depth1].get('SchedInterval') is not None:
				self.add_query_param('PbsInfo.' + str(depth1 + 1) + '.SchedInterval', PbsInfo[depth1].get('SchedInterval'))
			if PbsInfo[depth1].get('SchedMaxJobs') is not None:
				self.add_query_param('PbsInfo.' + str(depth1 + 1) + '.SchedMaxJobs', PbsInfo[depth1].get('SchedMaxJobs'))
			if PbsInfo[depth1].get('AclLimit') is not None:
				for depth2 in range(len(PbsInfo[depth1].get('AclLimit'))):
					if PbsInfo[depth1].get('AclLimit')[depth2].get('AclUsers') is not None:
						self.add_query_param('PbsInfo.' + str(depth1 + 1) + '.AclLimit.'  + str(depth2 + 1) + '.AclUsers', PbsInfo[depth1].get('AclLimit')[depth2].get('AclUsers'))
					if PbsInfo[depth1].get('AclLimit')[depth2].get('Queue') is not None:
						self.add_query_param('PbsInfo.' + str(depth1 + 1) + '.AclLimit.'  + str(depth2 + 1) + '.Queue', PbsInfo[depth1].get('AclLimit')[depth2].get('Queue'))
			if PbsInfo[depth1].get('ResourceLimit') is not None:
				for depth2 in range(len(PbsInfo[depth1].get('ResourceLimit'))):
					if PbsInfo[depth1].get('ResourceLimit')[depth2].get('MaxJobs') is not None:
						self.add_query_param('PbsInfo.' + str(depth1 + 1) + '.ResourceLimit.'  + str(depth2 + 1) + '.MaxJobs', PbsInfo[depth1].get('ResourceLimit')[depth2].get('MaxJobs'))
					if PbsInfo[depth1].get('ResourceLimit')[depth2].get('Nodes') is not None:
						self.add_query_param('PbsInfo.' + str(depth1 + 1) + '.ResourceLimit.'  + str(depth2 + 1) + '.Nodes', PbsInfo[depth1].get('ResourceLimit')[depth2].get('Nodes'))
					if PbsInfo[depth1].get('ResourceLimit')[depth2].get('Mem') is not None:
						self.add_query_param('PbsInfo.' + str(depth1 + 1) + '.ResourceLimit.'  + str(depth2 + 1) + '.Mem', PbsInfo[depth1].get('ResourceLimit')[depth2].get('Mem'))
					if PbsInfo[depth1].get('ResourceLimit')[depth2].get('Cpus') is not None:
						self.add_query_param('PbsInfo.' + str(depth1 + 1) + '.ResourceLimit.'  + str(depth2 + 1) + '.Cpus', PbsInfo[depth1].get('ResourceLimit')[depth2].get('Cpus'))
					if PbsInfo[depth1].get('ResourceLimit')[depth2].get('User') is not None:
						self.add_query_param('PbsInfo.' + str(depth1 + 1) + '.ResourceLimit.'  + str(depth2 + 1) + '.User', PbsInfo[depth1].get('ResourceLimit')[depth2].get('User'))
					if PbsInfo[depth1].get('ResourceLimit')[depth2].get('Queue') is not None:
						self.add_query_param('PbsInfo.' + str(depth1 + 1) + '.ResourceLimit.'  + str(depth2 + 1) + '.Queue', PbsInfo[depth1].get('ResourceLimit')[depth2].get('Queue'))
			if PbsInfo[depth1].get('SchedMaxQueuedJobs') is not None:
				self.add_query_param('PbsInfo.' + str(depth1 + 1) + '.SchedMaxQueuedJobs', PbsInfo[depth1].get('SchedMaxQueuedJobs'))
			if PbsInfo[depth1].get('JobHistoryDuration') is not None:
				self.add_query_param('PbsInfo.' + str(depth1 + 1) + '.JobHistoryDuration', PbsInfo[depth1].get('JobHistoryDuration'))
