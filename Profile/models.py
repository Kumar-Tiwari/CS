from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Profile(models.Model):
    profile=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    match_won=models.IntegerField(null=True,blank=True)
