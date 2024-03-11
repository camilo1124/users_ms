from django.db import models

# Create your models here.

class UserUN(models.Model):

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, null = True)
    last_name = models.CharField(max_length=30, null = True)
    role = models.CharField(max_length=20,null = True)
    date_birth = models.DateField(null=True)
    phone = models.CharField(max_length=10,null = True)
    document_type = models.CharField(max_length=20,null=True)
    document_number = models.CharField(max_length=11,null=True)

