from django.conf.urls.static import static
from django.urls import path

from Articles.views import Detail, Add_Comment
from NewDjango import settings

app_name = "articles"
urlpatterns = [
    path('detail/<int:aid>',Detail.as_view(),name='detail'),
    path('add_comment/<int:aid>',Add_Comment.as_view(),name='add_comment')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)