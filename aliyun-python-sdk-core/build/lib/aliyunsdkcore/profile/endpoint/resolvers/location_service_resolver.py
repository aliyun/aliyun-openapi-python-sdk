from aliyunsdkcore.profile.endpoint.resolvers.resolver import Resolver
import aliyunsdkcore.profile.endpoint.endpoint_profile as endpoint_profile


class LocationServiceResolver(Resolver):
    def __init__(self):
        pass

    def resolve_endpoint(self, params):
        location_product = params['locationProduct']
        endpoint_type = params['endpointType']
        product = params['product']
        region_id = params['regionId']
        location_service = params['locationService']

        if not location_product or len(location_product) == 0:
            # load service code from endpoint configs
            if product.lower() in endpoint_profile.endpoint_config:
                data_point = endpoint_profile.endpoint_config[product.lower()]
                if data_point:
                    location_product = data_point['location_service_code']

        if not location_product or len(location_product) == 0:
            return False, None

        if not endpoint_type or len(endpoint_type) == 0:
            endpoint_type = 'openAPI'

        endpoint = location_service.find_product_domain(region_id, location_product, product, endpoint_type)

        if endpoint and len(endpoint) > 0:
            return True, endpoint
        else:
            return False, None
