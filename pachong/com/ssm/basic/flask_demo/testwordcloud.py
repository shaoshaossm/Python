import jieba  # 分词
from matplotlib import pyplot as plt  # 绘图可视化
from wordcloud import WordCloud  # 词云
from PIL import Image  # 图片处理
import numpy as np  # 矩阵运算
import sqlite3  # 数据库

conn = sqlite3.connect('test.db')
cur = conn.cursor()
sql = 'select name,address from company'
data = cur.execute(sql)
text = ''
for item in data:
    text = text + item[0]

print(text)
cur.close()
conn.close()
cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))
img = Image.open('639cad061d950a7b7700d56c07d162d9f3d3c9f2.jpg')
img_array = np.array(img)  # 图片->数组
wc = WordCloud(background_color='white',
               mask=img_array,
               font_path='CENTURY.TTF')
wc.generate_from_text(string)
# 绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off') #是否显示坐标轴
# plt.show()
plt.savefig('word.jpg')