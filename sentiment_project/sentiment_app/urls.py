from django.urls import path
from . import views  # Correct import from the current directory

urlpatterns = [
    path('', views.home_view, name='home'),
    path('result/', views.result_view, name='result'),
]

from django.contrib import admin
from django.urls import path, include
from sentiment_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('result/', views.result_view, name='result'),
    path('', views.home_view, name='home'),  # Add this line for the root URL
]
