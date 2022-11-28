from django.contrib.auth.models import User
from django.db import models
from product.utils import rename_imagefile_to_uuid

COMPUTER_PART = (
    ('1', 'CPU'),
    ('2', 'MAINBOARD'),
    ('3', 'RAM'),
    ('4', 'SSD'),
    ('5', 'GPU'),
    ('6', 'POWER')
)

#테이블생성
class Product(models.Model):
    uid = models.ForeignKey(User,on_delete=models.CASCADE) #관리자중 누가 등록햇니
    category = models.CharField(choices=COMPUTER_PART, max_length=128) # 카테고리
    name = models.TextField() #상품명 필드
    imgsrc = models.ImageField(null=True, upload_to=rename_imagefile_to_uuid, max_length=255, blank=True)  # 이미지 경로 저장하는 필드
    display_yn = models.BooleanField(default=False) #상품리스트에 출력여부
    query_yn = models.BooleanField(default=False) #계속 검색할지 여부
    query_data = models.TextField() #쿼리 데이타
    create_date = models.DateTimeField(auto_now_add=True) #작성일자
    like = models.ManyToManyField(User, related_name='likes' ,blank=True)
    def __str__(self):
        return "product"
    class Meta:
        db_table = 'qrqr_product'