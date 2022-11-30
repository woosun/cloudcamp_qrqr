from django.shortcuts import redirect, render
from product.models import Product
#from product.froms import ProdcutForm  # 게시판 폼을 만들어둔걸 불러오기위한 거#
#from django.db.models import Q
from django.contrib.auth.decorators import login_required
#from django.contrib.auth import get_user_model  # 유저 목록 가져오기
#from django.contrib.auth.models import User

@login_required(login_url='/login') #게시글 작성 및 수정 삭제 모두 list 페이지에서 이루어 지므로 모두 list페이지로 보낸다.
def prog(request, type):
    print("타입없음에러")
    return render(request, 'index.html')

# 리스트함수 게시판명별로 정렬추가
def list(request,category):
    print(category)
    posts = Product.objects.filter(category=category).order_by('-id')
    print(posts)
    return render(request, 'product/index.html',
                  {'posts': posts, 'request': request})

def mains(request):
    return render(request, 'index.html')
