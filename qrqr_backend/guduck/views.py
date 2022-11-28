from django.shortcuts import redirect, render
from product.models import Product
from guduck.models import guduck
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='login') #게시글 작성 및 수정 삭제 모두 list 페이지에서 이루어 지므로 모두 list페이지로 보낸다.
def prog(request, pid):
    #구독여부확인하여
    #구독중
    uid = User.objects.get(Q(username=request.user))
    pid_s = Product.objects.get(Q(id=pid))
    post = guduck.objects.filter(uid_id=uid.id,pid_id=pid).first()
    if post != None : #구독중 > 구독해지
        if post.read_yn == 1 : #구독중 > 구독해지
            post.read_yn = 0
        else :
            post.read_yn = 1
        post.save()
    else :
        post = guduck()
        post.uid_id = uid.id
        post.pid_id = pid
        post.mailing_site = "y"
        post.read_yn = 1
        post.save()

    #구독해지