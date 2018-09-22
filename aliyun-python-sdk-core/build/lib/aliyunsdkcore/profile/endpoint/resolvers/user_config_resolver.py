from aliyunsdkcore.profile.endpoint.resolvers.resolver import Resolver
import aliyunsdkcore.profile.region_provider as user_config


class UserConfigResolver(Resolver):
    def __init__(self):
        pass

    def resolve_endpoint(self, params):
        product = params['product']
        region_id = params['regionId']

        if product in user_config.user_config_endpoints:
            product_data = user_config.user_config_endpoints[product]
            if region_id in product_data:
                return True, product_data[region_id]

        return False, None
