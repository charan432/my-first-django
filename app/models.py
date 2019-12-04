from django.db import models
from django.contrib.auth.models import User  # Import users model(hidden)

# Create your models here.


class Contact(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=150)
    phone = models.IntegerField()
    info = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=(
        ('male', 'Male'),
        ('female', 'Female')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateField(auto_now_add=True)

    # this method is added to convert object to string in the admin panel
    def __str__(self):
        return self.name

    # Ordering the fetched data (TO show last inserted record first)
    class Meta:
        ordering = ['-id']  # display records in descening order
