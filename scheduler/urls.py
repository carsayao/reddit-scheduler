from django.urls import path

from . import views

# Set application namespace
app_name = 'scheduler'
urlpatterns = [
    # the 'name' value as called by the {% url %} template tag

    # /scheduler/
    path('', views.index, name='index'),
    # /scheduler/1/
    # path('<int:user_id>/', views.detail, name='detail'),
    # /scheduler/1/user/
    path('<int:user_id>/user/', views.user, name='user'),
    # /scheduler/1/content/
    path('<int:user_id>/content/', views.content, name='content'),
    # /scheduler/u_id/content/c_id/
    path('<int:user_id>/content/<int:content_id>/', views.content_detail, name='content_detail')
]