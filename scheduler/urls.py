# the 'name' value as called by the {% url %} template tag

from django.urls import path

from . import views

# Set application namespace
app_name = 'scheduler'
urlpatterns = [
# /scheduler/
    path('', views.IndexView.as_view(), name='index'),
    # path('content/', views.ContentView.as_view(), name='content'),
# /scheduler/new/
    path('new/', views.ContentCreateView.as_view(), name='content-add'),
# /scheduler/edit/3/
    path('edit/<int:pk>/', views.ContentUpdateView.as_view(), name='content-update'),
# /scheduler/3/
    path('<int:pk>/', views.ContentDetailView.as_view(), name='content-detail'),
    # path('<int:content>/<int:post>/', views.PostListView.as_view(), name='post-list'),
    path('<int:pk>/<int:post>/', views.PostDetailView.as_view(), name='post-detail'),
]
