# coding=gbk
# @file:01-cookie.py
# @data:2021/7/28 23:06
# Editor:clown
#15574426396
#qq1472111531
#登录-》得到cookie
#带着cookie 去请求url->书架上的内容

#必须连着上面的两个操作链接起来
'''
我们可以使用session进行请求-》session你可以进行一连串请求
在这个过程中cookie不会丢失
'''
import requests
#会话
session=requests.session()
data={
"loginName": "15574426396",
"password": "qq1472111531"
}
session
#1.先登录
url="https://passport.17k.com/ck/user/login"
# resp=session.post(url,data=data)
session.post(url,data=data)
#print(resp.text)
#print("-"*30)
#print(resp.cookies)  #看cookie

#2.拿到书架上的数据
#刚才的session是有cookie的
book_url="https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
resp=session.get(book_url)
# print(resp.json())
dic=resp.json()
# print(dic)
# for i in dic.value():
for i in dic['data']:
    print(i["bookName"],end="--")
    print(i["bookClass"]['name'],end="--")
    print(i["bookCategory"]['name'],end='--')
    print(i["lastUpdateChapter"]['name'])
    # print(i['introduction'])


# A->B
# B->A
# A->B


