from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.home_page),
    path("customer/", views.customer),
    path("products/", views.products, name = "product"),


]