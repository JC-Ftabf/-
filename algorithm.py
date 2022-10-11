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
coe = np.load("course0.npy")
stu = np.load("student0.npy")

na = np.zeros((11,1))
nx = np.zeros((11,1))
wg = np.zeros((90,2))
e = np.zeros((20,1))
### 点名算法
#第一次点名
count = 0
i = 0
while i<90: #更新stu矩阵信息
    if coe[i][0]:
        stu[i][1]+=1
        count+=1
    i+=1
i = 0 #列出下次课同学点名权重
while i<90:
    flag = 0
    if coe[i][0]:
        flag = 1
    wg[i][1] = flag*0.1+stu[i][1]/20*0.9
    i+=1
e[0][0] = count / 90
#print(coe)
#print(stu)
#print(wg)
#第n次点名
i = 1
while i<20:
    count = 0
    wg1 = np.lexsort(-wg.T) #按照最后一列降序排序
    wg = wg[wg1, :]
    j = 0
    while j<11: #列出本次要点名的同学的名单
        nx[j][0] = wg[j][0]
        j+=1
    j = 0
    while j < 11:
        p = int(nx[j][0] - 1)
        if coe[p][i]:  # 如果被点名到的学生缺勤
            na[j][0] = p+1  # 记录下该学生的id号
            count += 1
        else:
            na[j][0] = 0
        j += 1
    j = 0
    while j < 11:  # 更新stu矩阵信息
        if na[j][0]:
            p = int(na[j][0] - 1)
            stu[p][1] += 1  # 若缺勤则累计缺勤次数加1
        j += 1
    j = 0  # 列出下次课同学点名权重
    while j < 90:
        k = 0
        flag = 0
        while k < 11:  # 核对na矩阵，查看该学生是否本次课缺勤
            if na[k][0] == j + 1:
                flag = 1
            k += 1
        wg[j][1] = flag*0.1+  stu[j][1] * 0.9 / 20
        j += 1
    e[i][0] = count/5
    i += 1

i = 0
E1 = 0
while i<20:
    E1+=e[i][0];
    i+=1
E1/=20
#print(e)

coe = np.load("course1.npy")
stu = np.load("student1.npy")

na = np.zeros((11,1))
nx = np.zeros((11,1))
wg = np.zeros((90,2))
e = np.zeros((20,1))
### 点名算法
#第一次点名
count = 0
i = 0
while i<90: #更新stu矩阵信息
    if coe[i][0]:
        stu[i][1]+=1
        count+=1
    i+=1
i = 0 #列出下次课同学点名权重
while i<90:
    flag = 0
    if coe[i][0]:
        flag = 1
    wg[i][1] = flag*0.1+stu[i][1]/20*0.9
    i+=1
e[0][0] = count / 90
#print(coe)
#print(stu)
#print(wg)
#第n次点名
i = 1
while i<20:
    count = 0
    wg1 = np.lexsort(-wg.T) #按照最后一列降序排序
    wg = wg[wg1, :]
    j = 0
    while j<11: #列出本次要点名的同学的名单
        nx[j][0] = wg[j][0]
        j+=1
    j = 0
    while j < 11:
        p = int(nx[j][0] - 1)
        if coe[p][i]:  # 如果被点名到的学生缺勤
            na[j][0] = p+1  # 记录下该学生的id号
            count += 1
        else:
            na[j][0] = 0
        j += 1
    j = 0
    while j < 11:  # 更新stu矩阵信息
        if na[j][0]:
            p = int(na[j][0] - 1)
            stu[p][1] += 1  # 若缺勤则累计缺勤次数加1
        j += 1
    j = 0  # 列出下次课同学点名权重
    while j < 90:
        k = 0
        flag = 0
        while k < 11:  # 核对na矩阵，查看该学生是否本次课缺勤
            if na[k][0] == j + 1:
                flag = 1
            k += 1
        wg[j][1] = flag*0.1+  stu[j][1] * 0.9 / 20
        j += 1
    e[i][0] = count/3
    i += 1

i = 0
E2 = 0
while i<20:
    E2+=e[i][0];
    i+=1
E2/=20
#print(e)

coe = np.load("course2.npy")
stu = np.load("student2.npy")

na = np.zeros((11,1))
nx = np.zeros((11,1))
wg = np.zeros((90,2))
e = np.zeros((20,1))
### 点名算法
#第一次点名
count = 0
i = 0
while i<90: #更新stu矩阵信息
    if coe[i][0]:
        stu[i][1]+=1
        count+=1
    i+=1
i = 0 #列出下次课同学点名权重
while i<90:
    flag = 0
    if coe[i][0]:
        flag = 1
    wg[i][1] = flag*0.1+stu[i][1]/20*0.9
    i+=1
