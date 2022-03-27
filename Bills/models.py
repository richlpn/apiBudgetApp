from django.db import models
from CustomUser.models import Users


# Create your models here.
class BillModel(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    tittle = models.CharField(max_length=60)
    description = models.CharField(max_length=200, blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    creation_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True)

    def __str__(self):
        return f"user:{self.user} " \
               f"tittle:{self.tittle} " \
               f"value:{self.value} "\
               f"creation_date:{self.creation_date} "\
               f"due_date:{self.due_date} "
