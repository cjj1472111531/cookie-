# coding=gbk
# @file:01-cookie.py
# @data:2021/7/28 23:06
# Editor:clown
#15574426396
#qq1472111531
#��¼-���õ�cookie
#����cookie ȥ����url->����ϵ�����

#�����������������������������
'''
���ǿ���ʹ��session��������-��session����Խ���һ��������
�����������cookie���ᶪʧ
'''
import requests
#�Ự
session=requests.session()
data={
"loginName": "15574426396",
"password": "qq1472111531"
}
session
#1.�ȵ�¼
url="https://passport.17k.com/ck/user/login"
# resp=session.post(url,data=data)
session.post(url,data=data)
#print(resp.text)
#print("-"*30)
#print(resp.cookies)  #��cookie

#2.�õ�����ϵ�����
#�ղŵ�session����cookie��
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


