from django.db import models
from accounts.models import User

class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150)
    is_blacklisted = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name