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

# coding=utf-8

import datetime
import json

from ..request import RpcRequest
from ..http.http_response import HttpResponse
from ..acs_exception import exceptions as exs
from ..acs_exception import error_code, error_msg

LOCATION_SERVICE_PRODUCT_NAME = "Location"
LOCATION_SERVICE_DOMAIN = "location-readonly.aliyuncs.com"
LOCATION_SERVICE_VERSION = "2015-06-12"
LOCATION_SERVICE_DESCRIBE_ENDPOINT_ACTION = "DescribeEndpoints"
LOCATION_SERVICE_REGION = "cn-hangzhou"
LOCATION_CACHE_EXPIRE_TIME = 3600  # Seconds

# location endpoint list
__location_endpoints = dict()
__last_cache_clear_time_per_product = dict()
__location_service_domain = 'location-readonly.aliyuncs.com'


class DescribeEndpointRequest(RpcRequest):
    def __init__(
            self,
            product_name,
            version,
            action_name,
            region_id,
            service_code,
            endpoint_type):
        RpcRequest.__init__(self, product_name, version, action_name)

        self.add_query_param("Id", region_id)
        self.add_query_param("ServiceCode", service_code)
        self.add_query_param("Type", endpoint_type)
        self.set_accept_format("JSON")


class LocationService:
    def __init__(self, client, timeout=None):
        self.__clinetRef = client
        self.__cache = get_location_endpoints()
        self.__service_product_name = LOCATION_SERVICE_PRODUCT_NAME
        self.__service_domain = get_location_service_domain()
        self.__service_version = LOCATION_SERVICE_VERSION
        self.__service_region = LOCATION_SERVICE_REGION
        self.__service_action = LOCATION_SERVICE_DESCRIBE_ENDPOINT_ACTION
        self.__cache_expire_time = LOCATION_CACHE_EXPIRE_TIME
        self.__last_cache_clear_time_per_product = get_last_cache_clear_time_per_product()
        self._timeout = timeout
        self._location_access_count = 0

    def set_location_service_attr(
            self,
            region=None,
            product_name=None,
            domain=None):
        if region is not None:
            self.__service_region = region

        if domain is not None:
            self.__service_domain = domain

        if product_name is not None:
            self.__service_product_name = product_name

    def find_product_domain(self, region_id, service_code, product_name, endpoint_type):
        key = "%s_&_%s" % (region_id, product_name)
        domain = self.__cache.get(key)
        if domain is None or self.check_endpoint_cache_is_expire(key) is True:
            domain = self.find_product_domain_from_location_service(
                region_id, service_code, endpoint_type)
            if domain is None:
                # set domain as <DomainNotFound> to avoid repeat access to location service
                # when location fetch miss
                self.__cache[key] = '<DomainNotFound>'
            else:
                self.__cache[key] = domain
            self.set_endpoint_cache_update_time(key)

        if domain == '<DomainNotFound>':
            return None
        return domain

    def set_endpoint_cache_update_time(self, key):
        now = datetime.datetime.now()
        self.__last_cache_clear_time_per_product[key] = now

    def check_endpoint_cache_is_expire(self, key):
        last_clear_time = self.__last_cache_clear_time_per_product.get(key)
        if last_clear_time is None:
            return False

        now = datetime.datetime.now()
        elapsed_time = now - last_clear_time
        if now > last_clear_time and elapsed_time.seconds > self.__cache_expire_time:
            return True

        return False

    def find_product_domain_from_location_service(
            self, region_id, service_code, endpoint_type):

        request = DescribeEndpointRequest(self.__service_product_name,
                                          self.__service_version,
                                          self.__service_action,
                                          region_id,
                                          service_code,
                                          endpoint_type)
        self._location_access_count += 1
        try:
            content = request.get_content()
            method = request.get_method()

            signer = getattr(self.__clinetRef, '_signer')
            header, url = signer.sign(self.__service_region, request)
            if self.__clinetRef.get_user_agent() is not None:
                header['User-Agent'] = self.__clinetRef.get_user_agent()
                header['x-sdk-client'] = 'python/2.0.0'
            protocol = request.get_protocol_type()
            response = HttpResponse(
                self.__service_domain,
                url,
                method,
                {} if header is None else header,
                protocol,
                content,
                self.__clinetRef.get_port(),
                timeout=self._timeout)

            status, header, body = response.get_response_object()

            result = json.loads(body.decode('utf-8'))
            if status == 200:
                endpoint = result.get('Endpoints').get('Endpoint')
                if len(endpoint) <= 0:
                    return None
                else:
                    return endpoint[0].get('Endpoint')
            elif 400 <= status < 500:
                # print "serviceCode=" + service_code + " get location error!
                # code=" + result.get('Code') +", message =" +
                # result.get('Message')
                return None
            elif status >= 500:
                # return None instead of throw an exception
                # in case of location service failure
                # SDK still has to work for robustness
                return None
            else:
                raise exs.ClientException(
                    result.get('Code'), result.get('Message'))
        except IOError:
            # return None instead of throw an exception
            # in case of location service unreachable,
            # SDK still has to work for robustness
            return None
        except AttributeError:
            raise exs.ClientException(
                error_code.SDK_INVALID_REQUEST,
                error_msg.get_msg('SDK_INVALID_REQUEST'))


def set_cache(product, region_id, domain):
    if region_id is not None and product is not None and domain is not None:
        key = "%s_&_%s" % (region_id, product)
        __location_endpoints[key] = domain
        __last_cache_clear_time_per_product[key] = datetime.datetime.strptime('2999-01-01 00:00:00',
                                                                              '%Y-%m-%d %H:%M:%S')


def get_location_endpoints():
    return __location_endpoints


def get_last_cache_clear_time_per_product():
    return __last_cache_clear_time_per_product


def set_location_service_domain(domain):
    global __location_service_domain
    if domain is not None:
        __location_service_domain = domain


def get_location_service_domain():
    return __location_service_domain
