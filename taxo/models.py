from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):
    level = models.CharField(max_length= 200)
    description = models.TextField()
    image = models.ImageField(upload_to="organism")
    answer = models.CharField(max_length = 200)
    know = models.TextField()
    class Meta:
        ordering = ['level']

    def __str__(self):
        return self.level
    
class Valid(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    asked = models.ForeignKey(Question, on_delete = models.CASCADE)
    finish = models.BooleanField()
    finished_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.asked}"


class Useful(models.Model):
    title = models.CharField(max_length= 20)
    idea = models.ImageField(upload_to='idea')
    back = models.ImageField(upload_to='back')
    good = models.ImageField(upload_to="check")
