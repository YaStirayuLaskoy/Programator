from django.urls import path, include
from rest_framework import routers
from .views import WorkerViewSet, DayViewSet, ShiftViewSet

app_name = 'pragramator_api'

router = routers.DefaultRouter()
router.register(r'workers', WorkerViewSet)
router.register(r'days', DayViewSet)
router.register(r'shifts', ShiftViewSet)

urlpatterns = [
    path('', include(router.urls)),
]