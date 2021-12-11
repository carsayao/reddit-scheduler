from django.urls import path

from . import views

# Set application namespace
app_name = 'posts'
urlpatterns = [
    # /posts/
    path('', views.index, name='index'),
    # /posts/5/
    path('<int:user_id>/', views.detail, name='detail'),
    # /posts/5/user/
    path('<int:user_id>/user/', views.user, name='user')
]