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


class CopyDataCacheRequest(RpcRequest):
    def __init__(self):
        RpcRequest.__init__(self, 'Eci', '2018-08-08', 'CopyDataCache', 'eci')

    def get_Bucket(self):
        return self.get_query_params().get("Bucket")

    def set_Bucket(self, Bucket):
        self.add_query_param("Bucket", Bucket)

    def get_Path(self):
        return self.get_query_params().get("Path")

    def set_Path(self, Path):
        self.add_query_param("Path", Path)

    def get_Name(self):
        return self.get_query_params().get("Name")

    def set_Name(self, Name):
        self.add_query_param("Name", Name)

    def get_RetentionDays(self):
        return self.get_query_params().get("RetentionDays")

    def set_RetentionDays(self, RetentionDays):
        self.add_query_param("RetentionDays", RetentionDays)

    def get_ResourceGroupId(self):
        return self.get_query_params().get("ResourceGroupId")

    def set_ResourceGroupId(self, ResourceGroupId):
        self.add_query_param("ResourceGroupId", ResourceGroupId)

    def get_ClientToken(self):
        return self.get_query_params().get("ClientToken")

    def set_ClientToken(self, ClientToken):
        self.add_query_param("ClientToken", ClientToken)

    def get_Tags(self):
        return self.get_query_params().get('Tags')

    def set_Tags(self, Tags):
        for i in range(len(Tags)):
            if Tags[i].get('Key') is not None:
                self.add_query_param('Tag.' + str(i + 1) + '.Key', Tags[i].get('Key'))
            if Tags[i].get('Value') is not None:
                self.add_query_param('Tag.' + str(i + 1) + '.Value', Tags[i].get('Value'))

    def get_DataCacheId(self):
        return self.get_query_params().get("DataCacheId")

    def set_DataCacheId(self, DataCacheId):
        self.add_query_param("DataCacheId", DataCacheId)

    def get_DestinationRegionId(self):
        return self.get_query_params().get("DestinationRegionId")

    def set_DestinationRegionId(self, DestinationRegionId):
        self.add_query_param("DestinationRegionId", DestinationRegionId)