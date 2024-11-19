from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    is_enabled = models.BooleanField(default=False)
    publish_date = models.DateField(null=True)
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()


