from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chart/<str:coin_id>/', views.chart, name='chart'),
]

