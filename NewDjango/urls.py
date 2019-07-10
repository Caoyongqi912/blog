from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Index.urls', namespace='Index')),
    path('spider/', include('spider.urls', namespace='spider')),
    path('user/', include('User.urls', namespace='User')),
    path('articles/',include('Articles.urls',namespace='articles')),


    path('product/',include('Product.urls',namespace='product')),
    path('pro_api/',include('Pro_Api.urls',namespace='pro_api')),
    path('pro_bug/',include('Pro_Bug.urls',namespace='pro_bug')),
    path('pro_set/',include('Pro_Set.urls',namespace='pro_set')),
    path('pro_app/',include('Pro_App.urls',namespace='pro_app')),
    path('pro_web/',include('Pro_Web.urls',namespace='pro_web')),
    path('pro_rep/',include('Pro_report.urls',namespace='pro_rep'))




]
