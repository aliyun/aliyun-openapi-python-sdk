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
from aliyunsdksgw.endpoint import endpoint_data

class CreateGatewayFileShareRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'sgw', '2018-05-11', 'CreateGatewayFileShare','hcs_sgw')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_InPlace(self):
		return self.get_query_params().get('InPlace')

	def set_InPlace(self,InPlace):
		self.add_query_param('InPlace',InPlace)

	def get_OssEndpoint(self):
		return self.get_query_params().get('OssEndpoint')

	def set_OssEndpoint(self,OssEndpoint):
		self.add_query_param('OssEndpoint',OssEndpoint)

	def get_ReadWriteClientList(self):
		return self.get_query_params().get('ReadWriteClientList')

	def set_ReadWriteClientList(self,ReadWriteClientList):
		self.add_query_param('ReadWriteClientList',ReadWriteClientList)

	def get_BypassCacheRead(self):
		return self.get_query_params().get('BypassCacheRead')

	def set_BypassCacheRead(self,BypassCacheRead):
		self.add_query_param('BypassCacheRead',BypassCacheRead)

	def get_BackendLimit(self):
		return self.get_query_params().get('BackendLimit')

	def set_BackendLimit(self,BackendLimit):
		self.add_query_param('BackendLimit',BackendLimit)

	def get_Squash(self):
		return self.get_query_params().get('Squash')

	def set_Squash(self,Squash):
		self.add_query_param('Squash',Squash)

	def get_ReadOnlyClientList(self):
		return self.get_query_params().get('ReadOnlyClientList')

	def set_ReadOnlyClientList(self,ReadOnlyClientList):
		self.add_query_param('ReadOnlyClientList',ReadOnlyClientList)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_KmsRotatePeriod(self):
		return self.get_query_params().get('KmsRotatePeriod')

	def set_KmsRotatePeriod(self,KmsRotatePeriod):
		self.add_query_param('KmsRotatePeriod',KmsRotatePeriod)

	def get_RemoteSyncDownload(self):
		return self.get_query_params().get('RemoteSyncDownload')

	def set_RemoteSyncDownload(self,RemoteSyncDownload):
		self.add_query_param('RemoteSyncDownload',RemoteSyncDownload)

	def get_ShareProtocol(self):
		return self.get_query_params().get('ShareProtocol')

	def set_ShareProtocol(self,ShareProtocol):
		self.add_query_param('ShareProtocol',ShareProtocol)

	def get_NfsV4Optimization(self):
		return self.get_query_params().get('NfsV4Optimization')

	def set_NfsV4Optimization(self,NfsV4Optimization):
		self.add_query_param('NfsV4Optimization',NfsV4Optimization)

	def get_AccessBasedEnumeration(self):
		return self.get_query_params().get('AccessBasedEnumeration')

	def set_AccessBasedEnumeration(self,AccessBasedEnumeration):
		self.add_query_param('AccessBasedEnumeration',AccessBasedEnumeration)

	def get_GatewayId(self):
		return self.get_query_params().get('GatewayId')

	def set_GatewayId(self,GatewayId):
		self.add_query_param('GatewayId',GatewayId)

	def get_SupportArchive(self):
		return self.get_query_params().get('SupportArchive')

	def set_SupportArchive(self,SupportArchive):
		self.add_query_param('SupportArchive',SupportArchive)

	def get_CacheMode(self):
		return self.get_query_params().get('CacheMode')

	def set_CacheMode(self,CacheMode):
		self.add_query_param('CacheMode',CacheMode)

	def get_LocalFilePath(self):
		return self.get_query_params().get('LocalFilePath')

	def set_LocalFilePath(self,LocalFilePath):
		self.add_query_param('LocalFilePath',LocalFilePath)

	def get_PartialSyncPaths(self):
		return self.get_query_params().get('PartialSyncPaths')

	def set_PartialSyncPaths(self,PartialSyncPaths):
		self.add_query_param('PartialSyncPaths',PartialSyncPaths)

	def get_DownloadLimit(self):
		return self.get_query_params().get('DownloadLimit')

	def set_DownloadLimit(self,DownloadLimit):
		self.add_query_param('DownloadLimit',DownloadLimit)

	def get_ReadOnlyUserList(self):
		return self.get_query_params().get('ReadOnlyUserList')

	def set_ReadOnlyUserList(self,ReadOnlyUserList):
		self.add_query_param('ReadOnlyUserList',ReadOnlyUserList)

	def get_FastReclaim(self):
		return self.get_query_params().get('FastReclaim')

	def set_FastReclaim(self,FastReclaim):
		self.add_query_param('FastReclaim',FastReclaim)

	def get_WindowsAcl(self):
		return self.get_query_params().get('WindowsAcl')

	def set_WindowsAcl(self,WindowsAcl):
		self.add_query_param('WindowsAcl',WindowsAcl)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_OssBucketName(self):
		return self.get_query_params().get('OssBucketName')

	def set_OssBucketName(self,OssBucketName):
		self.add_query_param('OssBucketName',OssBucketName)

	def get_TransferAcceleration(self):
		return self.get_query_params().get('TransferAcceleration')

	def set_TransferAcceleration(self,TransferAcceleration):
		self.add_query_param('TransferAcceleration',TransferAcceleration)

	def get_ClientSideCmk(self):
		return self.get_query_params().get('ClientSideCmk')

	def set_ClientSideCmk(self,ClientSideCmk):
		self.add_query_param('ClientSideCmk',ClientSideCmk)

	def get_PathPrefix(self):
		return self.get_query_params().get('PathPrefix')

	def set_PathPrefix(self,PathPrefix):
		self.add_query_param('PathPrefix',PathPrefix)

	def get_Browsable(self):
		return self.get_query_params().get('Browsable')

	def set_Browsable(self,Browsable):
		self.add_query_param('Browsable',Browsable)

	def get_ReadWriteUserList(self):
		return self.get_query_params().get('ReadWriteUserList')

	def set_ReadWriteUserList(self,ReadWriteUserList):
		self.add_query_param('ReadWriteUserList',ReadWriteUserList)

	def get_PollingInterval(self):
		return self.get_query_params().get('PollingInterval')

	def set_PollingInterval(self,PollingInterval):
		self.add_query_param('PollingInterval',PollingInterval)

	def get_ServerSideAlgorithm(self):
		return self.get_query_params().get('ServerSideAlgorithm')

	def set_ServerSideAlgorithm(self,ServerSideAlgorithm):
		self.add_query_param('ServerSideAlgorithm',ServerSideAlgorithm)

	def get_ServerSideCmk(self):
		return self.get_query_params().get('ServerSideCmk')

	def set_ServerSideCmk(self,ServerSideCmk):
		self.add_query_param('ServerSideCmk',ServerSideCmk)

	def get_ServerSideEncryption(self):
		return self.get_query_params().get('ServerSideEncryption')

	def set_ServerSideEncryption(self,ServerSideEncryption):
		self.add_query_param('ServerSideEncryption',ServerSideEncryption)

	def get_IgnoreDelete(self):
		return self.get_query_params().get('IgnoreDelete')

	def set_IgnoreDelete(self,IgnoreDelete):
		self.add_query_param('IgnoreDelete',IgnoreDelete)

	def get_LagPeriod(self):
		return self.get_query_params().get('LagPeriod')

	def set_LagPeriod(self,LagPeriod):
		self.add_query_param('LagPeriod',LagPeriod)

	def get_DirectIO(self):
		return self.get_query_params().get('DirectIO')

	def set_DirectIO(self,DirectIO):
		self.add_query_param('DirectIO',DirectIO)

	def get_ClientSideEncryption(self):
		return self.get_query_params().get('ClientSideEncryption')

	def set_ClientSideEncryption(self,ClientSideEncryption):
		self.add_query_param('ClientSideEncryption',ClientSideEncryption)

	def get_OssBucketSsl(self):
		return self.get_query_params().get('OssBucketSsl')

	def set_OssBucketSsl(self,OssBucketSsl):
		self.add_query_param('OssBucketSsl',OssBucketSsl)

	def get_RemoteSync(self):
		return self.get_query_params().get('RemoteSync')

	def set_RemoteSync(self,RemoteSync):
		self.add_query_param('RemoteSync',RemoteSync)

	def get_FrontendLimit(self):
		return self.get_query_params().get('FrontendLimit')

	def set_FrontendLimit(self,FrontendLimit):
		self.add_query_param('FrontendLimit',FrontendLimit)