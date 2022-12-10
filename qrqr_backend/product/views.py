from django.shortcuts import redirect, render
from product.models import Product
from django.contrib.auth.decorators import login_required
from guduck.models import guduck
from django.core.paginator import Paginator
import influxdb_client
import os
import json
import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
secret_file = os.path.join(BASE_DIR, 'secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())


bucket = secrets['bucket']
org = secrets['org']
token = secrets['token']
url=secrets['url']
@login_required(login_url='/login') #게시글 작성 및 수정 삭제 모두 list 페이지에서 이루어 지므로 모두 list페이지로 보낸다.
def prog(request, type):
    print("타입없음에러")
    return render(request, 'index.html')

# 리스트함수 게시판명별로 정렬추가
def list(request,category):
    board_list = Product.objects.filter(category=category, display_yn=1).order_by('-id')  # models.py Board 클래스의 모든 객체를 board_list에 담음
    # board_list 페이징 처리
    page = request.GET.get('page', '1')  # GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(board_list, '3')  # Paginator(분할될 객체, 페이지 당 담길 객체수)
    if int(page) > int(paginator.num_pages) :
        page = paginator.num_pages # 호출한 페이지가 총페이지보다 크면 마지막페이지 이동
    posts = paginator.page(page)  # 페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
    posts.in_page = page
    posts.category = category
    #현재가 최저가 추출
    for post in posts:
        post.Low_price = get_product_val(post.id,'low')
        post.price = get_product_val(post.id,'now')
        post.week_prices = get_product_week_val(post.id)
    return render(request, 'product/index.html',
                  {'posts': posts, 'request': request})
def get_product_week_val(pid):
    date_format = '%Y-%m-%dT%H:%M:%S.%f+00:00'
    product_info = Product.objects.get(id=pid)
    cate_name = findCategory(product_info.category)
    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
    query_api = client.query_api()
    query = ('''
        from(bucket:"qrqr")
        |> range(start: -7d, stop: now() )
        |> filter(fn: (r) => r["_measurement"] == "dragon_nest" and r["{0}"] == "1" and r["pid"] == "{1}" and r["_field"] == "Low_price")
        |> window(every: 1d)
        |> last()
        |> window(every: inf)
       ''').format(cate_name, pid)
    tables = query_api.query(query).to_json(indent=5)
    json_objects = json.loads(tables)
    for week_prices in json_objects:
        week_prices['value'] = week_prices['_value']
        week_prices['time'] = week_prices['_time']
        date_dt  = datetime.datetime.strptime(week_prices['_time'], date_format)
        week_prices['time_w'] = date_dt.strftime('%a')
        del week_prices['_value']
        del week_prices['_time']
    return json_objects

def get_product_val(pid,type):
    product_info = Product.objects.get(id=pid)
    cate_name = findCategory(product_info.category)
    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
    query_api = client.query_api()
    # 현재가 뽑아오는녀석
    if type == 'low':
        query=('''
            from(bucket:"qrqr")
            |> range(start: -365d, stop: now())
            |> filter(fn: (r) => r["_measurement"] == "dragon_nest" and r["{0}"] == "1" and r["pid"] == "{1}" and r["_field"] == "Low_price")
            |> sort(columns: ["_value"])
            |> limit(n:1)
           ''').format(cate_name,pid)
    else:
        query = ('''
            from(bucket:"qrqr")
            |> range(start: -1000m)
            |> filter(fn: (r) => r["_measurement"] == "dragon_nest" and r["{0}"] == "1" and r["pid"] == "{1}" and r["_field"] == "Low_price")
            |> last()
        ''').format(cate_name,pid)
    tables = query_api.query(query)
    for table in tables:
        for record in table.records:
            return(record['_value'])

@login_required(login_url='login')
def like(request,pid):
    spage = request.GET.get('page','')
    # 어떤 게시물에, 어떤 사람이 like를 했는 지
    post = Product.objects.get(id=pid) # 게시물 번호 몇번인지 정보 가져옴
    user = request.user
    if post.like.filter(id=request.user.id).exists(): # 유저면 알아서 유저의 id로 검색해줌
        #구독 삭제
        guduck_fc(request.user.id,pid,"remove")
        post.like.remove(user)
    else:
        guduck_fc(request.user.id, pid, "add")
        post.like.add(user) # post의 like에 현재유저의 정보를 넘김
    if spage :
      return redirect('/list/'+ post.category+'?page='+spage)
    else :
      return redirect('/list/'+post.category)



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

def findCategory(queryData):
    if queryData == '1':
        return "CPU"
    elif queryData == '2':
        return "MAIN_BOARD"
    elif queryData == '3':
        return "RAM"
    elif queryData == '4':
        return "SSD"
    elif queryData == '5':
        return "GPU"
    elif queryData == '6':
        return "POWER"