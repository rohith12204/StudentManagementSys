from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Student
from .serializers import StudentSerializer

# Optional test view
def index(request):
    return HttpResponse("Hello from the students app!")

# Main API ViewSet
class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    parser_classes = (MultiPartParser, FormParser)  # Needed for image uploads

    def get_queryset(self):
        # Only return students who are marked as active
        return Student.objects.filter(is_active=True)

    def get_serializer_context(self):
        # Ensures full image URL is returned
        return {'request': self.request}

    def perform_destroy(self, instance):
        # Soft delete: mark inactive instead of deleting
        instance.is_active = False
        instance.save()
