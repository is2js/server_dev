from django.conf.urls import url
from .views import RegistUser, Applogin

urlpatterns = [
    url("regist_user", RegistUser.as_view(), name="regist_user"), # ~/login(path)/register
    url("app_login", Applogin.as_view(), name="app_login") # ~/login(path)/app_login
]
