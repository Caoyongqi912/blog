from django.urls import path
from .views import Register, Login, RegisterCheck, Quit, Modify, ModifyCheck, ChangeInfo, github_login, github_check, \
    bind_email

app_name = "User"
urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('register_check/', RegisterCheck.as_view(), name='register_check'),
    path('quit/', Quit.as_view(), name='quit'),
    path('modify/', Modify.as_view(), name='modify'),
    path('modify_check/', ModifyCheck.as_view(), name='modify_check'),
    path('change_info',ChangeInfo.as_view(),name='change_info'),
    path('github_login/', github_login, name='github_login'),
    path('github_check/', github_check, name='github_check'),
    path('bind_email/', bind_email, name='bind_email'),

]
