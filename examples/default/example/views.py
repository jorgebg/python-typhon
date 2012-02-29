from tartarus.django.resources import Resource, View
from typhon.views import ModelResource
from django.conf import settings
from example.models import Post

class Home(Resource):
    pattern = ''
    class Default(View):
        template_name = 'home.html'
        def get_context_data(self, **kwargs):
            return {
                'project_name': settings.PROJECT_NAME
            }
            

class Posts(ModelResource):
    model = Post