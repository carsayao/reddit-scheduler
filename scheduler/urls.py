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
    path('content/<int:pk>/edit/', views.ContentUpdateView.as_view(), name='content-update'),
# /scheduler/3/delete/
    path('content/<int:pk>/delete/', views.ContentDeleteView.as_view(), name='content-delete'),
# /scheduler/3/
    path('content/<int:pk>/', views.ContentDetailView.as_view(), name='content-detail'),
    # path('<int:content>/<int:post>/', views.PostListView.as_view(), name='post-list'),
    # I don't know why I have to reverse this, but it works.
    # Trying '<pk>/<post>/' gives me a backwards url and can't access all posts.
    # Pay attention to order in content_detail.html as well.
    path('content/<int:post>/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
]
