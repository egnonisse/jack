from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('visitor', 'Visiteur'),
        ('provider', 'Fournisseur'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='visitor')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.username

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='provider_profile', null='True')  # Enlever `null=True`
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    social_media = models.URLField(blank=True, null=True)
    opening_hours = models.CharField(max_length=255)
    description = models.TextField()
    categories = models.ManyToManyField(ServiceCategory)  # Association avec les catégories
    average_rating = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def get_media(self):
        return self.media_set.all()  # Récupère tous les médias associés

class Review(models.Model):
    provider = models.ForeignKey(Provider, related_name="reviews", on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user_name} for {self.provider.name}"

class Media(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video')
    ]
    
    provider = models.ForeignKey(Provider, related_name='media_set', on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/')
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES)

    def __str__(self):
        return f"{self.media_type} for {self.provider.name}"
