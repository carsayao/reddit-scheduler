from django.urls import path

from . import views

# Set application namespace
app_name = 'scheduler'
urlpatterns = [
    # the 'name' value as called by the {% url %} template tag

    # /scheduler/
    path('', views.IndexView.as_view(), name='index'),
    # /scheduler/1/
    # path('<int:user_id>/', views.detail, name='detail'),
    # /scheduler/1/user/
    path('<int:user_id>/user/', views.UserView.as_view(), name='user'),

    # /scheduler/1/content/
    # path('<int:user_id>/content/', views.ContentView.as_view(), name='content'),

    # path('<int:user_id>/content/', views.content, name='content'),
    # /scheduler/u_id/content/c_id/
    # path('<int:user_id>/content/<int:content_id>/', views.Content_detailView.as_view(), name='content_detail')
    # path('content/<int:content_id>/', views.content_detail, name='content_detail'),

    # path('<int:content_id>/', views.content_detail, name='content_detail')
    path('<int:pk>/', views.ContentDetailView.as_view(), name='content_detail')
]