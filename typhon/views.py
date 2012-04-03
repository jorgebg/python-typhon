from tartarus.django.resources import autodiscover as base_autodiscover, Resource, ModelResource as BaseModelResource

class ModelResource(BaseModelResource):
    pass
        

def autodiscover(root=False):
    return base_autodiscover(root, lambda c: c!=ModelResource)