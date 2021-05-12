from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
from .CustomUserRateThrottle import CustomUserThrottle

#Url 1
class StudentViewset(viewsets.ModelViewSet):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticatedOrReadOnly]   
        throttle_classes = [ScopedRateThrottle] 
        throttle_scope = 'admin'

#Url 2
class StudentReadonly(viewsets.ModelViewSet):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]   
        throttle_classes = [ScopedRateThrottle]
        throttle_scope = 'cusomer'
#Url 3
class StudentUpdate(viewsets.ModelViewSet):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer
        authentication_classes = [JWTAuthentication]
        permission_classes = [AllowAny]   
        throttle_classes = [ScopedRateThrottle]
        throttle_scope = 'bank'

        