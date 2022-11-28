from django.shortcuts import redirect, render
from product.models import Product
#from product.froms import ProdcutForm  # 게시판 폼을 만들어둔걸 불러오기위한 거#
#from django.db.models import Q
from django.contrib.auth.decorators import login_required
#from django.contrib.auth import get_user_model  # 유저 목록 가져오기
from django.contrib.auth.models import User
from guduck.models import guduck
from django.db.models import Q
from django.http import JsonResponse

@login_required(login_url='login') #게시글 작성 및 수정 삭제 모두 list 페이지에서 이루어 지므로 모두 list페이지로 보낸다.
def prog(request, type):
    print("타입없음에러")
    return render(request, 'index.html')


# 리스트함수 게시판명별로 정렬추가
def list(request,category):
    posts = Product.objects.filter(category=category).order_by('-id')


    return render(request, 'product/index.html',
                  {'posts': posts, 'request': request})

@login_required(login_url='login')
def like(request,pid):
    # 어떤 게시물에, 어떤 사람이 like를 했는 지
    post = Product.objects.get(id=pid) # 게시물 번호 몇번인지 정보 가져옴
    user = request.user
    if post.like.filter(id=request.user.id).exists(): # 유저면 알아서 유저의 id로 검색해줌
        #구독 삭제
        guduck_fc(request.user.id,pid,"remove")
        post.like.remove(user)
        return JsonResponse({'message': 'deleted', 'like_cnt' : post.like.count() })
    else:
        guduck_fc(request.user.id, pid, "add")
        post.like.add(user) # post의 like에 현재유저의 정보를 넘김
        return JsonResponse({'message': 'added', 'like_cnt' : post.like.count()})


def guduck_fc(uid,pid,type):
    #구독여부확인하여
    #구독중
    if type == "add":
        post = guduck.objects.filter(uid_id=uid, pid_id=pid).first()
        if post != None : #구독중 > 구독해지
            post.read_yn = 1
            post.save()
        else :
            post = guduck()
            post.uid_id = uid
            post.pid_id = pid
            post.mailing_site = "y"
            post.read_yn = 1
            post.save()
    else :
        post = guduck.objects.filter(uid_id=uid, pid_id=pid).first()
        if post != None : #구독중 > 구독해지
            post.read_yn = 0
            post.save()


def mains(request):
    return render(request, 'index.html')