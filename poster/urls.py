from django.urls import path

from . import views

# Set application namespace
app_name = 'poster'
urlpatterns = [
    # /poster/
    path('', views.index, name='index'),
    # /poster/5/
    path('<int:user_id>/', views.detail, name='detail'),
    # /poster/5/user/
    path('<int:user_id>/user/', views.user, name='user')
]