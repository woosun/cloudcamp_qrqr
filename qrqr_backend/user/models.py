from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users():
    # user = models.CharField(max_length=64,verbose_name="사용자이름")
    # password = models.CharField(max_length=64, verbose_name="비밀번호")
    # useremail = models.EmailField(max_length=128, verbose_name="이메일")

    def __str__(self):
        return self.user

    class Meta:
        model = User
        field = [
            'username',
            'password',
            'email',
        ]

        # db_table = "users"
        # verbose_name ="사용자"
        # verbose_name_plural = "사용자"



