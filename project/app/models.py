from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)
    def __str__(self):
        return self.title