# coding=gbk
# @file:02-������_����Ƶ.py
# @data:2021/8/4 9:32
# Editor:clown
import requests

# 1.�õ���Ƶ��ַ,�õ�contID ͨ���Աȵõ�
url = "https://www.pearvideo.com/video_1737528"
contID_my = url[-7:] #����Ƭ
contID=url.split('_')[1] #���ݡ�_�������и� ѡȡ��һ���»��ߺ��������
# 2.�õ�videoStatus���ص�json-��srcurl
#����������޸�
videoStatus=f"https://www.pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.15583344380653297"
#����ͷ�����пո�
headers={
    "User-Agent":"Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko)Chrome/91.0.4472.124 Safari/537.36",
    "Referer": url
     # ������:referer  ��Դ ����ǰ�����������һ����˭
  # "Referer": " https://www.pearvideo.com/video_1737528"

}
resp=requests.get(videoStatus,headers=headers)
clown=resp.json()
print(resp.json())
# 3.�� srcURL �������ݽ����޸�
systime=clown['systemTime']
srcurl=clown['videoInfo']['videos']['srcUrl']

#srcurl='https://video.pearvideo.com/mp4/adshort/20210803/1628049619259-15737121_adpkg-ad_hd.mp4'
# ��ʵ��Ƶ����
# https://video.pearvideo.com/mp4/adshort/20210803/cont-1737528-15737121_adpkg-ad_hd.mp4
srcurl=srcurl.replace(systime,f"cont-{contID}")
print(srcurl)
# 4.������Ƶ
with open("lalal.mp4",mode='wb') as f:
    f.write(requests.get(srcurl).content)
