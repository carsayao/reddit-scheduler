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
# /scheduler/3/
    path('<int:pk>/', views.ContentDetailView.as_view(), name='content-detail'),
]
