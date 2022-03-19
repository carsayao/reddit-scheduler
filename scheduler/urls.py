# the 'name' value as called by the {% url %} template tag

from django.urls import path

from . import views

# Set application namespace
app_name = 'scheduler'
urlpatterns = [
# /scheduler/
    # Temporary index that routes '' to 'content/'
    path('', views.IndexView.as_view(), name='index'),
    # path('', views.ContentListView.as_view(), name='index'),
    path('content/', views.ContentListView.as_view(), name='content-list'),
# /scheduler/new/
    path('content/new/', views.ContentCreateView.as_view(), name='content-add'),
# /scheduler/edit/3/
    path('content/edit/<int:pk>/', views.ContentUpdateView.as_view(), name='content-update'),
# /scheduler/3/
    path('content/<int:pk>/', views.ContentDetailView.as_view(), name='content-detail'),
    # path('<int:content>/<int:post>/', views.PostListView.as_view(), name='post-list'),
    path('content/<int:pk>/<int:post>/', views.PostDetailView.as_view(), name='post-detail'),
]
