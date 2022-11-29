from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from guduck.models import guduck
from product.models import Product

# 리스트가 불러옴
@login_required(login_url='login') #나의 구독리스트 이므로 로그인여부 체크
def list(request):
    lists = guduck.objects.filter(uid_id = request.user.id,read_yn=1).order_by('-id')
    return render(request, 'guduck/index.html', {'lists': lists, 'request': request})

@login_required(login_url='login') #나의 구독리스트 이므로 로그인여부 체크
def unlike(request,pid):
    # 어떤 게시물에, 어떤 사람이 like를 했는 지
    post = Product.objects.get(id=pid)  # 게시물 번호 몇번인지 정보 가져옴
    user = request.user
    if post.like.filter(id=request.user.id).exists():  # 유저면 알아서 유저의 id로 검색해줌
        print("구독 삭제")
        guduck_fc(request.user.id, pid, "remove")
        post.like.remove(user)
    return redirect('/myguduck/')

def guduck_fc(uid, pid, type):
    # 구독여부확인하여
    # 구독중
    if type == "add":
        post = guduck.objects.filter(uid_id=uid, pid_id=pid).first()
        if post != None:  # 구독중 > 구독해지
            post.read_yn = 1
            post.save()
        else:
            post = guduck()
            post.uid_id = uid
            post.pid_id = pid
            post.mailing_site = "y"
            post.read_yn = 1
            post.save()
    else:
        post = guduck.objects.filter(uid_id=uid, pid_id=pid).first()
        if post != None:  # 구독중 > 구독해지
            post.read_yn = 0
            post.save()
