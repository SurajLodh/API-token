from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

#for ModelViewsets 
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

#Creating Default Router
router = DefaultRouter()

#Register Router
router.register('studentall', views.StudentViewset, basename="studentall")   #url1
router.register('studentread', views.StudentReadonly, basename="studentread")   #url2
router.register('studentupdate', views.StudentUpdate, basename="studentupdate")   #url3

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace="Authentication")),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
]

