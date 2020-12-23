from django.db import models

# Create your models here.
class Taskinfo(models.Model):
    task = models.CharField(max_length=100, blank=True, default='')
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User',related_name='tasks',on_delete=models.CASCADE,default='')