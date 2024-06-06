from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.app, name='app'),
    path('case/new/', views.case_new, name='case_new'),
    path('register_officer', views.register_officers, name='register_officers'),
    path('list', views.case_list, name='case_list'),
    path('case/<int:pk>/', views.case_detail, name='case_detail'),
    
    path('case/<int:pk>/edit/', views.case_edit, name='case_edit'),
    path('create_criminal_record', views.create_criminal_record, name='create_criminal_record'),
    path('admin/', admin.site.urls),
    
]