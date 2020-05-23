from django.urls import path

from . import views

urlpatterns = [
    path('', views.display),
    path('country/<str:country>/', views.display_country)


]
