from django.contrib import admin

from .models import Employee
# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    search_fields = ('name', 'surname', 'job_title')
    list_filter = ('job_title', )
    filter_horizontal = ('chief', )

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

