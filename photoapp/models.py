from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class PhotoModel(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_title = models.CharField(max_length=50)
    photo_description = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='images', blank=False)

    def __str__(self):
        return self.photo_title, self.user
