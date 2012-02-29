from tartarus.django.resources import autodiscover as base_autodiscover, Resource, ModelResource as BaseModelResource, ResourceHelper
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

class ModelResource(BaseModelResource):

    class List(ListView):
        def get_template_names(self):
            return super(ListView, self).get_template_names() + [ 'model%s.html' % self.template_name_suffix ]
        def get_context_data(self, **kwargs):
            context = super(ListView, self).get_context_data(**kwargs)
            ResourceHelper.update_context_data(self, context)
            return context
    
    class Detail(DetailView):
        def get_template_names(self):
            return super(DetailView, self).get_template_names() + [ 'model%s.html' % self.template_name_suffix ]
        def get_context_data(self, **kwargs):
            context = super(DetailView, self).get_context_data(**kwargs)
            ResourceHelper.update_context_data(self, context)
            return context
    
    class Create(CreateView):
        def get_template_names(self):
            return super(CreateView, self).get_template_names() + [ 'model%s.html' % self.template_name_suffix ]
        def get_context_data(self, **kwargs):
            context = super(CreateView, self).get_context_data(**kwargs)
            ResourceHelper.update_context_data(self, context)
            return context
    
    class Update(UpdateView):
        def get_template_names(self):
            return super(UpdateView, self).get_template_names() + [ 'model%s.html' % self.template_name_suffix ]
        def get_context_data(self, **kwargs):
            context = super(UpdateView, self).get_context_data(**kwargs)
            ResourceHelper.update_context_data(self, context)
            return context
    
    class Delete(DeleteView):
        def get_template_names(self):
            return super(DeleteView, self).get_template_names() + [ 'model%s.html' % self.template_name_suffix ]
        def get_context_data(self, **kwargs):
            context = super(DeleteView, self).get_context_data(**kwargs)
            ResourceHelper.update_context_data(self, context)
            return context
        

def autodiscover(root=False):
    return base_autodiscover(root, lambda c: c!=ModelResource)