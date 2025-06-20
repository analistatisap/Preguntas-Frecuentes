from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TipViewSet, ManualViewSet

router = DefaultRouter()
router.register(r'tips', TipViewSet)
router.register(r'manuales', ManualViewSet)

urlpatterns = [
    path('', include(router.urls)),
]