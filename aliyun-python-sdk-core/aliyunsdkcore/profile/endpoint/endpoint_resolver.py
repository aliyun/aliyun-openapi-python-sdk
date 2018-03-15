from aliyunsdkcore.profile.endpoint.resolvers.local_global_resolver import LocalGlobalResolver
from aliyunsdkcore.profile.endpoint.resolvers.local_regional_resolver import LocalRegionalResolver
from aliyunsdkcore.profile.endpoint.resolvers.location_service_resolver import LocationServiceResolver
from aliyunsdkcore.profile.endpoint.resolvers.request_domain_resolver import RequestDomainResolver
from aliyunsdkcore.profile.endpoint.resolvers.user_config_resolver import UserConfigResolver
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception import error_code, error_msg

# sort by priority
resolvers = [
    UserConfigResolver(),
    RequestDomainResolver(),
    LocationServiceResolver(),
    LocalRegionalResolver(),
    LocalGlobalResolver()
]


def resolve_endpoint(region_id, request, location_service):
    param = dict()
    param['regionId'] = region_id
    param['product'] = request.get_product()
    param['locationProduct'] = request.get_location_service_code()
    param['locationService'] = location_service
    param['endpointType'] = request.get_location_endpoint_type()
    if hasattr(request, 'get_domain'):
        param['requestDomain'] = request.get_domain()

    for resolver in resolvers:
        supported, endpoint = resolver.resolve_endpoint(param)
        if supported:
            return endpoint

    raise ClientException(
        error_code.SDK_INVALID_REGION_ID,
        error_msg.get_msg('SDK_INVALID_REGION_ID'))
