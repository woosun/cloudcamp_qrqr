from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import user.views
import product.views
#import guduck.views

urlpatterns = [
    #어드민
    path('admin/', admin.site.urls),
        #회원관리
        #구독관리
        #상품관리

    #메인페이지
    path('', user.views.mainFunc),

    #상품 #리스트
    path('list/<str:category>', product.views.list),
        #상세
    path('product/<str:type>', product.views.prog),



    #회원
        # 가입
    path('signup/', user.views.signup, name="signup"),
    path('login/', user.views.login, name="login"),
    path('logout/', user.views.logout),



    #구독 관리 guduck
        # 나의 구독 내역 list
 #   path('guduck/', product.views.list),
        # 나의 구독 수정(삭제)
 #   path('guduck/prog/<str:type>', product.views.prog),




]
