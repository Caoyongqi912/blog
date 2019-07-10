from django.contrib import admin

# Register your models here.
from Pro_Bug.models import Bug


@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display = ('bug_name','bug_detail','bug_status','bug_level','bug_creater','bug_assign','create_time')
