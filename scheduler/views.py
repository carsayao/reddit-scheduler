from django.http import HttpResponse
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import User, Content

# Create your views here.
def index(request):
    # Load a template, fill a context and return an HttpResponse object with
    # the result of the rendered template
    # username_list = User.objects.all()
    # template = loader.get_template('scheduler/index.html')
    # context = {
    #     'username_list': username_list,
    # }
    # return HttpResponse(template.render(context, request))

    # Shortcut for common load, fill context, return HttpResponse object
    # w/result of the rendered template.
    username_list = User.objects.all()
    # The context is a dictionary mapping template variable names to
    # Python objects.
    context = {
        'username_list': username_list,
    }
    return render(request, 'scheduler/index.html', context)

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

def content(request, user_id):
    # print(f"USER ID: {user_id}")
    user = get_object_or_404(User, pk=user_id)
    # print(f"USER ID: {user_id}")
    # print(f"USER CONTENT: {user.content_set.all()}")
    return render(request, 'scheduler/content.html', {'user': user})

def content_detail(request, content_id, user_id):
    content = get_object_or_404(Content, pk=content_id)
    user = get_object_or_404(User, pk=user_id)
    # return render(request, 'scheduler/content_detail.html', {'content': content})
    return render(request, 'scheduler/content_detail.html', {'content': content, 'user': user})