from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('pragramator_api.urls', namespace='pragramator_api'))
]
