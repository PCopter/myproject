from django.urls import path
from . import views
from .views import send_manual_email , trigger_weekly_email


urlpatterns = [
    path('', views.certifications, name='certifications'),
    path('<int:cert_id>/', views.certification, name='certification'),
    path('<str:country_name>/', views.certifications_by_country, name='certifications_by_country'),
    path('country_list', views.country_list , name= 'country_list'),
    path('certification_list/<str:country_name>/', views.certification_list, name='certification_list'),
    path('listview', views.listview , name= 'listview'),
    path('send-email/<int:country_id>/', send_manual_email, name='send_manual_email'),
    path('trigger-weekly-email/', trigger_weekly_email, name='trigger-weekly-email'),
    
    
]

