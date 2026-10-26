from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from .models import Property, Inquiry
from .serializers import PropertySerializer, InquirySerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all().order_by("-created_at")
    serializer_class = PropertySerializer
    filterset_fields = ["location", "bedrooms"]
    search_fields = ["name", "location", "description"]
    ordering_fields = ["price", "size_sqft", "bedrooms", "created_at"]
    ordering = ["-created_at"]

    def get_permissions(self):
        if self.action in ["list", "retrieve", "create_inquiry"]:
            return [AllowAny()]
        return [IsAdminUser()]

    @action(
        detail=True,
        methods=["post"],
        url_path="inquiries",
        permission_classes=[AllowAny],
    )
    def create_inquiry(self, request, pk=None):
        property_obj = self.get_object()

        serializer = InquirySerializer(
            data={
                **request.data,
                "property": property_obj.pk,
            }
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )


class InquiryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Inquiry.objects.select_related("property").order_by(
        "-created_at"
    )
    serializer_class = InquirySerializer
    permission_classes = [IsAdminUser]
