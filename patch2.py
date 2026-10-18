# ================================================
# 补丁练习 2/2   ·   2026-10-13   ·   约 20 分钟
# ================================================
# 规则同上：不许看旧代码，凭记忆写，写完运行。
# ================================================


# --- 5 · 字典计数器 --------------------------------
# 统计 'abracadabra' 里每个字符出现的次数。
# 检验标准：'a' 应该是 5 次。
# 提示：核心是 counts.get(ch, 0) + 1
text='abracadabra'
counts={}
for i in text:
    counts[i]=counts.get(i,0)+1
print(counts)



# --- 6 · get 的安全取值 ----------------------------
# d = {'name': 'Rhys', 'age': 19}
# 取出 'score'，要求【不报错】，并且缺省值是 0。
# 顺便：用 d['score'] 试一次，看看会报什么错（把报错抄进注释）
d = {'name': 'Rhys', 'age': 19}
print(d.get('score',0))





# --- 7 · NumPy axis --------------------------------
# m = np.arange(1, 13).reshape(3, 4)
# 输出三样：所有元素的和、每行的和、每列的和
# 检验标准：每行和应该是 3 个数，每列和应该是 4 个数
import numpy as np
m = np.arange(1, 13).reshape(3, 4)
print(m)
print(m.sum())
print(m.sum(axis=1))
print(m.sum(axis=0))






# --- 8 · Pandas 三连 -------------------------------
# 读 students.csv，然后：
#   ① 打印 info()
#   ② 找出语文 > 85 的学生，只要【姓名】和【语文】两列
#   ③ 按班级分组，算数学平均分
# 提示：② 用 df.loc[行条件, 列列表]
import pandas as pd
df=pd.read_csv(r'C:\Users\Rhysl\ai-learning\code\week02\students.csv')
print(df.info())
print(df.loc[df['语文'] > 85, ['姓名', '语文']])
print(df.groupby('班级')['数学'].mean().round(1))




# ================================================
# 做完把整个文件贴给我批改。
# ================================================
