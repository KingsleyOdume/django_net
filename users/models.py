from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, RegexValidator
from PIL import Image


# Create your models here.


class MyProfile(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.IntegerField(default=18, validators=[MinValueValidator(18)])
    city = models.TextField(null=True, blank=True)
    country = models.TextField(null=True, blank=True)
    club = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, default="single", choices=(
        ("single", "single"), ("married", "married"), ("widow", "widow"), ("seprated", "seprated"), ("commited", "commited")))
    gender = models.CharField(max_length=20, default="female",
                              choices=(("male", "male"), ("female", "female")))
    phone_no = models.CharField(validators=[RegexValidator(
        "^0?[5-9]{1}\d{9}$")], max_length=15, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{"%s" % self.user.username} MyProfile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
