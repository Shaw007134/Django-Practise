from django.shortcuts import render
from .models import BlogPost
from .forms import NewBlogForm, EditBlogForm
from .check_owner import check_blog_owner
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    """博客系统的主页"""
    return render(request, 'blogs/index.html')

def blogs(request):
    """显示所有博客"""
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    """显示单个博客的内容"""
    blog = BlogPost.objects.get(id=blog_id)
    context = {'blog': blog, 'text': blog.text}
    return render(request, 'blogs/blog.html', context)

@login_required
def new_blog(request):
    """添加新blog"""
    if request.method != 'POST':
        # 未提交数据，创建一个新表单
        form = NewBlogForm()
    else:
        # 对提交的数据进行处理
        form = NewBlogForm(request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            form.save()
            return HttpResponseRedirect(reverse('blogs:blogs'))
    context = {'form': form}
    return render(request, 'blogs/new_blog.html',context)

@login_required
def edit_blog(request,blog_id):
    """在特定的blog中进行编辑"""
    blog = BlogPost.objects.get(id=blog_id)
    title = blog.title
    check_blog_owner(request, blog)
    if request.method != 'POST':
        # 未提交数据，创建一个空表单
        form = EditBlogForm(instance=blog)
    else:
        # 对提交的数据进行处理
        form = EditBlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:blog', 
                   args = [blog.id]))
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/edit_blog.html', context)
    
