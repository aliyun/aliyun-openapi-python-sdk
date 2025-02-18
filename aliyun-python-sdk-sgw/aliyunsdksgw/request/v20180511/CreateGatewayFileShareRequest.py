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

	def get_InPlace(self): # Boolean
		return self.get_query_params().get('InPlace')

	def set_InPlace(self, InPlace):  # Boolean
		self.add_query_param('InPlace', InPlace)
	def get_OssEndpoint(self): # String
		return self.get_query_params().get('OssEndpoint')

	def set_OssEndpoint(self, OssEndpoint):  # String
		self.add_query_param('OssEndpoint', OssEndpoint)
	def get_ReadWriteClientList(self): # String
		return self.get_query_params().get('ReadWriteClientList')

	def set_ReadWriteClientList(self, ReadWriteClientList):  # String
		self.add_query_param('ReadWriteClientList', ReadWriteClientList)
	def get_BypassCacheRead(self): # Boolean
		return self.get_query_params().get('BypassCacheRead')

	def set_BypassCacheRead(self, BypassCacheRead):  # Boolean
		self.add_query_param('BypassCacheRead', BypassCacheRead)
	def get_BackendLimit(self): # Integer
		return self.get_query_params().get('BackendLimit')

	def set_BackendLimit(self, BackendLimit):  # Integer
		self.add_query_param('BackendLimit', BackendLimit)
	def get_Squash(self): # String
		return self.get_query_params().get('Squash')

	def set_Squash(self, Squash):  # String
		self.add_query_param('Squash', Squash)
	def get_ReadOnlyClientList(self): # String
		return self.get_query_params().get('ReadOnlyClientList')

	def set_ReadOnlyClientList(self, ReadOnlyClientList):  # String
		self.add_query_param('ReadOnlyClientList', ReadOnlyClientList)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
	def get_KmsRotatePeriod(self): # Long
		return self.get_query_params().get('KmsRotatePeriod')

	def set_KmsRotatePeriod(self, KmsRotatePeriod):  # Long
		self.add_query_param('KmsRotatePeriod', KmsRotatePeriod)
	def get_RemoteSyncDownload(self): # Boolean
		return self.get_query_params().get('RemoteSyncDownload')

	def set_RemoteSyncDownload(self, RemoteSyncDownload):  # Boolean
		self.add_query_param('RemoteSyncDownload', RemoteSyncDownload)
	def get_ShareProtocol(self): # String
		return self.get_query_params().get('ShareProtocol')

	def set_ShareProtocol(self, ShareProtocol):  # String
		self.add_query_param('ShareProtocol', ShareProtocol)
	def get_NfsV4Optimization(self): # Boolean
		return self.get_query_params().get('NfsV4Optimization')

	def set_NfsV4Optimization(self, NfsV4Optimization):  # Boolean
		self.add_query_param('NfsV4Optimization', NfsV4Optimization)
	def get_AccessBasedEnumeration(self): # Boolean
		return self.get_query_params().get('AccessBasedEnumeration')

	def set_AccessBasedEnumeration(self, AccessBasedEnumeration):  # Boolean
		self.add_query_param('AccessBasedEnumeration', AccessBasedEnumeration)
	def get_GatewayId(self): # String
		return self.get_query_params().get('GatewayId')

	def set_GatewayId(self, GatewayId):  # String
		self.add_query_param('GatewayId', GatewayId)
	def get_SupportArchive(self): # Boolean
		return self.get_query_params().get('SupportArchive')

	def set_SupportArchive(self, SupportArchive):  # Boolean
		self.add_query_param('SupportArchive', SupportArchive)
	def get_CacheMode(self): # String
		return self.get_query_params().get('CacheMode')

	def set_CacheMode(self, CacheMode):  # String
		self.add_query_param('CacheMode', CacheMode)
	def get_LocalFilePath(self): # String
		return self.get_query_params().get('LocalFilePath')

	def set_LocalFilePath(self, LocalFilePath):  # String
		self.add_query_param('LocalFilePath', LocalFilePath)
	def get_PartialSyncPaths(self): # String
		return self.get_query_params().get('PartialSyncPaths')

	def set_PartialSyncPaths(self, PartialSyncPaths):  # String
		self.add_query_param('PartialSyncPaths', PartialSyncPaths)
	def get_DownloadLimit(self): # Integer
		return self.get_query_params().get('DownloadLimit')

	def set_DownloadLimit(self, DownloadLimit):  # Integer
		self.add_query_param('DownloadLimit', DownloadLimit)
	def get_ReadOnlyUserList(self): # String
		return self.get_query_params().get('ReadOnlyUserList')

	def set_ReadOnlyUserList(self, ReadOnlyUserList):  # String
		self.add_query_param('ReadOnlyUserList', ReadOnlyUserList)
	def get_FastReclaim(self): # Boolean
		return self.get_query_params().get('FastReclaim')

	def set_FastReclaim(self, FastReclaim):  # Boolean
		self.add_query_param('FastReclaim', FastReclaim)
	def get_WindowsAcl(self): # Boolean
		return self.get_query_params().get('WindowsAcl')

	def set_WindowsAcl(self, WindowsAcl):  # Boolean
		self.add_query_param('WindowsAcl', WindowsAcl)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_OssBucketName(self): # String
		return self.get_query_params().get('OssBucketName')

	def set_OssBucketName(self, OssBucketName):  # String
		self.add_query_param('OssBucketName', OssBucketName)
	def get_TransferAcceleration(self): # Boolean
		return self.get_query_params().get('TransferAcceleration')

	def set_TransferAcceleration(self, TransferAcceleration):  # Boolean
		self.add_query_param('TransferAcceleration', TransferAcceleration)
	def get_ClientSideCmk(self): # String
		return self.get_query_params().get('ClientSideCmk')

	def set_ClientSideCmk(self, ClientSideCmk):  # String
		self.add_query_param('ClientSideCmk', ClientSideCmk)
	def get_PathPrefix(self): # String
		return self.get_query_params().get('PathPrefix')

	def set_PathPrefix(self, PathPrefix):  # String
		self.add_query_param('PathPrefix', PathPrefix)
	def get_Browsable(self): # Boolean
		return self.get_query_params().get('Browsable')

	def set_Browsable(self, Browsable):  # Boolean
		self.add_query_param('Browsable', Browsable)
	def get_ReadWriteUserList(self): # String
		return self.get_query_params().get('ReadWriteUserList')

	def set_ReadWriteUserList(self, ReadWriteUserList):  # String
		self.add_query_param('ReadWriteUserList', ReadWriteUserList)
	def get_PollingInterval(self): # Integer
		return self.get_query_params().get('PollingInterval')

	def set_PollingInterval(self, PollingInterval):  # Integer
		self.add_query_param('PollingInterval', PollingInterval)
	def get_ServerSideAlgorithm(self): # String
		return self.get_query_params().get('ServerSideAlgorithm')

	def set_ServerSideAlgorithm(self, ServerSideAlgorithm):  # String
		self.add_query_param('ServerSideAlgorithm', ServerSideAlgorithm)
	def get_ServerSideCmk(self): # String
		return self.get_query_params().get('ServerSideCmk')

	def set_ServerSideCmk(self, ServerSideCmk):  # String
		self.add_query_param('ServerSideCmk', ServerSideCmk)
	def get_ServerSideEncryption(self): # Boolean
		return self.get_query_params().get('ServerSideEncryption')

	def set_ServerSideEncryption(self, ServerSideEncryption):  # Boolean
		self.add_query_param('ServerSideEncryption', ServerSideEncryption)
	def get_IgnoreDelete(self): # Boolean
		return self.get_query_params().get('IgnoreDelete')

	def set_IgnoreDelete(self, IgnoreDelete):  # Boolean
		self.add_query_param('IgnoreDelete', IgnoreDelete)
	def get_LagPeriod(self): # Long
		return self.get_query_params().get('LagPeriod')

	def set_LagPeriod(self, LagPeriod):  # Long
		self.add_query_param('LagPeriod', LagPeriod)
	def get_DirectIO(self): # Boolean
		return self.get_query_params().get('DirectIO')

	def set_DirectIO(self, DirectIO):  # Boolean
		self.add_query_param('DirectIO', DirectIO)
	def get_ClientSideEncryption(self): # Boolean
		return self.get_query_params().get('ClientSideEncryption')

	def set_ClientSideEncryption(self, ClientSideEncryption):  # Boolean
		self.add_query_param('ClientSideEncryption', ClientSideEncryption)
	def get_OssBucketRegionId(self): # String
		return self.get_query_params().get('OssBucketRegionId')

	def set_OssBucketRegionId(self, OssBucketRegionId):  # String
		self.add_query_param('OssBucketRegionId', OssBucketRegionId)
	def get_OssBucketSsl(self): # Boolean
		return self.get_query_params().get('OssBucketSsl')

	def set_OssBucketSsl(self, OssBucketSsl):  # Boolean
		self.add_query_param('OssBucketSsl', OssBucketSsl)
	def get_BindIPAddr(self): # String
		return self.get_query_params().get('BindIPAddr')

	def set_BindIPAddr(self, BindIPAddr):  # String
		self.add_query_param('BindIPAddr', BindIPAddr)
	def get_RemoteSync(self): # Boolean
		return self.get_query_params().get('RemoteSync')

	def set_RemoteSync(self, RemoteSync):  # Boolean
		self.add_query_param('RemoteSync', RemoteSync)
	def get_FrontendLimit(self): # Integer
		return self.get_query_params().get('FrontendLimit')

	def set_FrontendLimit(self, FrontendLimit):  # Integer
		self.add_query_param('FrontendLimit', FrontendLimit)
