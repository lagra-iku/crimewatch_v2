from django.urls import path
from . import views

urlpatterns = [
    path('', views.officer_list, name='officer_list'),
    path('create/', views.officer_create, name='officer_create'),
    path('update/<int:pk>/', views.officer_update, name='officer_update'),
    path('delete/<int:pk>/', views.officer_delete, name='officer_delete'),
]
