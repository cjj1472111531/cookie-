# coding=gbk
# @file:03-代理.py
# @data:2021/8/4 12:18
# Editor:clown
# 原理 通过第三方的一个机器发送请求
import requests
# 47.111.71.29:8081 #后面是端口的意思  d代理代理代理
proxies={
    "http":"https://47.111.71.29:8081"
    #"https":""

}
resp = requests.get("https://www.baidu.com/",proxies=proxies)
resp.encoding = "utf-8"
print(resp.text)



