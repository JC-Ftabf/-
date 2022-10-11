'''
写在最前面:
1.矩阵含义
coe[90][20]:单门课程90位学生，20次课是否缺勤情况登记表，缺勤登记为1，否则登记为0
stu[90][2]:90位学生情况登记表，第一列表示绩点，第二列表示累计缺勤次数
na[11][1]:点名情况登记表，点名11位同学，若不缺勤则登记为0，若缺勤则将索引值记录下来
nx[11][1]:下次课要被点名的同学的名单
wg[90][2]:同学在下次课被点名的权重矩阵,第一列表示学生id，第二列表示权重值
e[20][1]:命中率
2.算法介绍
将na矩阵中单次课点名情况作为下一次课点名的参考依据，占比40%，将学生绩点考虑在点名比重中，用（|学生绩点-绩点平均值|）/2作为参考依据，占比30%。将累计缺勤次数考虑在点名比重中，用累计缺勤次数*0.3/20作为参考依据，占比30%；
第一次点名为随机任意点名，从第二次点名开始将所有参考依据相加得到90位同学的权重值，选择权重值最大的11位作为下次点名的对象
'''
import numpy as np
np.set_printoptions(threshold=np.inf)
import random

na = np.zeros((11,1))
nx = np.zeros((11,1))
wg = np.zeros((90,2))
e = np.zeros((20,1))

i = 0
while i<90: #初始化学生id
    wg[i][0] = i+1
    i+=1
#print(wg)

def randint_generation(min, max, mount): #生成n个不重复整数
    list = []
    while len(list) != mount:
        unit = random.randint(min, max)
        if unit not in list:
            list.append(unit)
    return list

### 生成学生上课情况矩阵coe
coe = np.zeros((90,20)) #创建90行20列的全0矩阵，其中行表示该班级对应的90位学生，20列表示20次课，0代表不缺勤，1代表缺勤
num = random.randint(5,8) #生成有范围为5-8的随机数，代表有n位同学本学期缺勤80%的课
#print(num)
while num>0:
        k = random.randint(0,89) #随机选取一位同学
        ab = randint_generation(0, 19, 16) #在20门课中挑选出16门课代表该同学缺勤的课
        i = 0
        while i<16:
            coe[k][ab[i]] = 1 #更新coe矩阵，将缺勤的16门课记录为1
            i+=1
        num-=1
i = 0
while i<20:
    num = random.randint(0, 3)  #生成有范围为0-3的随机数，代表某门课程有n位缺勤
    while num>0:
        k = random.randint(0, 89)  #随机选取一位同学
        while coe[k][i]:
            k = random.randint(0, 89)  #如果k位同学该门课程已经被登记为缺勤那么重新生成随机数
        coe[k][i] = 1
        num-=1
    i+=1
#print(coe)
#print(ab)

### 生成学生信息记录情况，90行2列，其中第1列记录学生成绩（呈正态分布），第2列记录学生累计缺勤次数
stu = np.zeros((90,2)) #创建90行2列矩阵，其中行表示该班级对应的90位学生，第一列代表绩点，第二列代表累计缺勤次数
i = 0
while i<90:
    stu[i][0] = random.uniform(1.5,3.96) #随机生成学生的绩点，区间在1.5-3.96之间
    i+=1
sum = 0
i = 0
while i<90:
    sum+=stu[i][0]
    i+=1
ave = sum/90 #求出绩点平均值
#print(stu)
print("单门课程缺勤情况登记表:(共90行表示90位学生，20列表示20次课，缺课则登记为1)\n",coe)
print("\n学生信息登记表:(第一列为绩点，第二列为累计缺勤次数)\n",stu)

#以二进制文件的格式保存生成的数组
np.save("course4.npy",coe)
np.save("student4.npy",stu)
