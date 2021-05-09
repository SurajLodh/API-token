from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

#for ModelViewsets 
from tokenapp import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token #for httpie get_token
#Creating Default Router
router = DefaultRouter()

#Register Router
router.register('student', views.StudentViewset, basename="student")   #For_Complete_CRUD
# router.register('readonly', views.StudentReadonly, basename="readonly")  #For_ReadOnly_Read_&_Retrive

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace="Authentication")),
    path('gettoken/', obtain_auth_token), #for httpie get_token
]