e[0][0] = count / 90
#print(coe)
#print(stu)
#print(wg)
#第n次点名
i = 1
while i<20:
    count = 0
    wg1 = np.lexsort(-wg.T) #按照最后一列降序排序
    wg = wg[wg1, :]
    j = 0
    while j<11: #列出本次要点名的同学的名单
        nx[j][0] = wg[j][0]
        j+=1
    j = 0
    while j < 11:
        p = int(nx[j][0] - 1)
        if coe[p][i]:  # 如果被点名到的学生缺勤
            na[j][0] = p+1  # 记录下该学生的id号
            count += 1
        else:
            na[j][0] = 0
        j += 1
    j = 0
    while j < 11:  # 更新stu矩阵信息
        if na[j][0]:
            p = int(na[j][0] - 1)
            stu[p][1] += 1  # 若缺勤则累计缺勤次数加1
        j += 1
    j = 0  # 列出下次课同学点名权重
    while j < 90:
        k = 0
        flag = 0
        while k < 11:  # 核对na矩阵，查看该学生是否本次课缺勤
            if na[k][0] == j + 1:
                flag = 1
            k += 1
        wg[j][1] = flag*0.1+  stu[j][1] * 0.9 / 20
        j += 1
    e[i][0] = count/3
    i += 1

i = 0
E3 = 0
while i<20:
    E3+=e[i][0];
    i+=1
E3/=20
#print(e)

coe = np.load("course3.npy")
stu = np.load("student3.npy")

na = np.zeros((11,1))
nx = np.zeros((11,1))
wg = np.zeros((90,2))
e = np.zeros((20,1))
### 点名算法
#第一次点名
count = 0
i = 0
while i<90: #更新stu矩阵信息
    if coe[i][0]:
        stu[i][1]+=1
        count+=1
    i+=1
i = 0 #列出下次课同学点名权重
while i<90:
    flag = 0
    if coe[i][0]:
        flag = 1
    wg[i][1] = flag*0.1+stu[i][1]/20*0.9
    i+=1
e[0][0] = count / 90
#print(coe)
#print(stu)
#print(wg)
#第n次点名
i = 1
while i<20:
    count = 0
    wg1 = np.lexsort(-wg.T) #按照最后一列降序排序
    wg = wg[wg1, :]
    j = 0
    while j<11: #列出本次要点名的同学的名单
        nx[j][0] = wg[j][0]
        j+=1
    j = 0
    while j < 11:
        p = int(nx[j][0] - 1)
        if coe[p][i]:  # 如果被点名到的学生缺勤
            na[j][0] = p+1  # 记录下该学生的id号
            count += 1
        else:
            na[j][0] = 0
        j += 1
    j = 0
    while j < 11:  # 更新stu矩阵信息
        if na[j][0]:
            p = int(na[j][0] - 1)
            stu[p][1] += 1  # 若缺勤则累计缺勤次数加1
        j += 1
    j = 0  # 列出下次课同学点名权重
    while j < 90:
        k = 0
        flag = 0
        while k < 11:  # 核对na矩阵，查看该学生是否本次课缺勤
            if na[k][0] == j + 1:
                flag = 1
            k += 1
        wg[j][1] = flag*0.1+  stu[j][1] * 0.9 / 20
        j += 1
    e[i][0] = count/5
    i += 1

i = 0
E4 = 0
while i<20:
    E4+=e[i][0];
    i+=1
E4/=20
#print(e)

coe = np.load("course4.npy")
stu = np.load("student4.npy")

na = np.zeros((11,1))
nx = np.zeros((11,1))
wg = np.zeros((90,2))
e = np.zeros((20,1))
### 点名算法
#第一次点名
count = 0
i = 0
while i<90: #更新stu矩阵信息
    if coe[i][0]:
        stu[i][1]+=1
        count+=1
    i+=1
i = 0 #列出下次课同学点名权重
while i<90:
    flag = 0
    if coe[i][0]:
        flag = 1
    wg[i][1] = flag*0.1+stu[i][1]/20*0.9
    i+=1
e[0][0] = count / 90
#print(coe)
#print(stu)
#print(wg)
#第n次点名
i = 1
while i<20:
    count = 0
    wg1 = np.lexsort(-wg.T) #按照最后一列降序排序
    wg = wg[wg1, :]
    j = 0
    while j<11: #列出本次要点名的同学的名单
        nx[j][0] = wg[j][0]
        j+=1
    j = 0
    while j < 11:
        p = int(nx[j][0] - 1)
        if coe[p][i]:  # 如果被点名到的学生缺勤
            na[j][0] = p+1  # 记录下该学生的id号
            count += 1
        else:
            na[j][0] = 0
        j += 1
    j = 0
    while j < 11:  # 更新stu矩阵信息
        if na[j][0]:
            p = int(na[j][0] - 1)
            stu[p][1] += 1  # 若缺勤则累计缺勤次数加1
        j += 1
    j = 0  # 列出下次课同学点名权重
    while j < 90:
        k = 0
        flag = 0
        while k < 11:  # 核对na矩阵，查看该学生是否本次课缺勤
            if na[k][0] == j + 1:
                flag = 1
            k += 1
        wg[j][1] = flag*0.1+  stu[j][1] * 0.9 / 20
        j += 1
    e[i][0] = count/2
    i += 1

i = 0
E5 = 0
while i<20:
    E5+=e[i][0];
    i+=1
E5/=20
#print(e)
E = 0
E = (E1+E2+E3+E4+E5)/5


print('五门课程平均评价标准为',E)
