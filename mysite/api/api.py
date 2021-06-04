from .models import TestModel
from rest_framework import viewsets, permissions
from .serializers import TestSerializer

# Test Viewset
class TestViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = TestSerializer
