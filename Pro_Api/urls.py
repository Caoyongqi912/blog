from django.urls import path

from Pro_Api import views

app_name = "pro_api"
urlpatterns = [
    path('product_api/<int:pid>', views.Pro_Detail.as_view(), name='product_api'),
    path('api_method/<int:aid>', views.Method.as_view(), name='api_method'),

]