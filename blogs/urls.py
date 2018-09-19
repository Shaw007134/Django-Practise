"""定义blogs的URL模式"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    
    # 显示所有博客
    url(r'^blogs/$', views.blogs, name = 'blogs'), 
    
    # 显示博客详细
    url(r'^blogs/(?P<blog_id>\d+)/$', views.blog, name = 'blog'),
    
    # 发布新博客
    url(r'^new_blog/$', views.new_blog, name = 'new_blog' ),
    
    # 用于编辑现有博客内容
    url(r'^edit_blog/(?P<blog_id>\d+)/$',views.edit_blog, 
      name = 'edit_blog'),
]
