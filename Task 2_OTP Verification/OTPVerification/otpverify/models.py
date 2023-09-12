from django.db import models

class ResPasToken(models.Model):
    CurrentUser = models.EmailField(max_length=50,null=True)
    PassToken = models.CharField(max_length=6,null=True)