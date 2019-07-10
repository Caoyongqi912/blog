from django.contrib import admin

# Register your models here.
from Pro_Set.models import Set


@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    list_display = ('set_name','set_value')
