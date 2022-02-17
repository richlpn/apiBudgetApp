from rest_framework import serializers
from .models import BillModel


class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = BillModel
        # fields = ['tittle', 'value', 'description', 'creation_date', 'due_date']
        fields = ['user', 'tittle', 'value', 'due_date', 'id']


