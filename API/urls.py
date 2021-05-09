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


#in this sinario we have genrate token by admin site and terminal by drf_crate_token
#terminal by drf_crate_token [python manage.py drf_create_token user1]
#obtain_auth_token using this import we route through terminal using httpie [http POST http://127.0.0.1:8000/gettoken/ username="user4" password="geekyshows"]]

