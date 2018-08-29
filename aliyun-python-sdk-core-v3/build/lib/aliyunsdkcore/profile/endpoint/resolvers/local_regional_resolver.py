from aliyunsdkcore.profile.endpoint.resolvers.resolver import Resolver
import aliyunsdkcore.profile.endpoint.endpoint_profile as endpoint_profile


class LocalRegionalResolver(Resolver):

    def __init__(self):
        pass

    def resolve_endpoint(self, params):
        region_id = params['regionId']
        product = params['product']

        if product.lower() in endpoint_profile.endpoint_config:
            data_point = endpoint_profile.endpoint_config[product.lower()]
            regional_list = data_point['regional_endpoints']
            if regional_list:
                for regional_data in regional_list:
                    if regional_data['region'] == region_id:
                        return True, regional_data['endpoint']

        return False, None
