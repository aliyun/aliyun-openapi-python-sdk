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
from aliyunsdkservicemesh.endpoint import endpoint_data

class UpdateMeshFeatureRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'servicemesh', '2020-01-11', 'UpdateMeshFeature','servicemesh')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ProxyRequestCPU(self):
		return self.get_body_params().get('ProxyRequestCPU')

	def set_ProxyRequestCPU(self,ProxyRequestCPU):
		self.add_body_params('ProxyRequestCPU', ProxyRequestCPU)

	def get_OPALimitCPU(self):
		return self.get_body_params().get('OPALimitCPU')

	def set_OPALimitCPU(self,OPALimitCPU):
		self.add_body_params('OPALimitCPU', OPALimitCPU)

	def get_OpenAgentPolicy(self):
		return self.get_body_params().get('OpenAgentPolicy')

	def set_OpenAgentPolicy(self,OpenAgentPolicy):
		self.add_body_params('OpenAgentPolicy', OpenAgentPolicy)

	def get_OpaEnabled(self):
		return self.get_body_params().get('OpaEnabled')

	def set_OpaEnabled(self,OpaEnabled):
		self.add_body_params('OpaEnabled', OpaEnabled)

	def get_ProxyLimitMemory(self):
		return self.get_body_params().get('ProxyLimitMemory')

	def set_ProxyLimitMemory(self,ProxyLimitMemory):
		self.add_body_params('ProxyLimitMemory', ProxyLimitMemory)

	def get_CniExcludeNamespaces(self):
		return self.get_body_params().get('CniExcludeNamespaces')

	def set_CniExcludeNamespaces(self,CniExcludeNamespaces):
		self.add_body_params('CniExcludeNamespaces', CniExcludeNamespaces)

	def get_OPALogLevel(self):
		return self.get_body_params().get('OPALogLevel')

	def set_OPALogLevel(self,OPALogLevel):
		self.add_body_params('OPALogLevel', OPALogLevel)

	def get_CustomizedZipkin(self):
		return self.get_body_params().get('CustomizedZipkin')

	def set_CustomizedZipkin(self,CustomizedZipkin):
		self.add_body_params('CustomizedZipkin', CustomizedZipkin)

	def get_SidecarInjectorRequestCPU(self):
		return self.get_body_params().get('SidecarInjectorRequestCPU')

	def set_SidecarInjectorRequestCPU(self,SidecarInjectorRequestCPU):
		self.add_body_params('SidecarInjectorRequestCPU', SidecarInjectorRequestCPU)

	def get_CniEnabled(self):
		return self.get_body_params().get('CniEnabled')

	def set_CniEnabled(self,CniEnabled):
		self.add_body_params('CniEnabled', CniEnabled)

	def get_Tracing(self):
		return self.get_body_params().get('Tracing')

	def set_Tracing(self,Tracing):
		self.add_body_params('Tracing', Tracing)

	def get_IncludeIPRanges(self):
		return self.get_body_params().get('IncludeIPRanges')

	def set_IncludeIPRanges(self,IncludeIPRanges):
		self.add_body_params('IncludeIPRanges', IncludeIPRanges)

	def get_OPALimitMemory(self):
		return self.get_body_params().get('OPALimitMemory')

	def set_OPALimitMemory(self,OPALimitMemory):
		self.add_body_params('OPALimitMemory', OPALimitMemory)

	def get_ProxyLimitCPU(self):
		return self.get_body_params().get('ProxyLimitCPU')

	def set_ProxyLimitCPU(self,ProxyLimitCPU):
		self.add_body_params('ProxyLimitCPU', ProxyLimitCPU)

	def get_ProxyRequestMemory(self):
		return self.get_body_params().get('ProxyRequestMemory')

	def set_ProxyRequestMemory(self,ProxyRequestMemory):
		self.add_body_params('ProxyRequestMemory', ProxyRequestMemory)

	def get_Telemetry(self):
		return self.get_body_params().get('Telemetry')

	def set_Telemetry(self,Telemetry):
		self.add_body_params('Telemetry', Telemetry)

	def get_OPARequestCPU(self):
		return self.get_body_params().get('OPARequestCPU')

	def set_OPARequestCPU(self,OPARequestCPU):
		self.add_body_params('OPARequestCPU', OPARequestCPU)

	def get_SidecarInjectorWebhookAsYaml(self):
		return self.get_body_params().get('SidecarInjectorWebhookAsYaml')

	def set_SidecarInjectorWebhookAsYaml(self,SidecarInjectorWebhookAsYaml):
		self.add_body_params('SidecarInjectorWebhookAsYaml', SidecarInjectorWebhookAsYaml)

	def get_OPARequestMemory(self):
		return self.get_body_params().get('OPARequestMemory')

	def set_OPARequestMemory(self,OPARequestMemory):
		self.add_body_params('OPARequestMemory', OPARequestMemory)

	def get_AutoInjectionPolicyEnabled(self):
		return self.get_body_params().get('AutoInjectionPolicyEnabled')

	def set_AutoInjectionPolicyEnabled(self,AutoInjectionPolicyEnabled):
		self.add_body_params('AutoInjectionPolicyEnabled', AutoInjectionPolicyEnabled)

	def get_SidecarInjectorLimitMemory(self):
		return self.get_body_params().get('SidecarInjectorLimitMemory')

	def set_SidecarInjectorLimitMemory(self,SidecarInjectorLimitMemory):
		self.add_body_params('SidecarInjectorLimitMemory', SidecarInjectorLimitMemory)

	def get_EnableAudit(self):
		return self.get_body_params().get('EnableAudit')

	def set_EnableAudit(self,EnableAudit):
		self.add_body_params('EnableAudit', EnableAudit)

	def get_ClusterDomain(self):
		return self.get_body_params().get('ClusterDomain')

	def set_ClusterDomain(self,ClusterDomain):
		self.add_body_params('ClusterDomain', ClusterDomain)

	def get_SidecarInjectorRequestMemory(self):
		return self.get_body_params().get('SidecarInjectorRequestMemory')

	def set_SidecarInjectorRequestMemory(self,SidecarInjectorRequestMemory):
		self.add_body_params('SidecarInjectorRequestMemory', SidecarInjectorRequestMemory)

	def get_ServiceMeshId(self):
		return self.get_body_params().get('ServiceMeshId')

	def set_ServiceMeshId(self,ServiceMeshId):
		self.add_body_params('ServiceMeshId', ServiceMeshId)

	def get_LocalityLoadBalancing(self):
		return self.get_body_params().get('LocalityLoadBalancing')

	def set_LocalityLoadBalancing(self,LocalityLoadBalancing):
		self.add_body_params('LocalityLoadBalancing', LocalityLoadBalancing)

	def get_SidecarInjectorLimitCPU(self):
		return self.get_body_params().get('SidecarInjectorLimitCPU')

	def set_SidecarInjectorLimitCPU(self,SidecarInjectorLimitCPU):
		self.add_body_params('SidecarInjectorLimitCPU', SidecarInjectorLimitCPU)

	def get_TraceSampling(self):
		return self.get_body_params().get('TraceSampling')

	def set_TraceSampling(self,TraceSampling):
		self.add_body_params('TraceSampling', TraceSampling)

	def get_Http10Enabled(self):
		return self.get_body_params().get('Http10Enabled')

	def set_Http10Enabled(self,Http10Enabled):
		self.add_body_params('Http10Enabled', Http10Enabled)

	def get_AuditProject(self):
		return self.get_body_params().get('AuditProject')

	def set_AuditProject(self,AuditProject):
		self.add_body_params('AuditProject', AuditProject)

	def get_OutboundTrafficPolicy(self):
		return self.get_body_params().get('OutboundTrafficPolicy')

	def set_OutboundTrafficPolicy(self,OutboundTrafficPolicy):
		self.add_body_params('OutboundTrafficPolicy', OutboundTrafficPolicy)

	def get_EnableNamespacesByDefault(self):
		return self.get_body_params().get('EnableNamespacesByDefault')

	def set_EnableNamespacesByDefault(self,EnableNamespacesByDefault):
		self.add_body_params('EnableNamespacesByDefault', EnableNamespacesByDefault)