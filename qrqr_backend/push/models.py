from django.contrib.auth.models import User
from django.db import models
from product.models import product
from guduck.models import guduck
# Create your models here.
class push(models.Model):
    uid = models.ForeignKey(User,on_delete=models.CASCADE) #누구
    pid = models.ForeignKey(product,on_delete=models.CASCADE) #상품
    gid = models.ForeignKey(guduck,on_delete=models.CASCADE) #구독
    try_yn = models.BooleanField(default=False) #발송성공여부
    reg_date = models.DateTimeField(auto_now_add=True) #발송일자
    def __str__(self):
        return "push"