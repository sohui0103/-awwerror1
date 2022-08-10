from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from awwwapp.models import Blog
from awwwapp.forms import BlogUpdate

# Create your views here.

def home(request):
    blogs = Blog.objects.order_by('-id')
    blog_list = Blog.objects.all().order_by('-id')
    paginator = Paginator(blog_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request,'home.html', {'blogs':blogs,'posts':posts}) 

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render (request, 'detail.html',{'blog': blog_detail})

def create(request):
    return render(request, 'create.html')

def postcreate(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.images = request.FILES['images']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/awwwapp/detail/' + str(blog.id))

def update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method =='POST':
        form = BlogUpdate(request.POST)
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.body = form.cleaned_data['body']
            blog.pub_date=timezone.now()
            blog.save()
            return redirect('/awwwapp/detail/' + str(blog.id))
    else:
        form = BlogUpdate(instance = blog) 
 
        return render(request,'update.html', {'form':form})

def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('/')

def new(request):
    return render(request, 'new.html')

def search(request):
    blogs = Blog.objects.all().order_by('-id')

    q = request.POST.get('q', "")

    if q:
        blogs = blogs.filter(title__icontains=q)
        return render(request, 'search.html',{'blogs' : blogs, 'q' : q})
    
    else:
        return render(request, 'search.html')


def musictalk(request):
    return render(request, 'musictalk.html')

def userplaylist(request):
    return render(request, 'userplaylist.html')

def musicplaylist(request):
    return render(request, 'musicplaylist.html')

def mypage(request):
    return render(request, 'mypage.html')

def makeplaylist(request):
    return render(request, 'makeplaylist.html')
