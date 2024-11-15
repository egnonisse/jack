# C:\laragon\www\2024\Nov\12112024\providers\urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProviderViewSet, ReviewViewSet, MediaViewSet, ServiceCategoryViewSet, RegisterView, LoginView, LogoutView, ProfileView, UserViewSet

router = DefaultRouter()
router.register(r'providers', ProviderViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'media', MediaViewSet)
router.register(r'category', ServiceCategoryViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Pas de préfixe `api/` ici, car il est déjà ajouté dans petitemain/urls.py
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('user/<int:pk>/', ProfileView.as_view(), name='profile'),
]
