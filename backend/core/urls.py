# core/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return HttpResponse("🎓 Welcome to the Student Management System!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # homepage
    path('api/', include('students.urls')),  # <-- This includes students app URLs under /api/
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
