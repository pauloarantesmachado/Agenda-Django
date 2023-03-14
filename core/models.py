from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(blank=True, null=type)
  event_date = models.DateTimeField(verbose_name='Data do evento')
  create_date = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  class Meta:
    db_table = 'event'

  def __str__(self):
    return self.title