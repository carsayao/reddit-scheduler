from re import template
from django.http import HttpResponse
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import ContentForm
from .models import User, Content, Post

class IndexView(ListView):
    template_name = 'scheduler/index.html'
    context_object_name = 'content_list'
    def get_queryset(self):
        return Content.objects.all()

class ContentCreateView(CreateView):
    model = Content
    form_class = ContentForm

# class ContentView(DetailView):
#     template_name = 'scheduler/content.html'
#     context_object_name = 'content_list'
#     def get_queryset(self):
#         return Content.objects.all()

class ContentDetailView(DetailView):
    model = Content
    template_name = 'scheduler/content_detail.html'
    # https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-display/#adding-extra-context
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the posts
        context['post_list'] = Post.objects.all()
        print(context)
        return context

class PostListView(ListView):
    template_name = 'scheduler/content_posts.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        self.content = get_object_or_404(Content, name=self.kwargs['content'])
        return Post.objects.select_relate().filter(content=self.content)

class PostDetailView(DetailView):
    model = Post