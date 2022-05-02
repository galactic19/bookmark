from django.contrib import admin
from .models import Bookmark

# Register your models here.
# 내가 만든 모델을 관리제 파이지에서 관리할 수 있도록 등록해줌.


admin.site.register(Bookmark)