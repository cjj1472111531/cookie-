# coding=gbk
# @file:03-����.py
# @data:2021/8/4 12:18
# Editor:clown
# ԭ�� ͨ����������һ��������������
import requests
# 47.111.71.29:8081 #�����Ƕ˿ڵ���˼  d����������
proxies={
    "http":"https://47.111.71.29:8081"
    #"https":""

}
resp = requests.get("https://www.baidu.com/",proxies=proxies)
resp.encoding = "utf-8"
print(resp.text)



