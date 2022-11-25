from django.contrib.auth.models import User
from django.db import models
from product.models import product
#테이블생성
class guduck(models.Model):
    uid = models.ForeignKey(User,on_delete=models.CASCADE) #관리자중 누가 등록햇니
    pid = models.ForeignKey(product,on_delete=models.CASCADE) #관리자중 누가 등록햇니
    read_yn = models.BooleanField(default=False) #구독여부
    mailing_site = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True) #작성일자
    def __str__(self):
        return "guduck"