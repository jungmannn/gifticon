from django.db import models

# Create your models here.
class BlogDrink(models.Model):
    title = models.CharField(max_length = 200) # 타이틀 길이 200 제한 ( 짧은 문자 CharField )
    kinds = models.CharField(max_length = 20) # 파는 물건의 종류(type)
    price = models.CharField(max_length = 100) # 가격
    image = models.ImageField(upload_to="image/") # 이미지
    pub_date = models.DateTimeField(auto_now_add=True) # 날짜와 시간을 나타내는 데이터
    body = models.TextField() # 긴 문자 TextField
    kakaoTalkID = models.CharField(max_length = 20) # 카카오톩 아이디
    expirationDate = models.CharField(max_length = 20) # 유효기간

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]