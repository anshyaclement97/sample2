from django.db import models
from django.contrib.auth.models import User #username,email , password ,firstname,lastname
# Create your models here.



class regmodel(models.Model):
        username = models.CharField(max_length=30)
        email = models.EmailField()
        password = models.CharField(max_length=20)





class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)


