from django.urls import path
from . import views

urlpatterns = [
    path('', views.case_list, name='case_list'),
    path('create/', views.case_create, name='case_create'),
    path('update/<int:pk>/', views.case_update, name='case_update'),
    path('delete/<int:pk>/', views.case_delete, name='case_delete'),
    path('ajax/load-subcategories/', views.load_subcategories, name='ajax_load_subcategories'),
    path('open-cases/', views.open_cases_list, name='open_cases_list'),
    path('closed-cases/', views.closed_cases_list, name='closed_cases_list'),
]
