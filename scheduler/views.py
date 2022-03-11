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
        context['post_list'] = Post.objects.select_related('content').filter(content=self.kwargs['pk'])

        print()

        # print("[!] DetailView", DetailView)
        # <class 'django.views.generic.detail.DetailView'>

        # print("[!] context", context)
        # {'object': <Content: test 1>, 'content': <Content: test 1>, 'view': <scheduler.views.ContentDetailView object at 0x7f317c5d3ca0>, 'post_list': <QuerySet [<Post: post 1>, <Post: post 2>, <Post: post 3>]>}

        print("[!] context['post_list']", context['post_list'])

        # print("[!] context['content']", context['content'])
        # test 1

        # print("[!] context['content'].id", context['content'].id)
        # 1

        # print("[!] self", self)
        # <scheduler.views.ContentDetailView object at 0x7f317c5d3ca0>

        # print("[!] kwargs", kwargs)
        # {'object': <Content: test 1>}

        # print("[!] kwargs['pk']", kwargs['pk'])   # Doesn't work
        # print("[!] **kwargs", **kwargs)   # Doesn't work

        # print("[!] self.kwargs", self.kwargs)
        # {'pk': 1}

        # print("[!] self.kwargs['pk']", self.kwargs['pk'])   # Get pk of current content
        # 1
        
        # print("[!] Post.objects", Post.objects.select_related('content').get(pk=self.kwargs['pk']))
        # post 1

        # print("[!] Post.objects", Post.objects.select_related('content').get(pk=2))
        # post 2

        # print("[!] Post.objects.all()", Post.objects.all())
        # <QuerySet [<Post: post 1>, <Post: post 2>, <Post: post 3>]>

        # print("[!] Post.objects.select_related('content').filter(content=2)", Post.objects.select_related('content').filter(content=2))
        # <QuerySet [<Post: post 2>, <Post: post 3>]>

        # Get posts by content
        print("[!] Post.objects.select_related('content').filter(content=self.kwargs['pk'])", Post.objects.select_related('content').filter(content=self.kwargs['pk']))
        # <QuerySet [<Post: post 1>]>

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