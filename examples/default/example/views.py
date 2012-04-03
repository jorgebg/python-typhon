from tartarus.django.resources import Resource, ResourceView as View
from tartarus.django.sort import Choice
from typhon.views import ModelResource
from django.conf import settings
from example.models import Post
from django_easyfilters.filters import ValuesFilter

class Home(Resource):
    pattern = '^'
    class Default(View):
        template_name = 'home.html'
            

class Posts(ModelResource):
    model = Post
    class List(ModelResource.List):
        default_order = 'newer_first'
        class Sort:
            title = Choice('title')
            content_and_title = Choice('title', 'content')
            newer_first = Choice('date', label='Date: New to old')
            older_first = Choice('-date', label='Date: Old to new')
            length = Choice('length', extra={'select':{'length':'Length(content)'}})
        class Filter:
            fields = [
                'title',
                ('date', {}, ValuesFilter),
                ]
            