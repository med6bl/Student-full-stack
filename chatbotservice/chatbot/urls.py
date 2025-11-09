from django.urls import path
from .views import summarize_view, translate_view

urlpatterns = [
    path('api/summarize/', summarize_view, name='summarize'),
    path('api/translate/', translate_view, name='translate'),
]
