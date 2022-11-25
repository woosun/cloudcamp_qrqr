from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import product.views
import user.views
import guduck.views

urlpatterns = [
    #어드민
    path('admin/', admin.site.urls),
        #회원관리
        #구독관리
        #상품관리

    #메인페이지


    #상품 #리스트
    path('product/', product.views.list),
        #상세
    path('product/view', product.views.view),



    #회원
        # 가입
    path('signup/', user.views.signup),
    path('login/', user.views.login),
    path('logout/', user.views.logout),



    #구독 관리 guduck
        # 나의 구독 내역 list
    path('guduck/', product.views.list),
        # 나의 구독 수정(삭제)
    path('guduck/prog/<str:type>', product.views.prog),




]
