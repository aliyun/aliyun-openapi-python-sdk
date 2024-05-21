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
class SaveApRadioConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudwf', '2017-03-28', 'SaveApRadioConfig','cloudwf')

	def get_RequireMode(self):
		return self.get_query_params().get('RequireMode')

	def set_RequireMode(self,RequireMode):
		self.add_query_param('RequireMode',RequireMode)

	def get_Htmode(self):
		return self.get_query_params().get('Htmode')

	def set_Htmode(self,Htmode):
		self.add_query_param('Htmode',Htmode)

	def get_Frag(self):
		return self.get_query_params().get('Frag')

	def set_Frag(self,Frag):
		self.add_query_param('Frag',Frag)

	def get_Minrate(self):
		return self.get_query_params().get('Minrate')

	def set_Minrate(self,Minrate):
		self.add_query_param('Minrate',Minrate)

	def get_McastRate(self):
		return self.get_query_params().get('McastRate')

	def set_McastRate(self,McastRate):
		self.add_query_param('McastRate',McastRate)

	def get_Probereq(self):
		return self.get_query_params().get('Probereq')

	def set_Probereq(self,Probereq):
		self.add_query_param('Probereq',Probereq)

	def get_Channel(self):
		return self.get_query_params().get('Channel')

	def set_Channel(self,Channel):
		self.add_query_param('Channel',Channel)

	def get_Shortgi(self):
		return self.get_query_params().get('Shortgi')

	def set_Shortgi(self,Shortgi):
		self.add_query_param('Shortgi',Shortgi)

	def get_Hwmode(self):
		return self.get_query_params().get('Hwmode')

	def set_Hwmode(self,Hwmode):
		self.add_query_param('Hwmode',Hwmode)

	def get_Uapsd(self):
		return self.get_query_params().get('Uapsd')

	def set_Uapsd(self,Uapsd):
		self.add_query_param('Uapsd',Uapsd)

	def get_BeaconInt(self):
		return self.get_query_params().get('BeaconInt')

	def set_BeaconInt(self,BeaconInt):
		self.add_query_param('BeaconInt',BeaconInt)

	def get_Mac(self):
		return self.get_query_params().get('Mac')

	def set_Mac(self,Mac):
		self.add_query_param('Mac',Mac)

	def get_Rts(self):
		return self.get_query_params().get('Rts')

	def set_Rts(self,Rts):
		self.add_query_param('Rts',Rts)

	def get_Txpower(self):
		return self.get_query_params().get('Txpower')

	def set_Txpower(self,Txpower):
		self.add_query_param('Txpower',Txpower)

	def get_Noscan(self):
		return self.get_query_params().get('Noscan')

	def set_Noscan(self,Noscan):
		self.add_query_param('Noscan',Noscan)

	def get_BcastRate(self):
		return self.get_query_params().get('BcastRate')

	def set_BcastRate(self,BcastRate):
		self.add_query_param('BcastRate',BcastRate)

	def get_Disabled(self):
		return self.get_query_params().get('Disabled')

	def set_Disabled(self,Disabled):
		self.add_query_param('Disabled',Disabled)

	def get_InstantlyEffective(self):
		return self.get_query_params().get('InstantlyEffective')

	def set_InstantlyEffective(self,InstantlyEffective):
		self.add_query_param('InstantlyEffective',InstantlyEffective)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)

	def get_RadioIndex(self):
		return self.get_query_params().get('RadioIndex')

	def set_RadioIndex(self,RadioIndex):
		self.add_query_param('RadioIndex',RadioIndex)