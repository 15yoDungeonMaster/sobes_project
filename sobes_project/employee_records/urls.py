from django.urls import path

from .views import EmployeeListAPIView, EmployeeRetrieveAPIView





urlpatterns = [
    path('list/', EmployeeListAPIView.as_view(), name='employee-list'),
    path('employee/<int:pk>/', EmployeeRetrieveAPIView.as_view(), name='employee-retrieve'),

]