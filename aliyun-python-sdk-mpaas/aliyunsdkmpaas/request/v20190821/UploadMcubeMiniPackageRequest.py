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
from aliyunsdkmpaas.endpoint import endpoint_data

class UploadMcubeMiniPackageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mPaaS', '2019-08-21', 'UploadMcubeMiniPackage')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AutoInstall(self):
		return self.get_body_params().get('AutoInstall')

	def set_AutoInstall(self,AutoInstall):
		self.add_body_params('AutoInstall', AutoInstall)

	def get_InstallType(self):
		return self.get_body_params().get('InstallType')

	def set_InstallType(self,InstallType):
		self.add_body_params('InstallType', InstallType)

	def get_OnexFlag(self):
		return self.get_body_params().get('OnexFlag')

	def set_OnexFlag(self,OnexFlag):
		self.add_body_params('OnexFlag', OnexFlag)

	def get_EnableOptionMenu(self):
		return self.get_body_params().get('EnableOptionMenu')

	def set_EnableOptionMenu(self,EnableOptionMenu):
		self.add_body_params('EnableOptionMenu', EnableOptionMenu)

	def get_H5Version(self):
		return self.get_body_params().get('H5Version')

	def set_H5Version(self,H5Version):
		self.add_body_params('H5Version', H5Version)

	def get_EnableTabBar(self):
		return self.get_body_params().get('EnableTabBar')

	def set_EnableTabBar(self,EnableTabBar):
		self.add_body_params('EnableTabBar', EnableTabBar)

	def get_UserId(self):
		return self.get_body_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_body_params('UserId', UserId)

	def get_Uuid(self):
		return self.get_body_params().get('Uuid')

	def set_Uuid(self,Uuid):
		self.add_body_params('Uuid', Uuid)

	def get_ResourceFileUrl(self):
		return self.get_body_params().get('ResourceFileUrl')

	def set_ResourceFileUrl(self,ResourceFileUrl):
		self.add_body_params('ResourceFileUrl', ResourceFileUrl)

	def get_H5Id(self):
		return self.get_body_params().get('H5Id')

	def set_H5Id(self,H5Id):
		self.add_body_params('H5Id', H5Id)

	def get_ExtendInfo(self):
		return self.get_body_params().get('ExtendInfo')

	def set_ExtendInfo(self,ExtendInfo):
		self.add_body_params('ExtendInfo', ExtendInfo)

	def get_MainUrl(self):
		return self.get_body_params().get('MainUrl')

	def set_MainUrl(self,MainUrl):
		self.add_body_params('MainUrl', MainUrl)

	def get_ClientVersionMin(self):
		return self.get_body_params().get('ClientVersionMin')

	def set_ClientVersionMin(self,ClientVersionMin):
		self.add_body_params('ClientVersionMin', ClientVersionMin)

	def get_EnableKeepAlive(self):
		return self.get_body_params().get('EnableKeepAlive')

	def set_EnableKeepAlive(self,EnableKeepAlive):
		self.add_body_params('EnableKeepAlive', EnableKeepAlive)

	def get_Vhost(self):
		return self.get_body_params().get('Vhost')

	def set_Vhost(self,Vhost):
		self.add_body_params('Vhost', Vhost)

	def get_ClientVersionMax(self):
		return self.get_body_params().get('ClientVersionMax')

	def set_ClientVersionMax(self,ClientVersionMax):
		self.add_body_params('ClientVersionMax', ClientVersionMax)

	def get_PackageType(self):
		return self.get_body_params().get('PackageType')

	def set_PackageType(self,PackageType):
		self.add_body_params('PackageType', PackageType)

	def get_WorkspaceId(self):
		return self.get_body_params().get('WorkspaceId')

	def set_WorkspaceId(self,WorkspaceId):
		self.add_body_params('WorkspaceId', WorkspaceId)

	def get_H5Name(self):
		return self.get_body_params().get('H5Name')

	def set_H5Name(self,H5Name):
		self.add_body_params('H5Name', H5Name)

	def get_Platform(self):
		return self.get_body_params().get('Platform')

	def set_Platform(self,Platform):
		self.add_body_params('Platform', Platform)

	def get_TenantId(self):
		return self.get_body_params().get('TenantId')

	def set_TenantId(self,TenantId):
		self.add_body_params('TenantId', TenantId)

	def get_ResourceType(self):
		return self.get_body_params().get('ResourceType')

	def set_ResourceType(self,ResourceType):
		self.add_body_params('ResourceType', ResourceType)

	def get_IconFileUrl(self):
		return self.get_body_params().get('IconFileUrl')

	def set_IconFileUrl(self,IconFileUrl):
		self.add_body_params('IconFileUrl', IconFileUrl)

	def get_AppId(self):
		return self.get_body_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_body_params('AppId', AppId)