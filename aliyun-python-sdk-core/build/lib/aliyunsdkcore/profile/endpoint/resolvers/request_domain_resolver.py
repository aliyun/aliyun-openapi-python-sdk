from aliyunsdkcore.profile.endpoint.resolvers.resolver import Resolver


class RequestDomainResolver(Resolver):
    def __init__(self):
        pass

    def resolve_endpoint(self, params):
        if 'requestDomain' in params:
            domain = params['requestDomain']
            if domain:
                return True, domain

        return False, None
