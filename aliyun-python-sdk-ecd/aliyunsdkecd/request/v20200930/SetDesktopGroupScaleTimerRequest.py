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
from aliyunsdkecd.endpoint import endpoint_data

class SetDesktopGroupScaleTimerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'SetDesktopGroupScaleTimer')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DesktopGroupId(self): # String
		return self.get_query_params().get('DesktopGroupId')

	def set_DesktopGroupId(self, DesktopGroupId):  # String
		self.add_query_param('DesktopGroupId', DesktopGroupId)
	def get_ScaleTimerInfoss(self): # RepeatList
		return self.get_query_params().get('ScaleTimerInfos')

	def set_ScaleTimerInfoss(self, ScaleTimerInfos):  # RepeatList
		for depth1 in range(len(ScaleTimerInfos)):
			if ScaleTimerInfos[depth1].get('KeepDuration') is not None:
				self.add_query_param('ScaleTimerInfos.' + str(depth1 + 1) + '.KeepDuration', ScaleTimerInfos[depth1].get('KeepDuration'))
			if ScaleTimerInfos[depth1].get('MinResAmount') is not None:
				self.add_query_param('ScaleTimerInfos.' + str(depth1 + 1) + '.MinResAmount', ScaleTimerInfos[depth1].get('MinResAmount'))
			if ScaleTimerInfos[depth1].get('Cron') is not None:
				self.add_query_param('ScaleTimerInfos.' + str(depth1 + 1) + '.Cron', ScaleTimerInfos[depth1].get('Cron'))
			if ScaleTimerInfos[depth1].get('Type') is not None:
				self.add_query_param('ScaleTimerInfos.' + str(depth1 + 1) + '.Type', ScaleTimerInfos[depth1].get('Type'))
			if ScaleTimerInfos[depth1].get('LoadPolicy') is not None:
				self.add_query_param('ScaleTimerInfos.' + str(depth1 + 1) + '.LoadPolicy', ScaleTimerInfos[depth1].get('LoadPolicy'))
			if ScaleTimerInfos[depth1].get('RatioThreshold') is not None:
				self.add_query_param('ScaleTimerInfos.' + str(depth1 + 1) + '.RatioThreshold', ScaleTimerInfos[depth1].get('RatioThreshold'))
