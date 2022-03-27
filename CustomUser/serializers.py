from rest_framework import serializers

from .models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['first_name', 'username', 'email', 'is_staff', '']
