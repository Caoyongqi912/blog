from django.urls import path

from Pro_App import views

app_name = "pro_app"
urlpatterns = [
    path('appcase/<int:pid>', views.AppCaseView.as_view(), name='appcase'),
    path('appcasedetail/<int:aid>',views.AppCaseStepView.as_view(),name='appcasedetail'),



]