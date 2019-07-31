from django.shortcuts import render, get_object_or_404, redirect #몇 번 객체를 받아 오는지 설정하기 위해
from django.utils import timezone
from .models import Blog # 같은 파일에 있는 models.py로 부터 Blog를 import해주었다!
# Create your views here.

def home(request):
    blogs = Blog.objects # admin페이지의 blog안의 데이터들--> 모델로부터 전달받은 객체목록: 'queryset'--> 처리: '메소드'
    return render(request, 'home.html', {'blogs': blogs}) #blogs라는 변수를 templates에서 쓸 때 blog라는 이름으로 가져오겠다!
 
def detail(request, blog_id): 
    details = get_object_or_404(Blog, pk=blog_id) # 첫번째 인자: 어떤 클래스로 부터 object를 get 할 건지? # 두 번째 인자: 검색 조건(pk값 설정) 
    return render(request, 'detail.html', {'details': details})

def new(request):   # request가 들어오면 new.html을 띄우는 함수+new.html에서 입력한 내용을 DB에 등록하는 함수
    return render(request, 'new.html') #그냥 request가 들어오면 new.html을 띄워라!

def create(request): #new에서 제출버튼을 누르면 create가 실행 될 것임!, 입력받은 내용을 DB에 넣어주는 함수!!!
    blog = Blog()  #blog라는 이름으로 객체 생성
    blog.title = request.GET['title'] #new에 있는 title에서 가져온 것들을 blog라는 객체의 title안에 담아준다
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now() #블로그 작성 시점을 넣어줌
    blog.save() #쿼리셋 메소드 중 하나. 위의 데이터를 DB에 저장!
    return redirect('/blog/'+str(blog.id)) #redirect: 위의 것을 다 처리한 다음, 괄호안의 url로 넘기세요! # blod.id를 url로 형변화: str
#redirect와 render의 차이?: 인자에 따라서 선택!(이분법X) 1)redirect는 괄호에 외부 url추가 가능 2)render는 세번째 인자로 key값을 받음->파이썬 안에서 만든 여러가지를 다 담아서 html상에서 처리하고 싶을 때
