from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

#For_Complete_CRUD
class StudentViewset(viewsets.ModelViewSet):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticatedOrReadOnly]   
        throttle_classes = [AnonRateThrottle, UserRateThrottle]