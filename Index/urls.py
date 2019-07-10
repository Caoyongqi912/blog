from django.urls import path

from Index import views

app_name = "Index"
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('about/',views.About.as_view(),name='about'),
    path('apply/',views.Apply.as_view(),name='apply')
]
