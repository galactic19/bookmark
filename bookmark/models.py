from django.db import models
from django.urls import reverse

# Create your models here.
# 데이터 베이스를 SQL 없이 사용하기 위해 모델을 사용
# 데이터를 객체화 하여 다룰수 있다.
# 모델은 데이터베이스 테이블

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        return self.site_name

    # 필드의 종류가 결정 하는 것
    # 1. 데이터 베이스의 ㅋ컬럼 종류
    # 2. 제약 사항 (몇 글자까지 등등)
    # 3. Form 의 종류
    # 4. Form 에서 제약 사항.

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])
