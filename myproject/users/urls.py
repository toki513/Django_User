from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('register/',views.register_now, name = "register")
]
