from django.contrib import admin
from .models import Blog # 같은 폴더위치에 있는 models라는 파일에 Blog 라는 클래스를 가져오겠음

# Register your models here.
admin.site.register(Blog) #admin이라는 site에 Blog라는 클래스를 등록해라