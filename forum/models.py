from django.db import models

# Create your models here.

Gender = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other")
)

class Account(models.Model):
    phone_no = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    gender = models.CharField(
        max_length=6,
        choices=Gender
    )
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=250)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(
        Account, 
        related_name="like_post",
        blank=True
    )
    image = models.FileField()
