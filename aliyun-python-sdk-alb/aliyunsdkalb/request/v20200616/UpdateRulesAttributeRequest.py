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

class UpdateRulesAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alb', '2020-06-16', 'UpdateRulesAttribute','alb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Rules(self): # Array
		return self.get_query_params().get('Rules')

	def set_Rules(self, Rules):  # Array
		for index1, value1 in enumerate(Rules):
			if value1.get('RuleConditions') is not None:
				for index2, value2 in enumerate(value1.get('RuleConditions')):
					if value2.get('MethodConfig') is not None:
						if value2.get('MethodConfig').get('Values') is not None:
							for index3, value3 in enumerate(value2.get('MethodConfig').get('Values')):
								self.add_query_param('Rules.' + str(index1 + 1) + '.RuleConditions.' + str(index2 + 1) + '.MethodConfig.Values' + str(index3 + 1), value3)
					if value2.get('SourceIpConfig') is not None:
						if value2.get('SourceIpConfig').get('Values') is not None:
							for index3, value3 in enumerate(value2.get('SourceIpConfig').get('Values')):
								self.add_query_param('Rules.' + str(index1 + 1) + '.RuleConditions.' + str(index2 + 1) + '.SourceIpConfig.Values' + str(index3 + 1), value3)
					if value2.get('HostConfig') is not None:
						if value2.get('HostConfig').get('Values') is not None:
							for index3, value3 in enumerate(value2.get('HostConfig').get('Values')):
								self.add_query_param('Rules.' + str(index1 + 1) + '.RuleConditions.' + str(index2 + 1) + '.HostConfig.Values' + str(index3 + 1), value3)
					if value2.get('QueryStringConfig') is not None:
						if value2.get('QueryStringConfig').get('Values') is not None:
							for index3, value3 in enumerate(value2.get('QueryStringConfig').get('Values')):
								if value3.get('Value') is not None:
									self.add_query_param('Rules.' + str(index1 + 1) + '.RuleConditions.' + str(index2 + 1) + '.QueryStringConfig.Values' + str(index3 + 1) + '.Value', value3.get('Value'))
								if value3.get('Key') is not None:
									self.add_query_param('Rules.' + str(index1 + 1) + '.RuleConditions.' + str(index2 + 1) + '.QueryStringConfig.Values' + str(index3 + 1) + '.Key', value3.get('Key'))
					if value2.get('ResponseStatusCodeConfig') is not None:
						if value2.get('ResponseStatusCodeConfig').get('Values') is not None:
							for index3, value3 in enumerate(value2.get('ResponseStatusCodeConfig').get('Values')):
								self.add_query_param('Rules.' + str(index1 + 1) + '.RuleConditions.' + str(index2 + 1) + '.ResponseStatusCodeConfig.Values' + str(index3 + 1), value3)
					if value2.get('PathConfig') is not None:
						if value2.get('PathConfig').get('Values') is not None:
							for index3, value3 in enumerate(value2.get('PathConfig').get('Values')):
								self.add_query_param('Rules.' + str(index1 + 1) + '.RuleConditions.' + str(index2 + 1) + '.PathConfig.Values' + str(index3 + 1), value3)
					if value2.get('CookieConfig') is not None:
						if value2.get('CookieConfig').get('Values') is not None:
							for index3, value3 in enumerate(value2.get('CookieConfig').get('Values')):
								if value3.get('Value') is not None:
									self.add_query_param('Rules.' + str(index1 + 1) + '.RuleConditions.' + str(index2 + 1) + '.CookieConfig.Values' + str(index3 + 1) + '.Value', value3.get('Value'))
								if value3.get('Key') is not None:
									self.add_query_param('Rules.' + str(index1 + 1) + '.RuleConditions.' + str(index2 + 1) + '.CookieConfig.Values' + str(index3 + 1) + '.Key', value3.get('Key'))
					if value2.get('Type') is not None:
						self.add_query_param('Rules.' + str(index1 + 1) + '.RuleConditions.' + str(index2 + 1) + '.Type', value2.get('Type'))
					if value2.get('HeaderConfig') is not None:
						if value2.get('HeaderConfig').get('Values') is not None:
							for index3, value3 in enumerate(value2.get('HeaderConfig').get('Values')):
								self.add_query_param('Rules.' + str(index1 + 1) + '.RuleConditions.' + str(index2 + 1) + '.HeaderConfig.Values' + str(index3 + 1), value3)
						if value2.get('HeaderConfig').get('Key') is not None:
							self.add_query_param('Rules.' + str(index1 + 1) + '.RuleConditions.' + str(index2 + 1) + '.HeaderConfig.Key', value2.get('HeaderConfig').get('Key'))
					if value2.get('ResponseHeaderConfig') is not None:
						if value2.get('ResponseHeaderConfig').get('Values') is not None:
							for index3, value3 in enumerate(value2.get('ResponseHeaderConfig').get('Values')):
								self.add_query_param('Rules.' + str(index1 + 1) + '.RuleConditions.' + str(index2 + 1) + '.ResponseHeaderConfig.Values' + str(index3 + 1), value3)
						if value2.get('ResponseHeaderConfig').get('Key') is not None:
							self.add_query_param('Rules.' + str(index1 + 1) + '.RuleConditions.' + str(index2 + 1) + '.ResponseHeaderConfig.Key', value2.get('ResponseHeaderConfig').get('Key'))
			if value1.get('RuleName') is not None:
				self.add_query_param('Rules.' + str(index1 + 1) + '.RuleName', value1.get('RuleName'))
			if value1.get('Priority') is not None:
				self.add_query_param('Rules.' + str(index1 + 1) + '.Priority', value1.get('Priority'))
			if value1.get('RuleId') is not None:
				self.add_query_param('Rules.' + str(index1 + 1) + '.RuleId', value1.get('RuleId'))
			if value1.get('RuleActions') is not None:
				for index2, value2 in enumerate(value1.get('RuleActions')):
					if value2.get('FixedResponseConfig') is not None:
						if value2.get('FixedResponseConfig').get('HttpCode') is not None:
							self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.FixedResponseConfig.HttpCode', value2.get('FixedResponseConfig').get('HttpCode'))
						if value2.get('FixedResponseConfig').get('Content') is not None:
							self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.FixedResponseConfig.Content', value2.get('FixedResponseConfig').get('Content'))
						if value2.get('FixedResponseConfig').get('ContentType') is not None:
							self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.FixedResponseConfig.ContentType', value2.get('FixedResponseConfig').get('ContentType'))
					if value2.get('TrafficMirrorConfig') is not None:
						if value2.get('TrafficMirrorConfig').get('MirrorGroupConfig') is not None:
							if value2.get('TrafficMirrorConfig').get('MirrorGroupConfig').get('ServerGroupTuples') is not None:
								for index3, value3 in enumerate(value2.get('TrafficMirrorConfig').get('MirrorGroupConfig').get('ServerGroupTuples')):
									if value3.get('ServerGroupId') is not None:
										self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.TrafficMirrorConfig.MirrorGroupConfig.ServerGroupTuples' + str(index3 + 1) + '.ServerGroupId', value3.get('ServerGroupId'))
						if value2.get('TrafficMirrorConfig').get('TargetType') is not None:
							self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.TrafficMirrorConfig.TargetType', value2.get('TrafficMirrorConfig').get('TargetType'))
					if value2.get('ForwardGroupConfig') is not None:
						if value2.get('ForwardGroupConfig').get('ServerGroupStickySession') is not None:
							if value2.get('ForwardGroupConfig').get('ServerGroupStickySession').get('Enabled') is not None:
								self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.ForwardGroupConfig.ServerGroupStickySession.Enabled', value2.get('ForwardGroupConfig').get('ServerGroupStickySession').get('Enabled'))
							if value2.get('ForwardGroupConfig').get('ServerGroupStickySession').get('Timeout') is not None:
								self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.ForwardGroupConfig.ServerGroupStickySession.Timeout', value2.get('ForwardGroupConfig').get('ServerGroupStickySession').get('Timeout'))
						if value2.get('ForwardGroupConfig').get('ServerGroupTuples') is not None:
							for index3, value3 in enumerate(value2.get('ForwardGroupConfig').get('ServerGroupTuples')):
								if value3.get('ServerGroupId') is not None:
									self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.ForwardGroupConfig.ServerGroupTuples' + str(index3 + 1) + '.ServerGroupId', value3.get('ServerGroupId'))
								if value3.get('Weight') is not None:
									self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.ForwardGroupConfig.ServerGroupTuples' + str(index3 + 1) + '.Weight', value3.get('Weight'))
					if value2.get('RemoveHeaderConfig') is not None:
						if value2.get('RemoveHeaderConfig').get('Key') is not None:
							self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.RemoveHeaderConfig.Key', value2.get('RemoveHeaderConfig').get('Key'))
					if value2.get('InsertHeaderConfig') is not None:
						if value2.get('InsertHeaderConfig').get('ValueType') is not None:
							self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.InsertHeaderConfig.ValueType', value2.get('InsertHeaderConfig').get('ValueType'))
						if value2.get('InsertHeaderConfig').get('CoverEnabled') is not None:
							self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.InsertHeaderConfig.CoverEnabled', value2.get('InsertHeaderConfig').get('CoverEnabled'))
						if value2.get('InsertHeaderConfig').get('Value') is not None:
							self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.InsertHeaderConfig.Value', value2.get('InsertHeaderConfig').get('Value'))
						if value2.get('InsertHeaderConfig').get('Key') is not None:
							self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.InsertHeaderConfig.Key', value2.get('InsertHeaderConfig').get('Key'))
					if value2.get('TrafficLimitConfig') is not None:
						if value2.get('TrafficLimitConfig').get('QPS') is not None:
							self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.TrafficLimitConfig.QPS', value2.get('TrafficLimitConfig').get('QPS'))
					if value2.get('CorsConfig') is not None:
						if value2.get('CorsConfig').get('AllowCredentials') is not None:
							self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.CorsConfig.AllowCredentials', value2.get('CorsConfig').get('AllowCredentials'))
						if value2.get('CorsConfig').get('AllowOrigin') is not None:
							for index3, value3 in enumerate(value2.get('CorsConfig').get('AllowOrigin')):
								self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.CorsConfig.AllowOrigin' + str(index3 + 1), value3)
						if value2.get('CorsConfig').get('MaxAge') is not None:
							self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.CorsConfig.MaxAge', value2.get('CorsConfig').get('MaxAge'))
						if value2.get('CorsConfig').get('AllowMethods') is not None:
							for index3, value3 in enumerate(value2.get('CorsConfig').get('AllowMethods')):
								self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.CorsConfig.AllowMethods' + str(index3 + 1), value3)
						if value2.get('CorsConfig').get('AllowHeaders') is not None:
							for index3, value3 in enumerate(value2.get('CorsConfig').get('AllowHeaders')):
								self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.CorsConfig.AllowHeaders' + str(index3 + 1), value3)
						if value2.get('CorsConfig').get('ExposeHeaders') is not None:
							for index3, value3 in enumerate(value2.get('CorsConfig').get('ExposeHeaders')):
								self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.CorsConfig.ExposeHeaders' + str(index3 + 1), value3)
					if value2.get('RedirectConfig') is not None:
						if value2.get('RedirectConfig').get('Path') is not None:
							self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.RedirectConfig.Path', value2.get('RedirectConfig').get('Path'))
						if value2.get('RedirectConfig').get('Protocol') is not None:
							self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.RedirectConfig.Protocol', value2.get('RedirectConfig').get('Protocol'))
						if value2.get('RedirectConfig').get('Port') is not None:
							self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.RedirectConfig.Port', value2.get('RedirectConfig').get('Port'))
						if value2.get('RedirectConfig').get('Query') is not None:
							self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.RedirectConfig.Query', value2.get('RedirectConfig').get('Query'))
						if value2.get('RedirectConfig').get('Host') is not None:
							self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.RedirectConfig.Host', value2.get('RedirectConfig').get('Host'))
						if value2.get('RedirectConfig').get('HttpCode') is not None:
							self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.RedirectConfig.HttpCode', value2.get('RedirectConfig').get('HttpCode'))
					if value2.get('Type') is not None:
						self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.Type', value2.get('Type'))
					if value2.get('Order') is not None:
						self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.Order', value2.get('Order'))
					if value2.get('RewriteConfig') is not None:
						if value2.get('RewriteConfig').get('Path') is not None:
							self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.RewriteConfig.Path', value2.get('RewriteConfig').get('Path'))
						if value2.get('RewriteConfig').get('Query') is not None:
							self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.RewriteConfig.Query', value2.get('RewriteConfig').get('Query'))
						if value2.get('RewriteConfig').get('Host') is not None:
							self.add_query_param('Rules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.RewriteConfig.Host', value2.get('RewriteConfig').get('Host'))
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
