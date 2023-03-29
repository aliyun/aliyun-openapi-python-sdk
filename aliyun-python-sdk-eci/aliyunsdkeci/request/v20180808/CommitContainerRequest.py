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


class CommitContainerRequest(RpcRequest):
    def __init__(self):
        RpcRequest.__init__(self, "Eci", "2018-08-08", "CommitContainer", "eci")

    def set_ContainerGroupId(self, ContainerGroupId):
        self.add_query_param("ContainerGroupId", ContainerGroupId)

    def get_ContainerGroupId(self):
        return self.get_query_params().get("ContainerGroupId")

    def set_ContainerName(self, ContainerName):
        self.add_query_param("ContainerName", ContainerName)

    def get_ContainerName(self):
        return self.get_query_params().get("ContainerName")

    def set_Image(self, Image):
        self.add_query_param("Image.Repository", Image.get("Repository"))
        self.add_query_param("Image.Tag", Image.get("Tag"))
        self.add_query_param("Image.Message", Image.get("Message"))
        self.add_query_param("Image.Author", Image.get("Author"))

    def get_Image(self):
        return self.get_query_params().get("Image")

    def set_AcrRegistryInfo(self, AcrRegistryInfo):
        self.add_query_param("AcrRegistryInfo.InstanceId", AcrRegistryInfo.get("InstanceId"))
        self.add_query_param("AcrRegistryInfo.RegionId", AcrRegistryInfo.get("RegionId"))

    def get_AcrRegistryInfo(self):
        return self.get_query_params().get("AcrRegistryInfo")

    def set_Arn(self, Arn):
        self.add_query_param("Arn.RoleArn", Arn.get("RoleArn"))
        self.add_query_param("Arn.RoleType", Arn.get("RoleType"))

    def get_Arn(self):
        return self.get_query_params().get("Arn")

