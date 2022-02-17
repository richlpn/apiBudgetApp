from django.contrib import admin

# Register your models here.
from .models import BillModel

admin.site.register(BillModel)