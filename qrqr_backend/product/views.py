from django.shortcuts import redirect, render
#from product.models import Product
#from product.froms import ProdcutForm  # 게시판 폼을 만들어둔걸 불러오기위한 거#
#from django.db.models import Q
from django.contrib.auth.decorators import login_required
#from django.contrib.auth import get_user_model  # 유저 목록 가져오기
#from django.contrib.auth.models import User

@login_required(login_url='login') #게시글 작성 및 수정 삭제 모두 list 페이지에서 이루어 지므로 모두 list페이지로 보낸다.
def prog(request, type):
    if type == 'edit' or type == 'del':  # 작성자와 삭제 또는 수정자가 다를경우 게시판으로 다시보내자
        return redirect('/product/')
    # 조건 타입이 뭔지 보자
    if type == 'new':  # 새 게시물 작성 /prog/new?bname=free /porg/read?id=3
        return redirect('/list/')
    elif type == 'edit':  # 수정작업
        return redirect('/list/')
    elif type == 'read':  # 게시글 읽어와서 prog.html에 뿌려주기
        return redirect('/list/')
    elif type == 'del':
        return redirect('/list/')
    else:
        print("타입없음에러")
    return render(request, 'index.html')


# 리스트함수 게시판명별로 정렬추가
def list(request):
    posts = Product.objects.all().order_by('-id')
    return render(request, 'index.html',
                  {'posts': posts, 'request': request, 'users': users})

def mains(request):
    return render(request, 'index.html')