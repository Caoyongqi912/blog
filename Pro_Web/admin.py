from django.contrib import admin

# Register your models here.
from Pro_Web.models import WebCase, WebCaseStep

#
# @admin.register(WebCase)
# class WebCaseAdmin(admin.ModelAdmin):
#     list_display = ('web_case_name','web_test_res','web_tester','create_time')
#
# @admin.register(WebCaseStep)
# class WebCaseStepAdmin(admin.ModelAdmin):
#
#     list_display = ('web_case_name','web_test_step','web_sbj_name','web_find_method','web_element',
#                     'web_opt_method','web_test_data','web_assert_data','web_test_res','create_time')

class WebcasestepAdmin(admin.TabularInline):

    list_display = ['web_case_name','web_test_step','web_sbj_name','web_find_method','web_element',
                    'web_opt_method','web_test_data','web_assert_data','web_test_res','create_time','id','web_case']
    model = WebCaseStep
    extra = 1

class WebcaseAdmin(admin.ModelAdmin):
    list_display = ['web_case_name','web_test_res','create_time','id']
    inlines = [WebcasestepAdmin]

admin.site.register(WebCase,WebcaseAdmin)