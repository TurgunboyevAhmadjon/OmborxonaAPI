from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from userapp.views import *
from asosiy.views import *
from statsapp.views import *

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView



schema_view = get_schema_view(
   openapi.Info(
      title="OmborxonaAPI",
      default_version='v1',
      description="Test description",
      # terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="Ombor@gmail.com"),
      # license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ombor/', OmborAPIView.as_view()),
    path('mahsulot/', MahsulotListCreate.as_view()),
    path('mahsulot/<int:pk>/', MahsulotUpdate.as_view()),
    path('stats/', StatsListCreate.as_view()),
    path('stats/<int:pk>/', StatsUpdate.as_view()),
    path('client/', ClientListCreate.as_view()),
    path('client/<int:pk>/', ClientUpdate.as_view()),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-doc'),
    path('token-ber/', TokenObtainPairView.as_view(), name='token-ber'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
