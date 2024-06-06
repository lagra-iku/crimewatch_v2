from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.criminal_list, name='criminal_list'),
    path('create/', views.criminal_create, name='criminal_create'),
    path('update/<int:pk>/', views.criminal_update, name='criminal_update'),
    path('delete/<int:pk>/', views.criminal_delete, name='criminal_delete'),
    path('female-criminals/', views.female_criminals_list, name='female_criminals_list'),
    path('male-criminals/', views.male_criminals_list, name='male_criminals_list'),
    path('details/<int:pk>/', views.criminal_detail, name='criminal_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)