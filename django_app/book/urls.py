from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookHome),
    path('list/', views.list),
]
