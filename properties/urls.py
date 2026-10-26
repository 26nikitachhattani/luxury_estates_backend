from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, InquiryViewSet

router = DefaultRouter()
router.register("properties", PropertyViewSet, basename="property")
router.register("inquiries", InquiryViewSet, basename="inquiry")

urlpatterns = [
    path("", include(router.urls)),
]