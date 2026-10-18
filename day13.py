import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['axes.unicode_minus']=False
df=pd.read_csv(r'C:\Users\Rhysl\ai-learning\code\week02\students.csv')
one=df[df['班级']=='一班'].reset_index(drop=True)
fig,ax=plt.subplots(2,2,figsize=(11,8))
g = df.groupby('班级')['语文'].mean()
ax[0,0].bar(g.index, g.values, width=0.4)
ax[0,1].scatter(df['语文'], df['数学'], s=70, alpha=0.7)
ax[0,1].set_title('语文 vs 数学')
ax[1,0].hist(df['总分'].dropna(), bins=8)
ax[1,0].set_title('总分分布')
data = [df['语文'].dropna(), df['数学'].dropna(), df['英语'].dropna()]
ax[1,1].boxplot(data, tick_labels=['语文', '数学', '英语'])
ax[1,1].set_title('三科成绩分布')
ax[0,0].set_title('各班语文平均分')
ax[1,1].set_ylabel('分数')
plt.tight_layout()
plt.savefig('my_charts.png',dpi=150)
plt.show()