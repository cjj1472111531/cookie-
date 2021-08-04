# coding=gbk
# @file:000-request进阶.py
# @data:2021/7/28 22:35
# Editor:clown
# 模拟浏览器登录->处理cookie
# 防盗链处理-》梨视视频数据
# 代理-》防止被封ip
'''
我们在之前的爬虫中其实已经使用过headers了. header为HTTP协
议中的请求头. 一般存放一些和请求内容无关的数据. 有时也会存放
一些安全验证信息.比如常见的User-Agent, token, cookie等.

通过requests发送的请求, 我们可以把请求头信息放在headers中. 也
可以单独进行存放, 最终由requests自动动帮我们拼接成完整的http请
求头.
'''

# 综合训练：抓取网易云音乐评论信息



