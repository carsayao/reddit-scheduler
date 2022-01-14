# the 'name' value as called by the {% url %} template tag

from django.urls import path

from . import views

# Set application namespace
app_name = 'scheduler'
urlpatterns = [
# /scheduler/
    path('', views.IndexView.as_view(), name='index'),
# /scheduler/new/
    path('new/', views.NewContent.as_view(), name='new_content'),
# /scheduler/3/
    path('<int:pk>/', views.ContentDetailView.as_view(), name='content_detail'),
]
