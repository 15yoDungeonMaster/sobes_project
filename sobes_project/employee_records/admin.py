from django.contrib import admin

from .models import Person, Subordination


# Register your models here.


class SubordinateInline(admin.TabularInline):
    model = Subordination.employee.through
    extra = 1


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    model = Person
    search_fields = ('name', 'surname',)
        # ('job_title')
    # list_filter = ('job_title',)
    inlines = (SubordinateInline,)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

@admin.register(Subordination)
class SubordinateAdmin(admin.ModelAdmin):
    model = Subordination
