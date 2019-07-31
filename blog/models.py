from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200) # 타이틀 길이 200 제한 ( 짧은 문자 CharField )
    pub_date = models.DateTimeField('date published') # 날짜와 시간을 나타내는 데이터
    body = models.TextField() # 긴 문자 TextField
    kinds = models.CharField(max_length = 20)
    kakaotalkID = models.CharField(max_length = 20)
    price = models.CharField(max_length = 100)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]