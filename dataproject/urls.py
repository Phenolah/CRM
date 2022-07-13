
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("accounts.urls")),
    path("customer/", include("accounts.urls")),
    path("products/", include("accounts.urls"))



]
