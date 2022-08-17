import jieba
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt  # 画图

# 读取停用词库,注意编码应为‘utf8’
f = open('stopwords.txt', encoding='utf8')
stopwords = f.read().split('\n')
print(stopwords)  # 打印停用词

f.close()  # 关闭停用词文件(・。・)
with open("barrages.txt", "r", encoding='utf8') as fp:
    text = fp.read()

segs = jieba.cut(text)  # 进行jieba分词
mytext_list = []  # 构建一个容纳过滤掉停用词的弹幕数据文件

# 文本清洗
for seg in segs:  # 循环遍历每一个分词文本
    # 如果该词不属于停用词表 并且非空 长度不为1
    if seg not in stopwords and seg != "" and len(seg) != 1:
        # 将该词语添加到mytext_list列表中
        mytext_list.append(seg.replace(" ", ""))

print(mytext_list)  # 打印过滤后的弹幕数据
cloud_text = ",".join(mytext_list)  # 连接列表里面的词语
print(cloud_text)

plt.figure()  # 图形窗口
wc = WordCloud(
    background_color="white",  # 背景颜色
    max_words=200,  # 显示最大次数
    font_path=r'C:/Windows/Fonts/STXINGKA.TTF',  # 字体
    width=400,  # 宽
    height=200,  # 高
    scale=10).generate(cloud_text)  # 迭代生成词云
wc.to_file("我的第一个词云.png")
plt.imshow(wc, interpolation="bilinear")  # 插值为双线性,会使显示平滑更加平滑
plt.axis("off")  # 坐标轴隐藏
plt.show()
print("成功!")

