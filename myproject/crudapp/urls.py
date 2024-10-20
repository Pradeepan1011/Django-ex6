from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_student, name='create_student'),
    path('students/', views.student_list, name='student_list'),
    path('update/<int:pk>/', views.update_student, name='update_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),
]