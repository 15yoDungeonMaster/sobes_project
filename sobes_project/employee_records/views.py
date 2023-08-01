
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


from employee_records.models import Person
from employee_records.serializers import PersonSerializer


class EmployeeListAPIView(ListCreateAPIView):
    """List of employees"""
    queryset = Person.objects.prefetch_related('subordination').all()
    serializer_class = PersonSerializer
    permission_classes = (IsAuthenticated, )


class EmployeeRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    """Employee detail view"""
    queryset = Person.objects.prefetch_related('subordination').all()
    serializer_class = PersonSerializer
    permission_classes = (IsAuthenticated, )

