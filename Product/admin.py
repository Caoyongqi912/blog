from django.contrib import admin

# Register your models here.
from Pro_Api.models import Apis
from Pro_App.models import AppCase
from .models import Product

class AppcaseAdmin(admin.TabularInline):
    list_display = ['app_case_name','app_case_result','create_time','id','product']
    model = AppCase
    extra = 1


class ApisAdmin(admin.TabularInline):
    list_display = ['api_name', 'api_url', 'api_par_val', 'api_method', 'api_result', 'api_status', 'create_time', 'id',
                    'product']
    model = Apis
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','product_desc','create_time','id']
    inlines = [ApisAdmin]





admin.site.register(Product)