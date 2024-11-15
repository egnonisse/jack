#C:\laragon\www\2024\Nov\12112024\providers\serializers.py

from rest_framework import serializers
from .models import Provider, Review, ServiceCategory, Media, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user_type', 'avatar', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'avatar' in validated_data:
            instance.avatar = validated_data['avatar']
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ['id', 'name']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user_name', 'rating', 'comment', 'created_at']

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'provider', 'file', 'media_type']

class ProviderSerializer(serializers.ModelSerializer):
    media = MediaSerializer(many=True, read_only=True)  # Inclure la sérialisation des médias
    categories = ServiceCategorySerializer(many=True)  # Sérialisation des catégories liées
    avatar = serializers.ImageField(required=False)  # Ajout de l'avatar comme champ d'image
    
    class Meta:
        model = Provider
        fields = ['id', 'name', 'address', 'latitude', 'longitude', 'phone_number', 
                  'email', 'website', 'social_media', 'opening_hours', 'description', 
                  'categories', 'average_rating', 'media', 'avatar']  # Liste des champs à inclure dans l'API

    # Méthode pour récupérer les médias associés au fournisseur
    def get_media(self, obj):
        media_items = obj.media_set.all()
        return MediaSerializer(media_items, many=True).data
