from rest_framework import serializers

from employee_records.models import Person, Subordination


class PersonSerializer(serializers.ModelSerializer):
    employees = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = ('id', 'name', 'surname', 'job_title', 'chiefs', 'employees')

    def get_employees(self, obj):
        data = [
            {
                'id': person.id,
                'name': person.name,
                'surname': person.surname,
                'job_title': person.job_title,
            }

            for person in obj.subordination.employee.all()
        ]
        return data

    def create(self, validated_data):
        chiefs = validated_data.pop('chiefs')
        instance = Person.objects.create(**validated_data)
        Subordination.objects.create(person=instance)
        instance.chiefs.set(chiefs)
        return instance

