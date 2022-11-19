from django.db import models

# Create your models here.
class post (models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    category = models.CharField(max_length=100)
    datePost = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "{}. {}".format(self.id,self.title)