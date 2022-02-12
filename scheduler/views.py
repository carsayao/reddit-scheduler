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
        print("[!] DetailView", DetailView)
        print("[!] context", context)
        print("[!] context['content']", context['content'])
        print("[!] context['content'].id", context['content'].id)
        # print("", Post.objects.filter())
        print("[!] self", self)
        print("[!] kwargs", kwargs)
        # Doesn't work
        # print("[!] kwargs['pk']", kwargs['pk'])
        # print("[!] **kwargs", **kwargs)
        print("[!] self.kwargs", self.kwargs)
        # Get pk of current content
        print("[!] self.kwargs['pk']", self.kwargs['pk'])
        print("[!] Post.objects", Post.objects.select_related('content').get(pk=self.kwargs['pk']))
        print("[!] Post.objects", Post.objects.select_related('content').get(pk=2))
        print("[!] Post.objects.all()", Post.objects.all())
        print("[!] Post.objects.select_related('content').filter(content=2)", Post.objects.select_related('content').filter(content=2))
        # Get posts by content
        print("[!] Post.objects.select_related('content').filter(content=self.kwargs['pk'])", Post.objects.select_related('content').filter(content=self.kwargs['pk']))
        return context
        # Maybe try
        # Content.objects.get(id=<int>).post_set.all()

class PostListView(ListView):
    template_name = 'scheduler/content_posts.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        self.content = get_object_or_404(Content, name=self.kwargs['content'])
        return Post.objects.select_relate().filter(content=self.content)

class PostDetailView(DetailView):
    model = Post