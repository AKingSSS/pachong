#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# -*- coding: utf-8 -*-
import re  # 正则表达式库
import collections  # 词频统计库
import numpy as np  # numpy数据处理库
import jieba  # 结巴分词
import wordcloud  # 词云展示库
from PIL import Image  # 图像处理库
import matplotlib.pyplot as plt  # 图像展示库
import os  # 系统
import matplotlib.colors as colors  # 颜色

# 字体路径
FONT_PATH = os.environ.get("FONT_PATH",
                           os.path.join(os.path.dirname(__file__), "STXINGKA.TTF"))

# 字体颜色
color = ['#FF0000', '#FF7F00',
         '#FFFF00', '#00FF00',
         '#00FFFF', '#0000FF', '#8B00FF']
colormap = colors.ListedColormap(color)

# 读取文件
fn = open('comment.txt', 'rt', encoding='utf-8')  # 打开文件
string_data = fn.read()  # 读出整个文件
fn.close()  # 关闭文件

# 文本预处理
pattern = re.compile(u'[^0-9A-Za-z\u4e00-\u9fa5]')  # 定义正则表达式匹配模式
string_data = re.sub(pattern, '', string_data)  # 将符合模式的字符去除

# 文本分词
jieba.add_word('罗老师')
seg_list_exact = jieba.cut(string_data, cut_all=False)  # 精确模式分词
object_list = []
remove_words = [u'转发', u'这个', u'微博', ]  # 自定义去除词库

for word in seg_list_exact:  # 循环读出每个分词
    if len(word) > 1 and word not in remove_words:  # 如果不在去除词库中
        object_list.append(word)  # 分词追加到列表

# 词频统计
word_counts = collections.Counter(object_list)  # 对分词做词频统计
word_counts_top = word_counts.most_common(200)  # 获取前10最高频的词
print(word_counts_top)  # 输出检查

# 词频展示
mask = np.array(Image.open('niu.jpg'))  # 定义词频背景
wc = wordcloud.WordCloud(
    font_path=FONT_PATH,  # 设置字体格式
    mask=mask,  # 设置背景图
    max_words=200,  # 最多显示词数
    max_font_size=100,  # 字体最大值
    colormap=colormap
)

wc.generate_from_frequencies(word_counts)  # 从字典生成词云
# 保存图片
result = wc.to_file('luo.png')
plt.imshow(wc)  # 显示词云
plt.axis('off')  # 关闭坐标轴
plt.show()  # 显示图像
