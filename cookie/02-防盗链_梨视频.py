# coding=gbk
# @file:02-防盗链_梨视频.py
# @data:2021/8/4 9:32
# Editor:clown
import requests

# 1.拿到视频网址,拿到contID 通过对比得到
url = "https://www.pearvideo.com/video_1737528"
contID_my = url[-7:] #找切片
contID=url.split('_')[1] #根据“_”进行切割 选取第一个下划线后面的数字
# 2.拿到videoStatus返回的json-》srcurl
#对这个进行修改
videoStatus=f"https://www.pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.15583344380653297"
#请求头不能有空格
headers={
    "User-Agent":"Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko)Chrome/91.0.4472.124 Safari/537.36",
    "Referer": url
     # 防盗链:referer  溯源 ，当前本次请求的上一级是谁
  # "Referer": " https://www.pearvideo.com/video_1737528"

}
resp=requests.get(videoStatus,headers=headers)
clown=resp.json()
print(resp.json())
# 3.将 srcURL 里面内容进行修改
systime=clown['systemTime']
srcurl=clown['videoInfo']['videos']['srcUrl']

#srcurl='https://video.pearvideo.com/mp4/adshort/20210803/1628049619259-15737121_adpkg-ad_hd.mp4'
# 真实视频链接
# https://video.pearvideo.com/mp4/adshort/20210803/cont-1737528-15737121_adpkg-ad_hd.mp4
srcurl=srcurl.replace(systime,f"cont-{contID}")
print(srcurl)
# 4.下载视频
with open("lalal.mp4",mode='wb') as f:
    f.write(requests.get(srcurl).content)
