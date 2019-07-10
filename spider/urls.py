from django.urls import path

from spider import views, youdao, cat

app_name = 'spider'
urlpatterns = [
    path('to_youdao_spider/', youdao.You.as_view(), name='to_youdao_spider'),
    path('youdao_spider/', youdao.YouDao.as_view(), name='youdao_spider'),
    path('quanji_spider/', views.QuanJi_movie.as_view(), name='quanji_spider'),
    path('cat/', cat.Cat.as_view(), name='cat')
]
