from django.urls import path

from Pro_Set import views

app_name = "pro_set"
urlpatterns = [
    path('set/',views.SetView.as_view(),name='set'),

]