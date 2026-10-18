#1
import numpy as np
arr1=np.array([1,2,3,4,5,6,7,8,9,10])
print(arr1**2)
print(arr1+100)
#2
arr2=np.random.randint(1,100,10)
print(arr2)
print(arr2.max())
print(arr2.min())
print(arr2.sum())
print(arr2.mean())
#3
arr3=np.arange(1,13)
print(arr3)
arr3=arr3.reshape(3,4)
print(arr3)
print(arr3.shape)
print(arr3.ndim)
print(arr3.size)
print(arr3.dtype)
#4
print(arr3[1])
print(arr3[:,2])
print(arr3[1,2])
print(arr3[0])
#5
arr5=np.random.randint(1,100,20)
print(arr5)
print(arr5[arr5>50])
print(arr5[arr5>50].size)
#6
arr6=np.arange(1,13)
arr6=arr6.reshape(3,4)
print(arr6)
print(arr6.sum())
print(arr6.sum(axis=1))
print(arr6.sum(axis=0))
#7
arr7=np.arange(1,7)
arr7=arr7.reshape(2,3)
print(arr7)
arr7.T
print(arr7.T)
print(arr7.T.shape)
#8
scores = np.array([
    [90, 85, 88],
    [78, 92, 80],
    [85, 79, 95],
    [60, 70, 65],
    [95, 98, 92],
])
scores_student=scores.sum(axis=1)
print('全班的平均分')
print(scores_student.mean())
print('每个学生的总分')
print(scores_student)
print('每个学生的平均分')
print(scores.sum(axis=1)/3)
print('每科的平均分')
print(scores.sum(axis=0)/5)
print('最高分是多少、出现在哪个学生哪一科')
print(scores.max(),np.argmax(scores)%3)
if(np.argmax(scores)%3==2):
    print(f'最高分是{scores.max()}，在英语科目')
elif(np.argmax(scores)%3==1):
    print(f'最高分是{scores.max()}，在数学科目')
elif(np.argmax(scores)%3==0):
    print(f'最高分是{scores.max()}，在语文科目')
print('有没有学生有科目不及格（< 60）？用布尔索引找出所有不及格的分数')
x=scores[scores<60].size
if(x==0):
    print('没有学生不及格')
else:
    print(scores[scores<60]) 

