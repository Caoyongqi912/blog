from django.contrib import admin

# Register your models here.
from .models import User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    date_hierarchy = 'add_time'
    exclude = ('views',)

    list_display = ('id', 'username', 'add_time')

    list_filter = ('add_time', 'username')
    list_per_page = 10  # 每页数量
