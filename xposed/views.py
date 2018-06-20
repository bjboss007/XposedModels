from django.shortcuts import render,reverse
from .forms import RegistratonForm
from django.views.generic import  ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, FormView
from .models import Xposed_models,Pictures,Gallery



class IndexView(ListView):
    model = Xposed_models
    context_object_name = 'xmodels'
    template_name = "index.html"

class ModelsDetail(DetailView):
    model = Xposed_models
    template_name = 'detail.html'
    context_object_name = 'xmodels'

class AboutView(TemplateView):
    template_name = "about.html"

class CreateView(CreateView):
    model = Xposed_models
    form_class = RegistratonForm
    template_name = 'registration.html'
    success_url = 'xposed:index'
    


class GalleryView(ListView):
    context_object_name = 'picture_list'
    template_name = "gallery.html"

    def get_queryset(self): 
        return Gallery.objects.order_by("date")

    
