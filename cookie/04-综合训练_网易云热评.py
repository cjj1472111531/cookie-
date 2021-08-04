# coding=gbk
# @file:04-综合训练_网易云热评.py
# @data:2021/8/4 15:25
# Editor:clown
# 1.找到未加密的参数
import requests

url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
#请求方式为POST
requests.post()
'''
initiator从下往上执行的js脚本

'''
# 2.想办法把参数进行加密（按照参考网易的逻辑），params，enSecKey
# 3.请求到网易，拿到热评
