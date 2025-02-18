from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('upload/', views.upload_chat, name='upload'),
]