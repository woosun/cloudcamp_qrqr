#-*- coding: utf-8 -*-
import urllib.request
import json
import pymysql
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
bucket = "qrqr"
org = "qrqr"
token = "DJFvAGHanKa1AUci8PLbzrhm1UPjayh5Re5ulyFCvx4BVVt8JQVi0rdw0jiwPHAlKLAq1l4N-4DcZR0i8oun2w=="
url = "https://influx.oud.kr"

client = influxdb_client.InfluxDBClient(
        url = url,
        token = token,
        org = org
)
write_api = client.write_api(write_options = SYNCHRONOUS)

# 네이버 API를 사용하기 위한 클라이언트ID 및 클라이언스Secret
client_id = "N_XdOJ1lB5IRk2s3HL8N"
client_secret = "Uu0IUt04du"


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

def find_naver_api(pid,c_name,query_data,create_date):
    searchText = urllib.parse.quote(query_data)
    sort = "sim"
    ex = "used"
    url = "https://openapi.naver.com/v1/search/shop.json?query=" + searchText + "&display=100&sort=" + sort + "&exclude=" + ex
    print(url)
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    p = {}
    if(rescode==200):
        response_body = response.read()
        pyJson = response_body.decode('utf-8')
        json_obj = json.loads(pyJson)
        for i in range (0, len(json_obj['items'])):
            if (json_obj['items'][i]['productType']) == '1':
                # 카테고리 찾아오기
                category = c_name
                pid = pid
                regDate = create_date

                # !# influxDB에 데이터를 전달하는 코드
                p = {
                    'measurement': "dragon_nest",
                    'tags': {
                        category: 1,
                        'pid': str(pid),
                    },
                    'fields': {
                        'name': json_obj['items'][i]['title'],
                        'Low_price': json_obj['items'][i]['lprice'],
                        'producurl': json_obj['items'][i]['link'],
                        'regDate': str(regDate)
                    }
                }
                send_body = []
                send_body.append(p)
                if len(send_body) > 0:
                    write_api.write(bucket, org, send_body)
                    send_body = []

                break;






con = pymysql.connect(
    host='oud.kr',
    user='gedflow',
    password='qwer1234',
    db='qrqr',
    port=8306,
    charset='utf8') # 한글처리 (charset = 'utf8')
sql = "select * from qrqr_product where category=1 and query_yn=1"
with con:
    with con.cursor() as cur:
        cur.execute(sql)
        result = cur.fetchall()
        for data in result:
            pid = data[0]
            c_name = findCategory(data[1])
            query_data = data[6]
            create_date = data[7]
            print(pid)
            print(c_name)
            find_naver_api(pid, c_name, query_data, create_date)



