from django.contrib import admin

# Register your models here.
from Pro_App.models import AppCase, AppCaseStep


# @admin.register(AppCase)
# # class AppCaseAdmin(admin.ModelAdmin):
#     list_display =  ('app_case_name','app_case_result','app_tester','create_time')

class AppCaseStepAdmin(admin.TabularInline):
    list_display = ['app_test_step','app_sbj_name','app_find_method','app_element','app_res','create_time','id',
                    'appcase']
    model = AppCaseStep
    extra = 1

class AppCaseAdmin(admin.ModelAdmin):
    list_display = ['app_case_name','app_case_result','create_time','id']
    inlines = [AppCaseStepAdmin]

admin.site.register(AppCase,AppCaseAdmin)