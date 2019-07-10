from django.contrib import admin

# Register your models here.
from Pro_Api.models import ApiTestStep, ApiTest, Apis


class ApiTestStepAdmin(admin.TabularInline):
    list_display = ['api_name','api_url','api_param_val','api_method','api_result','api_status','create_time',
                    'id','api_test']
    model = ApiTestStep
    extra = 1


class ApisAdmin(admin.TabularInline):
    list_display = ['api_name', 'api_url', 'api_par_val', 'api_method', 'api_result', 'api_status', 'create_time', 'id',
                    'product']


class ApiTestAdmin(admin.ModelAdmin):
    list_display = ['api_test_name','api_tester','api_test_res','create_time','id',]
    inlines = [ApiTestStepAdmin]



admin.site.register(Apis)
admin.site.register(ApiTest,ApiTestAdmin)