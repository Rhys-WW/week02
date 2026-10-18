#1
import pandas as pd
df=pd.read_csv(r'C:\Users\Rhysl\ai-learning\code\week02\students.csv')
print(df.head())
print(df.shape)
print(list(df.columns))
print(df.dtypes)
#2
print(df.info())
print (df.describe())
#注释：20行5列/语数外都有缺失值，各一个/数学平均分是74.052632
#3
print(df[['姓名','英语']].head(8))
print(df['姓名'])
#4
print(df.loc[df['语文']>85,['姓名','班级','语文']])
#5
print(df[(df['班级']=='一班')&(df['数学']>=80)])
#6 · 加列 + 排序
#   1) 加一列「总分」 = 语文 + 数学 + 英语
#   2) 加一列「平均分」，保留两位小数
#   3) 按总分降序排列，输出前 5 名的：姓名 / 班级 / 总分 / 平均分
#   提示：df['新列'] = ...      排序：df.sort_values('总分', ascending=False)
#   观察：有几行的总分是 NaN？为什么？
df['总分']=df['语文']+df['数学']+df['英语']
df['平均分']=df[['语文','数学','英语']].mean(axis=1)
print(df.sort_values('总分', ascending=False).head(5)[['姓名','班级','总分','平均分']])
#3行，因为nan会传染
#7 · 分组统计
#   1) 每个班的语文 / 数学 / 英语平均分（保留 1 位小数）
#   2) 每个班各有多少人
#   提示：df.groupby('班级')[['语文','数学','英语']].mean().round(1)
#        数人数：df['班级'].value_counts()
print(df.groupby('班级')[['语文','数学','英语']].mean().round(1))
print(df['班级'].value_counts())


#8 · 缺失值盘点
#   1) 每一列缺几个
#   2) 所有含缺失值的行
#   提示：df.isnull().sum()   /   df[df.isnull().any(axis=1)]
print(df.isnull().sum())
print(df[df.isnull().any(axis=1)])

#9 ★ 对比实验（今天的重点，别跳过）
#   分别用三种方式算「一班的数学平均分」，三个数字都打印出来：
#     ① 原始数据      → df[df['班级']=='一班']['数学'].mean()
#     ② dropna() 之后 → 先删掉有缺失的行，再算
#     ③ fillna(0) 之后 → 先用 0 填，再算
#   最后在注释里写一句话：为什么第 ③ 个是错的？
a=df[df['班级']=='一班']['数学'].mean()
print(f'{a:.2f}')
d1=df.dropna()
b=d1[d1['班级']=='一班']['数学'].mean()
print(f'{b:.2f}')
d2=df.fillna(0)
c=d2[d2['班级']=='一班']['数学'].mean()
print(f'{c:.2f}')
#我测试了三组，3错是因为把缺考记成0了，这段代码要验证三的时候要注意先去掉2的函数
#10 · 导出
#   把第 6 题算好的表存成 result.csv，不要行号
#   提示：df.to_csv('result.csv', index=False)
df.to_csv('result.csv', index=False)

