from django.db import models


class Student(models.Model):
    roll_no = models.CharField(max_length=10, unique=True)  # ✅ Add this line
    name = models.CharField(max_length=100, default='Unknown')
    age = models.IntegerField(default=18)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(default='example@example.com')
    phone = models.CharField(max_length=15, default='0000000000')
    department = models.CharField(max_length=100, default='Unknown')
    image = models.ImageField(upload_to='student_images/', null=True, blank=True)
    attendance_percentage = models.FloatField(default=0.0)
    mark_percentage = models.FloatField(default=0.0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



