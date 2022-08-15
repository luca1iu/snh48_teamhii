print('hello world')
import re
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/103.0.0.0 Safari/537.36'}

# 获取弹幕文件
cid = '375937815'
xml = "https://comment.bilibili.com/{}.xml".format(cid)
# xml = 'https://api.bilibili.com/x/v1/dm/list.so?oid={}'.format(cid)
response = requests.get(xml, headers)
response.encoding = 'utf-8'
xml_text = response.text
soup = BeautifulSoup(xml_text, 'html.parser')
barrages = [re.sub(r'\s+', '', bar.text) for bar in soup.find_all('d')]

# 查看弹幕数量
print('弹幕数量：' + str(len(barrages)))

# 将弹幕写入文件
with open('./barrages.txt', 'w', encoding='utf-8') as output_file:
    for bar in barrages:
        output_file.write(bar + '\n')
print('弹幕信息已成功写入文件！')


