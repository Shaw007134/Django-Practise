from .models import BlogPost
from django.http import HttpResponseRedirect, Http404

def check_blog_owner(request, blogpost):
    """检查当前topic的owner是否是是当前登录的用户"""
    if blogpost.owner != request.user:
        raise Http404
