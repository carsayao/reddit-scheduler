from django.http import HttpResponse
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import User, Content

class IndexView(generic.ListView):
    template_name = 'scheduler/index.html'
    context_object_name = 'content_list'
    def get_queryset(self):
        return Content.objects.all()

class NewContent(generic.DetailView):
    pass

class ContentView(generic.DetailView):
    template_name = 'scheduler/content.html'
    context_object_name = 'content_list'
    def get_queryset(self):
        return User.content_set

class ContentDetailView(generic.DetailView):
    model = Content
    template_name = 'scheduler/content_detail.html'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context