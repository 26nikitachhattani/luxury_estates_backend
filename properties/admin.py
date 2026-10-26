from django.contrib import admin
from .models import Property, Inquiry


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "price",
        "size_sqft",
        "bedrooms",
    )
    search_fields = ("name", "location")
    list_filter = ("location", "bedrooms")


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "property",
        "created_at",
    )
    search_fields = ("name", "email", "property__name")
    list_filter = ("created_at",)
    readonly_fields = ("created_at",)