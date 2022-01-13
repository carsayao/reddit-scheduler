from django.http import HttpResponse
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import User, Content

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'scheduler/index.html'
    context_object_name = 'content_list'
    def get_queryset(self):
        return Content.objects.all()

class UserView(generic.DetailView):
    pass

# Raise the Http404 exception if a user with the requested ID doesn’t exist.
def detail(request, user_id):
    # return HttpResponse("You're looking at user %s." % user_id)

    # try:
    #     user = User.objects.get(pk=user_id)
    # except User.DoesNotExist:
    #     raise Http404("User does not exist")
    # return render(request, 'scheduler/detail.html', {'user': user})

    user = get_object_or_404(User, pk=user_id)
    return render(request, 'scheduler/detail.html', {'user': user})

def user(request, user_id):
    # return HttpResponse("You're looking at the name of %s." % user_id)
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'scheduler/content.html', {'user': user})

class ContentView(generic.DetailView):
    # model = User
    template_name = 'scheduler/content.html'
    context_object_name = 'content_list'
    def get_queryset(self):
        return User.content_set
    # def get_queryset(self):
    #     return User

# def content(request, user_id):
#     # print(f"USER ID: {user_id}")
#     user = get_object_or_404(User, pk=user_id)
#     # print(f"USER ID: {user_id}")
#     # print(f"USER CONTENT: {user.content_set.all()}")
#     return render(request, 'scheduler/content.html', {'user': user})

class ContentDetailView(generic.DetailView):
    model = Content
    template_name = 'scheduler/content_detail.html'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context
        
# def content_detail(request, content_id):
#     """ View details of content """
#     content = get_object_or_404(Content, pk=content_id)
#     return render(request, 'scheduler/content_detail.html', {'content': content, 'user': user})