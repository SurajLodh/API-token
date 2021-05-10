from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
# from rest_framework.authentication import TokenAuthentication
from .CustomAuthentication import MyAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

#For_Complete_CRUD
class StudentViewset(viewsets.ModelViewSet):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer
        authentication_classes = [MyAuthentication]  #http://127.0.0.1:8000/student/1/?username=user1
        permission_classes = [IsAuthenticatedOrReadOnly]  