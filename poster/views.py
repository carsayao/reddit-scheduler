from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import User

# Create your views here.
def index(request):
    username_list = User.objects.all()
    template = loader.get_template('poster/index.html')
    # The context is a dictionary mapping template variable names to
    # Python objects.
    context = {
        'username_list': username_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'poster/index.html', context)

# Raise the Http404 exception if a user with the requested ID doesn’t exist.
def detail(request, user_id):
    # return HttpResponse("You're looking at user %s." % user_id)

    # try:
    #     user = User.objects.get(pk=user_id)
    # except User.DoesNotExist:
    #     raise Http404("User does not exist")
    # return render(request, 'poster/detail.html', {'user': user})

    user = get_object_or_404(User, pk=user_id)
    return render(request, 'poster/detail.html', {'user': user})

def user(request, user_id):
    return HttpResponse("You're looking at the name of %s." % user_id)