from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from jalali_date import datetime2jalali, date2jalali
class Post(models.Model):
    file = models.FileField(null=True)
    subtitle = models.CharField(max_length=255, null=False)
    text = models.TextField(null=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    release_date = models.DateTimeField(auto_now=True)
    tag = models.CharField(null=True, max_length=255)

    @property
    def get_release_date(self):
        return datetime2jalali(self.release_date).strftime('%Y/%m/%d')

    @property
    def get_release_time(self):
        return datetime2jalali(self.release_date).strftime('%H:%M:%S')