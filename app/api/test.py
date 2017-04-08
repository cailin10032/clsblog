from base import register, BaseResource

@register.register_resource()
class TestResource(BaseResource):
    def get(self):
        return self.response(data='hello, world')
