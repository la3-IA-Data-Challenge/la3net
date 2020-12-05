"""
URL configurations for app
"""

from django.urls import path
from app import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('files/', views.FileList.as_view()),
    path('files/<int:pk>/', views.FileDetail.as_view()),
    path('datasets/', views.DatasetList.as_view()),
    path('datasets/<int:pk>/', views.DatasetDetail.as_view()),
    path('similarities/', views.DatasetList.as_view()),
    path('similarities/<int:pk>/', views.DatasetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
