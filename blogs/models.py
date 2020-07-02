from django.db import models

class Blog(models.Model):
    title = models.CharField(blank=False, null=False, max_length=150)
    text = models.TextField(blank=True)
    create_datetime = models.DateTimeField(auto_now_add=True)
    updata_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
