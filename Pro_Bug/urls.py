from django.urls import path

from Pro_Bug import views

app_name = "pro_bug"
urlpatterns = [
    path('bug/<int:pid>',views.BugView.as_view(),name='bug'),

]