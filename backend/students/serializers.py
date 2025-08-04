from rest_framework import serializers
from .models import Student  

class StudentSerializer(serializers.ModelSerializer):
    image_path = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = [
            'id',
            'roll_no',
            'name',
            'age',
            'dob',
            'email',
            'phone',
            'department',
            'attendance_percentage',  # <--- ADD
            'mark_percentage', 
            'image',
            'image_path',
            'is_active',
            'created_at',
            'updated_at'
        ]

    def get_image_path(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None