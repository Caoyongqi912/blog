from django.urls import path
from .views import *
from .testcase import *
app_name = 'pro_web'
urlpatterns=[
    path('web_case/<int:pid>',WebCaseView.as_view(),name='web_case'),
    path('web_case_step/<int:web_id>',WebCaseStepView.as_view(),name='web_case_step'),
    path('web_test/<int:aid>',getid,name='web_test')

]
