from django.db import models

# Create your models here.

class Blog(models.Model):#class명을 지을 때에는 대문자!
    title = models.CharField(max_length=200) #title 속성은 최대 lenth가 200인 문자열로 형성할거야!
    pub_date = models.DateTimeField('date published') # pub_date 속성은 날짜와 시간으로 형성할거야!
    body = models.TextField()# 문자열 제한 X
    # model을 만든다--> makemigrations&migrate 하기!

    def __str__(self): #admin페이지의 블로그 글 이름을 자기 자신의 객체를 인자로 받을 때(제목 설정)
        return self.title #자기 자신의 타이틀을 내보내라!

    def summary(self):    #summary는 자기 자신 객체를 인자로 받음
        return self.body[:100]  #자기 자신 객체 안에 있는 body라고 하는 본문 내용을 return + 100글자 상한선->home.html에 있는 본문의 'body'를 'summary'라고 바꾸어 주어야 함.