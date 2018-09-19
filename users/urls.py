"""为应用程序users定义URL模式"""

from django.conf.urls import url
from django.contrib.auth.views import login,logout

from . import views

urlpatterns = [
    # 登录页面
    url('^login/$', login, {'template_name': 'users/login.html'},
        name = 'login'),
    # 注销
    url('^logout/$', logout, {'template_name': 'users/logout.html'}, 
        name = 'logout'),
    # 登录页面
    url('^register/$', views.register, name='register'),
]
