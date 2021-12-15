from django.urls import path

from . import views

# Set application namespace
app_name = 'poster'
urlpatterns = [
    # the 'name' value as called by the {% url %} template tag

    # /poster/
    path('', views.index, name='index'),
    # /poster/1/
    # path('<int:user_id>/', views.detail, name='detail'),
    # /poster/1/user/
    path('<int:user_id>/user/', views.user, name='user'),
    # /poster/1/content/
    path('<int:user_id>/content/', views.content, name='content'),
    # /poster/u_id/content/c_id/
    path('<int:user_id>/content/<int:content_id>/', views.content_detail, name='content_detail')
]