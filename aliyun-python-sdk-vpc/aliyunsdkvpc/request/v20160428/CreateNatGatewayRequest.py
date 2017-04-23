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


class CreateNatGatewayRequest(RpcRequest):
    def __init__(self):
        RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'CreateNatGateway', 'vpc')

    def get_OwnerId(self):
        return self.get_query_params().get('OwnerId')

    def set_OwnerId(self, OwnerId):
        self.add_query_param('OwnerId', OwnerId)

    def get_ResourceOwnerAccount(self):
        return self.get_query_params().get('ResourceOwnerAccount')

    def set_ResourceOwnerAccount(self, ResourceOwnerAccount):
        self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)

    def get_ResourceOwnerId(self):
        return self.get_query_params().get('ResourceOwnerId')

    def set_ResourceOwnerId(self, ResourceOwnerId):
        self.add_query_param('ResourceOwnerId', ResourceOwnerId)

    def get_OwnerAccount(self):
        return self.get_query_params().get('OwnerAccount')

    def set_OwnerAccount(self, OwnerAccount):
        self.add_query_param('OwnerAccount', OwnerAccount)

    def get_VpcId(self):
        return self.get_query_params().get('VpcId')

    def set_VpcId(self, VpcId):
        self.add_query_param('VpcId', VpcId)

    def get_Name(self):
        return self.get_query_params().get('Name')

    def set_Name(self, Name):
        self.add_query_param('Name', Name)

    def get_Description(self):
        return self.get_query_params().get('Description')

    def set_Description(self, Description):
        self.add_query_param('Description', Description)

    def get_ClientToken(self):
        return self.get_query_params().get('ClientToken')

    def set_ClientToken(self, ClientToken):
        self.add_query_param('ClientToken', ClientToken)

    def get_Spec(self):
        return self.get_query_params().get('Spec')

    def set_Spec(self, Spec):
        self.add_query_param('Spec', Spec)

    def set_BandwidthPackage_1_IpCount(self, BandwidthPackage_1_IpCount):
        self.add_query_param('BandwidthPackage.1.IpCount', BandwidthPackage_1_IpCount)


    def get_BandwidthPackage_1_IpCount(self):
        self.get_query_params().get('BandwidthPackage.1.IpCount')


    def set_BandwidthPackage_2_IpCount(self, BandwidthPackage_2_IpCount):
        self.add_query_param('BandwidthPackage.2.IpCount', BandwidthPackage_2_IpCount)


    def get_BandwidthPackage_2_IpCount(self):
        self.get_query_params().get('BandwidthPackage.2.IpCount')


    def set_BandwidthPackage_3_IpCount(self, BandwidthPackage_3_IpCount):
        self.add_query_param('BandwidthPackage.3.IpCount', BandwidthPackage_3_IpCount)


    def get_BandwidthPackage_3_IpCount(self):
        self.get_query_params().get('BandwidthPackage.3.IpCount')


    def set_BandwidthPackage_4_IpCount(self, BandwidthPackage_4_IpCount):
        self.add_query_param('BandwidthPackage.4.IpCount', BandwidthPackage_4_IpCount)


    def get_BandwidthPackage_4_IpCount(self):
        self.get_query_params().get('BandwidthPackage.4.IpCount')


    def set_BandwidthPackage_1_Bandwidth(self, BandwidthPackage_1_Bandwidth):
        self.add_query_param('BandwidthPackage.1.Bandwidth', BandwidthPackage_1_Bandwidth)


    def get_BandwidthPackage_1_Bandwidth(self):
        self.get_query_params().get('BandwidthPackage.1.Bandwidth')


    def set_BandwidthPackage_2_Bandwidth(self, BandwidthPackage_2_Bandwidth):
        self.add_query_param('BandwidthPackage.2.Bandwidth', BandwidthPackage_2_Bandwidth)


    def get_BandwidthPackage_2_Bandwidth(self):
        self.get_query_params().get('BandwidthPackage.2.Bandwidth')


    def set_BandwidthPackage_3_Bandwidth(self, BandwidthPackage_3_Bandwidth):
        self.add_query_param('BandwidthPackage.3.Bandwidth', BandwidthPackage_3_Bandwidth)


    def get_BandwidthPackage_3_Bandwidth(self):
        self.get_query_params().get('BandwidthPackage.3.Bandwidth')


    def set_BandwidthPackage_4_Bandwidth(self, BandwidthPackage_4_Bandwidth):
        self.add_query_param('BandwidthPackage.4.Bandwidth', BandwidthPackage_4_Bandwidth)


    def get_BandwidthPackage_4_Bandwidth(self):
        self.get_query_params().get('BandwidthPackage.4.Bandwidth')


    def set_BandwidthPackage_1_Zone(self, BandwidthPackage_1_Zone):
        self.add_query_param('BandwidthPackage.1.Zone', BandwidthPackage_1_Zone)


    def get_BandwidthPackage_1_Zone(self):
        self.get_query_params().get('BandwidthPackage.1.Zone')


    def set_BandwidthPackage_2_Zone(self, BandwidthPackage_2_Zone):
        self.add_query_param('BandwidthPackage.2.Zone', BandwidthPackage_2_Zone)


    def get_BandwidthPackage_2_Zone(self):
        self.get_query_params().get('BandwidthPackage.2.Zone')


    def set_BandwidthPackage_3_Zone(self, BandwidthPackage_3_Zone):
        self.add_query_param('BandwidthPackage.3.Zone', BandwidthPackage_3_Zone)


    def get_BandwidthPackage_3_Zone(self):
        self.get_query_params().get('BandwidthPackage.3.Zone')


    def set_BandwidthPackage_4_Zone(self, BandwidthPackage_4_Zone):
        self.add_query_param('BandwidthPackage.4.Zone', BandwidthPackage_4_Zone)


    def get_BandwidthPackage_4_Zone(self):
        self.get_query_params().get('BandwidthPackage.4.Zone')


    def set_BandwidthPackage_1_ISP(self, BandwidthPackage_1_ISP):
        self.add_query_param('BandwidthPackage.1.ISP', BandwidthPackage_1_ISP)


    def get_BandwidthPackage_1_ISP(self):
        self.get_query_params().get('BandwidthPackage.1.ISP')


    def set_BandwidthPackage_2_ISP(self, BandwidthPackage_2_ISP):
        self.add_query_param('BandwidthPackage.2.ISP', BandwidthPackage_2_ISP)


    def get_BandwidthPackage_2_ISP(self):
        self.get_query_params().get('BandwidthPackage.2.ISP')


    def set_BandwidthPackage_3_ISP(self, BandwidthPackage_3_ISP):
        self.add_query_param('BandwidthPackage.3.ISP', BandwidthPackage_3_ISP)


    def get_BandwidthPackage_3_ISP(self):
        self.get_query_params().get('BandwidthPackage.3.ISP')


    def set_BandwidthPackage_4_ISP(self, BandwidthPackage_4_ISP):
        self.add_query_param('BandwidthPackage.4.ISP', BandwidthPackage_4_ISP)


    def get_BandwidthPackage_4_ISP(self):
        self.get_query_params().get('BandwidthPackage.4.ISP')
