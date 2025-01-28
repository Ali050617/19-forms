from django.urls import path
from . import views


app_name = 'tests'


urlpatterns = [
    path('tests/', views.test_list, name='test_list'),
    path('tests/create/', views.test_create, name='test_create'),
    path('tests/<int:pk>/edit/', views.test_edit, name='test_edit'),
    path('tests/<int:pk>/delete/', views.delete, name='test_delete'),
    path('questions/<int:pk>/edit/', views.question_edit, name='question_edit'),
]

