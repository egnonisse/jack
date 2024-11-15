from django.contrib import admin

# Register your models here.
from .models import Provider, Review, ServiceCategory, Media

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'email', 'average_rating')
    search_fields = ('name', 'address', 'email')
    list_filter = ('categories',)

@admin.register(Review) 
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('provider', 'user_name', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('user_name', 'comment')

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('provider', 'media_type')
    list_filter = ('media_type',)
