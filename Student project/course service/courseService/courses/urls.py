from django.urls import path, include   
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('courses/', views.get_courses),
    path('courses/add/', views.add_course),
    path('courses/<int:id>/update/', views.update_course),
    path('courses/<int:id>/delete/', views.delete_course),
    path('courses/search/', views.search_course),
    path('courses/enroll/', views.enroll_student),
    path('courses/<int:id>/students/', views.get_course_students),
    path('students/<int:id>/courses/', views.get_student_courses),
]