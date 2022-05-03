from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class post(models.Model):
    #TODO add this fields ==> 1.iamge 2.text 3.writer 4.tags
    file = models.FileField(null=True)
    text = models.TextField(null=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    release_date = models.DateField(auto_now=True)
    tag = models.CharField(null=True, max_length=255)


