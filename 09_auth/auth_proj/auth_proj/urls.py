from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('task_api.urls')),
    path('api/', include('user_api.urls')),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
