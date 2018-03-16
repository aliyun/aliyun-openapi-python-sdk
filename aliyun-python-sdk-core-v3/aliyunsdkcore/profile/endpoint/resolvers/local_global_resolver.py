from aliyunsdkcore.profile.endpoint.resolvers.resolver import Resolver
import aliyunsdkcore.profile.endpoint.endpoint_profile as endpoint_profile


class LocalGlobalResolver(Resolver):
    def __init__(self):
        pass

    def resolve_endpoint(self, params):
        product = params['product']

        if product.lower() in endpoint_profile.endpoint_config:
            data_point = endpoint_profile.endpoint_config[product.lower()]
            global_endpoint = data_point['global_endpoint']
            if len(global_endpoint) > 0:
                return True, global_endpoint

        return False, None
