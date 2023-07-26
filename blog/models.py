from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100, help_text="This is a title field")
    author = models.CharField(max_length=100, null=True)
    price = models.IntegerField(null=True)
    def __str__(self):
        return self.title
