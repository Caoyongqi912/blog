from django.urls import path

from Pro_report import views


app_name='pro_rep'
urlpatterns=[
    path('report/',views.Report.as_view(),name='report'),
    path('api_report/<int:pid>', views.ApiReprot.as_view(), name='api_report')


]