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
class SaveApRadioSsidConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudwf', '2017-03-28', 'SaveApRadioSsidConfig','cloudwf')

	def get_Nasid(self):
		return self.get_query_params().get('Nasid')

	def set_Nasid(self,Nasid):
		self.add_query_param('Nasid',Nasid)

	def get_AuthPort(self):
		return self.get_query_params().get('AuthPort')

	def set_AuthPort(self,AuthPort):
		self.add_query_param('AuthPort',AuthPort)

	def get_Hidden(self):
		return self.get_query_params().get('Hidden')

	def set_Hidden(self,Hidden):
		self.add_query_param('Hidden',Hidden)

	def get_DynamicVlan(self):
		return self.get_query_params().get('DynamicVlan')

	def set_DynamicVlan(self,DynamicVlan):
		self.add_query_param('DynamicVlan',DynamicVlan)

	def get_AuthServer(self):
		return self.get_query_params().get('AuthServer')

	def set_AuthServer(self,AuthServer):
		self.add_query_param('AuthServer',AuthServer)

	def get_SecondaryAcctServer(self):
		return self.get_query_params().get('SecondaryAcctServer')

	def set_SecondaryAcctServer(self,SecondaryAcctServer):
		self.add_query_param('SecondaryAcctServer',SecondaryAcctServer)

	def get_Ssid(self):
		return self.get_query_params().get('Ssid')

	def set_Ssid(self,Ssid):
		self.add_query_param('Ssid',Ssid)

	def get_Cir(self):
		return self.get_query_params().get('Cir')

	def set_Cir(self,Cir):
		self.add_query_param('Cir',Cir)

	def get_Mac(self):
		return self.get_query_params().get('Mac')

	def set_Mac(self,Mac):
		self.add_query_param('Mac',Mac)

	def get_SecondaryAcctSecret(self):
		return self.get_query_params().get('SecondaryAcctSecret')

	def set_SecondaryAcctSecret(self,SecondaryAcctSecret):
		self.add_query_param('SecondaryAcctSecret',SecondaryAcctSecret)

	def get_Ieee80211w(self):
		return self.get_query_params().get('Ieee80211w')

	def set_Ieee80211w(self,Ieee80211w):
		self.add_query_param('Ieee80211w',Ieee80211w)

	def get_Network(self):
		return self.get_query_params().get('Network')

	def set_Network(self,Network):
		self.add_query_param('Network',Network)

	def get_Isolate(self):
		return self.get_query_params().get('Isolate')

	def set_Isolate(self,Isolate):
		self.add_query_param('Isolate',Isolate)

	def get_ApAssetId(self):
		return self.get_query_params().get('ApAssetId')

	def set_ApAssetId(self,ApAssetId):
		self.add_query_param('ApAssetId',ApAssetId)

	def get_EncKey(self):
		return self.get_query_params().get('EncKey')

	def set_EncKey(self,EncKey):
		self.add_query_param('EncKey',EncKey)

	def get_MulticastForward(self):
		return self.get_query_params().get('MulticastForward')

	def set_MulticastForward(self,MulticastForward):
		self.add_query_param('MulticastForward',MulticastForward)

	def get_Encryption(self):
		return self.get_query_params().get('Encryption')

	def set_Encryption(self,Encryption):
		self.add_query_param('Encryption',Encryption)

	def get_Wmm(self):
		return self.get_query_params().get('Wmm')

	def set_Wmm(self,Wmm):
		self.add_query_param('Wmm',Wmm)

	def get_AuthCache(self):
		return self.get_query_params().get('AuthCache')

	def set_AuthCache(self,AuthCache):
		self.add_query_param('AuthCache',AuthCache)

	def get_Disabled(self):
		return self.get_query_params().get('Disabled')

	def set_Disabled(self,Disabled):
		self.add_query_param('Disabled',Disabled)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)

	def get_RadioIndex(self):
		return self.get_query_params().get('RadioIndex')

	def set_RadioIndex(self,RadioIndex):
		self.add_query_param('RadioIndex',RadioIndex)

	def get_IgnoreWeakProbe(self):
		return self.get_query_params().get('IgnoreWeakProbe')

	def set_IgnoreWeakProbe(self,IgnoreWeakProbe):
		self.add_query_param('IgnoreWeakProbe',IgnoreWeakProbe)

	def get_Maxassoc(self):
		return self.get_query_params().get('Maxassoc')

	def set_Maxassoc(self,Maxassoc):
		self.add_query_param('Maxassoc',Maxassoc)

	def get_AcctServer(self):
		return self.get_query_params().get('AcctServer')

	def set_AcctServer(self,AcctServer):
		self.add_query_param('AcctServer',AcctServer)

	def get_SecondaryAuthServer(self):
		return self.get_query_params().get('SecondaryAuthServer')

	def set_SecondaryAuthServer(self,SecondaryAuthServer):
		self.add_query_param('SecondaryAuthServer',SecondaryAuthServer)

	def get_DaeClient(self):
		return self.get_query_params().get('DaeClient')

	def set_DaeClient(self,DaeClient):
		self.add_query_param('DaeClient',DaeClient)

	def get_DaeSecret(self):
		return self.get_query_params().get('DaeSecret')

	def set_DaeSecret(self,DaeSecret):
		self.add_query_param('DaeSecret',DaeSecret)

	def get_DisassocLowAck(self):
		return self.get_query_params().get('DisassocLowAck')

	def set_DisassocLowAck(self,DisassocLowAck):
		self.add_query_param('DisassocLowAck',DisassocLowAck)

	def get_SecondaryAuthPort(self):
		return self.get_query_params().get('SecondaryAuthPort')

	def set_SecondaryAuthPort(self,SecondaryAuthPort):
		self.add_query_param('SecondaryAuthPort',SecondaryAuthPort)

	def get_AcctSecret(self):
		return self.get_query_params().get('AcctSecret')

	def set_AcctSecret(self,AcctSecret):
		self.add_query_param('AcctSecret',AcctSecret)

	def get_DisassocWeakRssi(self):
		return self.get_query_params().get('DisassocWeakRssi')

	def set_DisassocWeakRssi(self,DisassocWeakRssi):
		self.add_query_param('DisassocWeakRssi',DisassocWeakRssi)

	def get_SecondaryAcctPort(self):
		return self.get_query_params().get('SecondaryAcctPort')

	def set_SecondaryAcctPort(self,SecondaryAcctPort):
		self.add_query_param('SecondaryAcctPort',SecondaryAcctPort)

	def get_DaePort(self):
		return self.get_query_params().get('DaePort')

	def set_DaePort(self,DaePort):
		self.add_query_param('DaePort',DaePort)

	def get_SsidLb(self):
		return self.get_query_params().get('SsidLb')

	def set_SsidLb(self,SsidLb):
		self.add_query_param('SsidLb',SsidLb)

	def get_AcctPort(self):
		return self.get_query_params().get('AcctPort')

	def set_AcctPort(self,AcctPort):
		self.add_query_param('AcctPort',AcctPort)

	def get_MaxInactivity(self):
		return self.get_query_params().get('MaxInactivity')

	def set_MaxInactivity(self,MaxInactivity):
		self.add_query_param('MaxInactivity',MaxInactivity)

	def get_VlanDhcp(self):
		return self.get_query_params().get('VlanDhcp')

	def set_VlanDhcp(self,VlanDhcp):
		self.add_query_param('VlanDhcp',VlanDhcp)

	def get_InstantlyEffective(self):
		return self.get_query_params().get('InstantlyEffective')

	def set_InstantlyEffective(self,InstantlyEffective):
		self.add_query_param('InstantlyEffective',InstantlyEffective)

	def get_ShortPreamble(self):
		return self.get_query_params().get('ShortPreamble')

	def set_ShortPreamble(self,ShortPreamble):
		self.add_query_param('ShortPreamble',ShortPreamble)

	def get_AuthSecret(self):
		return self.get_query_params().get('AuthSecret')

	def set_AuthSecret(self,AuthSecret):
		self.add_query_param('AuthSecret',AuthSecret)

	def get_SecondaryAuthSecret(self):
		return self.get_query_params().get('SecondaryAuthSecret')

	def set_SecondaryAuthSecret(self,SecondaryAuthSecret):
		self.add_query_param('SecondaryAuthSecret',SecondaryAuthSecret)

	def get_Ownip(self):
		return self.get_query_params().get('Ownip')

	def set_Ownip(self,Ownip):
		self.add_query_param('Ownip',Ownip)