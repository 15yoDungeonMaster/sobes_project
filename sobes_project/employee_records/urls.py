from django.urls import path, include

from .views import EmployeeViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employee_records', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls))

]