from django.urls import path
from .views import CreateUserView

urlpatterns = [
    path("", CreateUserView.as_view(), name="register_user"),

]

