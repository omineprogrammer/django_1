from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'identification',
        'email',
        'phone',
        'address',
    ]
    fields = [
        (
            'first_name', 'middle_name',
            'last_name', 'second_last_name',
        ),
        ('id_type', 'identification',),
        'email',
        'phone',
        'address',
    ]
