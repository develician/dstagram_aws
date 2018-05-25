from django.urls import path
from django.views.generic import DetailView

from Photo import views
from Photo.models import Photo
from Photo.views import post_list

app_name = 'Photo'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('single/<int:pk>/', DetailView.as_view(model=Photo, template_name='photo/post_detail.html'), name='post_detail'),
    path('upload/', views.UploadView.as_view(), name='photo_create'),
    path('delete/<int:pk>/', views.PhotoDeleteView.as_view(), name='post_delete'),
    path('update/<int:pk>/', views.PhotoUpdateView.as_view(), name='post_update'),
]
