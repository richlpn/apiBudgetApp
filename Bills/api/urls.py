from django.urls import path
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from ..views import BillView

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token_obtain'),
    path('bill/', BillView.as_view(), name='bill_obtain'),

]
