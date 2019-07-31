from django.contrib import admin
from django.urls import path #include: ~~~/@@@의 형태에서 ~~~를 없애고 싶을 때 import 해주어야함
import blog.views
import portfolio.views #views를 꼭 import해주기!!! + 새로운 앱을 시작했으면 settings에 꼭 추가!
from django.conf import settings
from django.conf.urls.static import static #이 두개는 외우기

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"), #blog라는 앱에 있는 views.py에서 'home'이라는 함수랑 연결하겠다! 이 path이름은 home! 
    path('blog/<int:blog_id>/', blog.views.detail, name="detail"), # <>:path converter, int: 숫자 # 두번째: 블로그앱 안에 있는 views라는 함수 안의 detail이라는 함수로 두 번째 인자(blog_id)를 전달 # 이름은 detail.  
    path('blog/new/', blog.views.new, name="new"),
    path('blog/create', blog.views.create, name="create"), #create로 가면, views.py에 있는 create함수를 실행해라! *꼭 html을 띄울 필요 X
    path('portfolio/', portfolio.views.portfolio, name="porfol"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #이것또한 외우기...
