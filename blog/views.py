# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from drink.models import BlogDrink
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def home(request):
    blogs = Blog.objects # 쿼리셋( 블로그 객체 목록 = 메소드 ) 전달 
    return render(request, 'home.html', {'blogs' : blogs})

    # 쿼리셋 표현
    # 모델.쿼리셋(object)
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog' : blog_detail})

def new(request):
    return render(request, 'new.html')
    
@csrf_exempt
def create(request): # 입력받은내용을 DB에 넣어주는 함수
    blog = Blog()
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.now()
    blog.kinds = request.POST['kinds']
    blog.kakaotalkID = request.POST['kakaoTalkID']
    blog.price = request.POST['price']
    blog.save()
    return render(request, 'finish.html')