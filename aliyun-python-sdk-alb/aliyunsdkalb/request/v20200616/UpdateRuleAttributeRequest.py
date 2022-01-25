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
from aliyunsdkalb.endpoint import endpoint_data

class UpdateRuleAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alb', '2020-06-16', 'UpdateRuleAttribute','alb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_RuleName(self): # String
		return self.get_query_params().get('RuleName')

	def set_RuleName(self, RuleName):  # String
		self.add_query_param('RuleName', RuleName)
	def get_RuleActions(self): # Array
		return self.get_query_params().get('RuleActions')

	def set_RuleActions(self, RuleActions):  # Array
		for index1, value1 in enumerate(RuleActions):
			if value1.get('FixedResponseConfig') is not None:
				if value1.get('FixedResponseConfig').get('HttpCode') is not None:
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.FixedResponseConfig.HttpCode', value1.get('FixedResponseConfig').get('HttpCode'))
				if value1.get('FixedResponseConfig').get('Content') is not None:
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.FixedResponseConfig.Content', value1.get('FixedResponseConfig').get('Content'))
				if value1.get('FixedResponseConfig').get('ContentType') is not None:
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.FixedResponseConfig.ContentType', value1.get('FixedResponseConfig').get('ContentType'))
			if value1.get('TrafficMirrorConfig') is not None:
				if value1.get('TrafficMirrorConfig').get('MirrorGroupConfig') is not None:
					if value1.get('TrafficMirrorConfig').get('MirrorGroupConfig').get('ServerGroupTuples') is not None:
						for index2, value2 in enumerate(value1.get('TrafficMirrorConfig').get('MirrorGroupConfig').get('ServerGroupTuples')):
							if value2.get('ServerGroupId') is not None:
								self.add_query_param('RuleActions.' + str(index1 + 1) + '.TrafficMirrorConfig.MirrorGroupConfig.ServerGroupTuples' + str(index2 + 1) + '.ServerGroupId', value2.get('ServerGroupId'))
				if value1.get('TrafficMirrorConfig').get('TargetType') is not None:
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.TrafficMirrorConfig.TargetType', value1.get('TrafficMirrorConfig').get('TargetType'))
			if value1.get('ForwardGroupConfig') is not None:
				if value1.get('ForwardGroupConfig').get('ServerGroupStickySession') is not None:
					if value1.get('ForwardGroupConfig').get('ServerGroupStickySession').get('Enabled') is not None:
						self.add_query_param('RuleActions.' + str(index1 + 1) + '.ForwardGroupConfig.ServerGroupStickySession.Enabled', value1.get('ForwardGroupConfig').get('ServerGroupStickySession').get('Enabled'))
					if value1.get('ForwardGroupConfig').get('ServerGroupStickySession').get('Timeout') is not None:
						self.add_query_param('RuleActions.' + str(index1 + 1) + '.ForwardGroupConfig.ServerGroupStickySession.Timeout', value1.get('ForwardGroupConfig').get('ServerGroupStickySession').get('Timeout'))
				if value1.get('ForwardGroupConfig').get('ServerGroupTuples') is not None:
					for index2, value2 in enumerate(value1.get('ForwardGroupConfig').get('ServerGroupTuples')):
						if value2.get('ServerGroupId') is not None:
							self.add_query_param('RuleActions.' + str(index1 + 1) + '.ForwardGroupConfig.ServerGroupTuples' + str(index2 + 1) + '.ServerGroupId', value2.get('ServerGroupId'))
						if value2.get('Weight') is not None:
							self.add_query_param('RuleActions.' + str(index1 + 1) + '.ForwardGroupConfig.ServerGroupTuples' + str(index2 + 1) + '.Weight', value2.get('Weight'))
			if value1.get('RemoveHeaderConfig') is not None:
				if value1.get('RemoveHeaderConfig').get('Key') is not None:
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.RemoveHeaderConfig.Key', value1.get('RemoveHeaderConfig').get('Key'))
			if value1.get('InsertHeaderConfig') is not None:
				if value1.get('InsertHeaderConfig').get('ValueType') is not None:
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.InsertHeaderConfig.ValueType', value1.get('InsertHeaderConfig').get('ValueType'))
				if value1.get('InsertHeaderConfig').get('CoverEnabled') is not None:
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.InsertHeaderConfig.CoverEnabled', value1.get('InsertHeaderConfig').get('CoverEnabled'))
				if value1.get('InsertHeaderConfig').get('Value') is not None:
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.InsertHeaderConfig.Value', value1.get('InsertHeaderConfig').get('Value'))
				if value1.get('InsertHeaderConfig').get('Key') is not None:
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.InsertHeaderConfig.Key', value1.get('InsertHeaderConfig').get('Key'))
			if value1.get('TrafficLimitConfig') is not None:
				if value1.get('TrafficLimitConfig').get('QPS') is not None:
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.TrafficLimitConfig.QPS', value1.get('TrafficLimitConfig').get('QPS'))
			if value1.get('CorsConfig') is not None:
				if value1.get('CorsConfig').get('AllowCredentials') is not None:
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.CorsConfig.AllowCredentials', value1.get('CorsConfig').get('AllowCredentials'))
				if value1.get('CorsConfig').get('AllowOrigin') is not None:
					for index2, value2 in enumerate(value1.get('CorsConfig').get('AllowOrigin')):
						self.add_query_param('RuleActions.' + str(index1 + 1) + '.CorsConfig.AllowOrigin' + str(index2 + 1), value2)
				if value1.get('CorsConfig').get('MaxAge') is not None:
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.CorsConfig.MaxAge', value1.get('CorsConfig').get('MaxAge'))
				if value1.get('CorsConfig').get('AllowMethods') is not None:
					for index2, value2 in enumerate(value1.get('CorsConfig').get('AllowMethods')):
						self.add_query_param('RuleActions.' + str(index1 + 1) + '.CorsConfig.AllowMethods' + str(index2 + 1), value2)
				if value1.get('CorsConfig').get('AllowHeaders') is not None:
					for index2, value2 in enumerate(value1.get('CorsConfig').get('AllowHeaders')):
						self.add_query_param('RuleActions.' + str(index1 + 1) + '.CorsConfig.AllowHeaders' + str(index2 + 1), value2)
				if value1.get('CorsConfig').get('ExposeHeaders') is not None:
					for index2, value2 in enumerate(value1.get('CorsConfig').get('ExposeHeaders')):
						self.add_query_param('RuleActions.' + str(index1 + 1) + '.CorsConfig.ExposeHeaders' + str(index2 + 1), value2)
			if value1.get('RedirectConfig') is not None:
				if value1.get('RedirectConfig').get('Path') is not None:
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.RedirectConfig.Path', value1.get('RedirectConfig').get('Path'))
				if value1.get('RedirectConfig').get('Protocol') is not None:
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.RedirectConfig.Protocol', value1.get('RedirectConfig').get('Protocol'))
				if value1.get('RedirectConfig').get('Port') is not None:
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.RedirectConfig.Port', value1.get('RedirectConfig').get('Port'))
				if value1.get('RedirectConfig').get('Query') is not None:
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.RedirectConfig.Query', value1.get('RedirectConfig').get('Query'))
				if value1.get('RedirectConfig').get('Host') is not None:
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.RedirectConfig.Host', value1.get('RedirectConfig').get('Host'))
				if value1.get('RedirectConfig').get('HttpCode') is not None:
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.RedirectConfig.HttpCode', value1.get('RedirectConfig').get('HttpCode'))
			if value1.get('Type') is not None:
				self.add_query_param('RuleActions.' + str(index1 + 1) + '.Type', value1.get('Type'))
			if value1.get('Order') is not None:
				self.add_query_param('RuleActions.' + str(index1 + 1) + '.Order', value1.get('Order'))
			if value1.get('RewriteConfig') is not None:
				if value1.get('RewriteConfig').get('Path') is not None:
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.RewriteConfig.Path', value1.get('RewriteConfig').get('Path'))
				if value1.get('RewriteConfig').get('Query') is not None:
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.RewriteConfig.Query', value1.get('RewriteConfig').get('Query'))
				if value1.get('RewriteConfig').get('Host') is not None:
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.RewriteConfig.Host', value1.get('RewriteConfig').get('Host'))
	def get_RuleConditions(self): # Array
		return self.get_query_params().get('RuleConditions')

	def set_RuleConditions(self, RuleConditions):  # Array
		for index1, value1 in enumerate(RuleConditions):
			if value1.get('MethodConfig') is not None:
				if value1.get('MethodConfig').get('Values') is not None:
					for index2, value2 in enumerate(value1.get('MethodConfig').get('Values')):
						self.add_query_param('RuleConditions.' + str(index1 + 1) + '.MethodConfig.Values' + str(index2 + 1), value2)
			if value1.get('SourceIpConfig') is not None:
				if value1.get('SourceIpConfig').get('Values') is not None:
					for index2, value2 in enumerate(value1.get('SourceIpConfig').get('Values')):
						self.add_query_param('RuleConditions.' + str(index1 + 1) + '.SourceIpConfig.Values' + str(index2 + 1), value2)
			if value1.get('HostConfig') is not None:
				if value1.get('HostConfig').get('Values') is not None:
					for index2, value2 in enumerate(value1.get('HostConfig').get('Values')):
						self.add_query_param('RuleConditions.' + str(index1 + 1) + '.HostConfig.Values' + str(index2 + 1), value2)
			if value1.get('QueryStringConfig') is not None:
				if value1.get('QueryStringConfig').get('Values') is not None:
					for index2, value2 in enumerate(value1.get('QueryStringConfig').get('Values')):
						if value2.get('Value') is not None:
							self.add_query_param('RuleConditions.' + str(index1 + 1) + '.QueryStringConfig.Values' + str(index2 + 1) + '.Value', value2.get('Value'))
						if value2.get('Key') is not None:
							self.add_query_param('RuleConditions.' + str(index1 + 1) + '.QueryStringConfig.Values' + str(index2 + 1) + '.Key', value2.get('Key'))
			if value1.get('ResponseStatusCodeConfig') is not None:
				if value1.get('ResponseStatusCodeConfig').get('Values') is not None:
					for index2, value2 in enumerate(value1.get('ResponseStatusCodeConfig').get('Values')):
						self.add_query_param('RuleConditions.' + str(index1 + 1) + '.ResponseStatusCodeConfig.Values' + str(index2 + 1), value2)
			if value1.get('PathConfig') is not None:
				if value1.get('PathConfig').get('Values') is not None:
					for index2, value2 in enumerate(value1.get('PathConfig').get('Values')):
						self.add_query_param('RuleConditions.' + str(index1 + 1) + '.PathConfig.Values' + str(index2 + 1), value2)
			if value1.get('CookieConfig') is not None:
				if value1.get('CookieConfig').get('Values') is not None:
					for index2, value2 in enumerate(value1.get('CookieConfig').get('Values')):
						if value2.get('Value') is not None:
							self.add_query_param('RuleConditions.' + str(index1 + 1) + '.CookieConfig.Values' + str(index2 + 1) + '.Value', value2.get('Value'))
						if value2.get('Key') is not None:
							self.add_query_param('RuleConditions.' + str(index1 + 1) + '.CookieConfig.Values' + str(index2 + 1) + '.Key', value2.get('Key'))
			if value1.get('Type') is not None:
				self.add_query_param('RuleConditions.' + str(index1 + 1) + '.Type', value1.get('Type'))
			if value1.get('HeaderConfig') is not None:
				if value1.get('HeaderConfig').get('Values') is not None:
					for index2, value2 in enumerate(value1.get('HeaderConfig').get('Values')):
						self.add_query_param('RuleConditions.' + str(index1 + 1) + '.HeaderConfig.Values' + str(index2 + 1), value2)
				if value1.get('HeaderConfig').get('Key') is not None:
					self.add_query_param('RuleConditions.' + str(index1 + 1) + '.HeaderConfig.Key', value1.get('HeaderConfig').get('Key'))
			if value1.get('ResponseHeaderConfig') is not None:
				if value1.get('ResponseHeaderConfig').get('Values') is not None:
					for index2, value2 in enumerate(value1.get('ResponseHeaderConfig').get('Values')):
						self.add_query_param('RuleConditions.' + str(index1 + 1) + '.ResponseHeaderConfig.Values' + str(index2 + 1), value2)
				if value1.get('ResponseHeaderConfig').get('Key') is not None:
					self.add_query_param('RuleConditions.' + str(index1 + 1) + '.ResponseHeaderConfig.Key', value1.get('ResponseHeaderConfig').get('Key'))
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_Priority(self): # Integer
		return self.get_query_params().get('Priority')

	def set_Priority(self, Priority):  # Integer
		self.add_query_param('Priority', Priority)
	def get_RuleId(self): # String
		return self.get_query_params().get('RuleId')

	def set_RuleId(self, RuleId):  # String
		self.add_query_param('RuleId', RuleId)
