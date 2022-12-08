from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import user.views
import product.views
import guduck.views
app_name = 'guduck'
urlpatterns = [
    #어드민
    path('admin/', admin.site.urls),
    #회원관리
    path('myguduck/',guduck.views.list),
    path('unlike/<int:pid>',guduck.views.unlike),
    #구독관리
    path('like/<int:pid>',product.views.like),
    #메인페이지
    path('', user.views.mainFunc),
    #상품 #리스트
    path('list/<str:category>', product.views.list, name="list"),
    #상세
    path('product/<str:type>', product.views.prog),
    #회원
    path('signup/', user.views.signup, name="signup"),
    path('login/', user.views.login, name="login"),
    path('logout/', user.views.logout, name="logout"),
    path('mypage/', user.views.mypage, name="mypage"),
]
