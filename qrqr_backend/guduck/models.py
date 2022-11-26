from django.contrib.auth.models import User
from django.db import models
from product.models import Product
#테이블생성
class guduck(models.Model):
    uid = models.ForeignKey(User,on_delete=models.CASCADE) #관리자중 누가 등록햇니
    pid = models.ForeignKey(Product, related_name="Product_name", on_delete=models.CASCADE, db_column="Product_name")
    read_yn = models.BooleanField(default=False) #구독여부
    mailing_site = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True) #작성일자
    def __str__(self):
        return "guduck"
    class Meta:
        db_table = 'qrqr_guduck'