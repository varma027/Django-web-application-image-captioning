from django.urls import path
from . import views  # Correct import from the current directory

urlpatterns = [
    path('', views.home_view, name='home'),
    path('result/', views.result_view, name='result'),
]

