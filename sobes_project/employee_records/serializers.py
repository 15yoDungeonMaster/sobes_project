
from rest_framework.serializers import ModelSerializer, Serializer

from employee_records.models import Employee


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'surname', 'job_title', 'chief', 'employees',)

    def to_representation(self, instance):
        data = super(EmployeeSerializer, self).to_representation(instance)
        chief_data = data.pop('chief')
        data['chiefs'] = chief_data
        return data
