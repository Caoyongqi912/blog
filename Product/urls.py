from django.urls import path

from Product import views
app_name = "product"
urlpatterns = [
    path('product/',views.ProductView.as_view(),name='product'),
    path('product_detail/<int:pid>',views.Detail.as_view(),name='product_detail'),
    path('del_product/',views.Del_pro.as_view(),name='del_product'),


]
