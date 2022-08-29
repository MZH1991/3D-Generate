import numpy as np
import matplotlib.pyplot as plt
import math
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
import os
Allomatrix = np.array([[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]])  #一个八个方向，每个数组代表一个方向移动，
Sect0 = 40
# cata = 'test'
imgsize = 5001  
oripixel = 64 
noipixel = 64 
bkgrate = 0   
def move(direction, img):   
    assert direction in [-1, 0, 1], "direction should be in [-1, 0, 1]"
    if direction == 0:
        return img
    elif direction == 1:
        return np.concatenate((img[1:, 1:], np.zeros(img.shape[1]).reshape(1, -1)), axis = 0)
    elif direction == -1:
        return np.concatenate((np.zeros(img.shape[1]).reshape(1, -1), img[:-1]), axis = 0)

ims = 27 
for numk in range(1,imgsize):
    nn = 0
    nnn = 0
    mm = 0

    folder1 = 'F:/Data Base/learning/shift' + str(oripixel) + str(noipixel) + '/before/'
    folder2 = 'F:/Data Base/learning/shift' + str(oripixel) + str(noipixel) + '/after/' 
    folder3 = 'F:/Data Base/learning/shift' + str(oripixel) + str(noipixel) + '/label/'

    
    if not os.path.exists(folder1): 
        os.makedirs(folder1)
    if not os.path.exists(folder2):
        os.makedirs(folder2)
    if not os.path.exists(folder3):
        os.makedirs(folder3)

    m12menmory = [[0,0,0],[0,0,0]]
    a = np.zeros((ims,ims,ims))
    b = np.zeros((ims,ims,ims))
    c = np.zeros((ims,ims,ims))
    m12menmory = np.array(m12menmory)
    while nn < oripixel:
        m1 = np.random.randint(3,ims-3)
        m2 = np.random.randint(3,ims-3)
        m3 = np.random.randint(3,ims-3)

        kk = [m1,m2,m3]
        k01 = a[m1-1,m2-1,m3]
        k02 = a[m1-1,m2,m3]
        k03 = a[m1-1,m2+1,m3]
        k04 = a[m1,m2-1,m3]
        k05 = a[m1,m2,m3]
        k06 = a[m1,m2+1,m3]
        k07 = a[m1+1,m2-1,m3]
        k08 = a[m1+1,m2,m3]
        k09 = a[m1+1,m2+1,m3]

        k11 = a[m1-1,m2-1,m3-1]
        k12 = a[m1-1,m2,m3-1]
        k13 = a[m1-1,m2+1,m3-1]
        k14 = a[m1,m2-1,m3-1]
        k15 = a[m1,m2,m3-1]
        k16 = a[m1,m2+1,m3-1]
        k17 = a[m1+1,m2-1,m3-1]
        k18 = a[m1+1,m2,m3-1]
        k19 = a[m1+1,m2+1,m3-1]

        k21 = a[m1-1,m2-1,m3+1]
        k22 = a[m1-1,m2,m3+1]
        k23 = a[m1-1,m2+1,m3+1]
        k24 = a[m1,m2-1,m3+1]
        k25 = a[m1,m2,m3+1]
        k26 = a[m1,m2+1,m3+1]
        k27 = a[m1+1,m2-1,m3+1]
        k28 = a[m1+1,m2,m3+1]
        k29 = a[m1+1,m2+1,m3+1]

        judge = k01 + k02 + k03 + k04 + k05 + k06 + k07 + k08 + k09 + k11 + k12 + k13 + k14 + k15 + k16 + k17 + k18 + k19 + k21 + k22 + k23 + k24 + k25 + k26 + k27 + k28 + k29

        if k05 > 0:
            nn = nn
        else:
            nn = nn+ 1
            m12menmory = np.row_stack((m12menmory, kk))
            a[m1][m2][m3] = 1
    aaa = a
    while nnn < noipixel:
        m1 = np.random.randint(3,ims-3)
        m2 = np.random.randint(3,ims-3)
        m3 = np.random.randint(3,ims-3)
        kk = [m1,m2,m3]

        k01 = aaa[m1-1,m2-1,m3]
        k02 = aaa[m1-1,m2,m3]
        k03 = aaa[m1-1,m2+1,m3]
        k04 = aaa[m1,m2-1,m3]
        k05 = aaa[m1,m2,m3]
        k06 = aaa[m1,m2+1,m3]
        k07 = aaa[m1+1,m2-1,m3]
        k08 = aaa[m1+1,m2,m3]
        k09 = aaa[m1+1,m2+1,m3]

        k11 = aaa[m1-1,m2-1,m3-1]
        k12 = aaa[m1-1,m2,m3-1]
        k13 = aaa[m1-1,m2+1,m3-1]
        k14 = aaa[m1,m2-1,m3-1]
        k15 = aaa[m1,m2,m3-1]
        k16 = aaa[m1,m2+1,m3-1]
        k17 = aaa[m1+1,m2-1,m3-1]
        k18 = aaa[m1+1,m2,m3-1]
        k19 = aaa[m1+1,m2+1,m3-1]

        k21 = aaa[m1-1,m2-1,m3+1]
        k22 = aaa[m1-1,m2,m3+1]
        k23 = aaa[m1-1,m2+1,m3+1]
        k24 = aaa[m1,m2-1,m3+1]
        k25 = aaa[m1,m2,m3+1]
        k26 = aaa[m1,m2+1,m3+1]
        k27 = aaa[m1+1,m2-1,m3+1]
        k28 = aaa[m1+1,m2,m3+1]
        k29 = aaa[m1+1,m2+1,m3+1]

        k10 = b[m1,m2,m3]
        judge = k01 + k02 + k03 + k04 + k05 + k06 + k07 + k08 + k09 + k10 + k11 + k12 + k13 + k14 + k15 + k16 + k17 + k18 + k19 + k21 + k22 + k23 + k24 + k25 + k26 + k27 + k28 + k29       
        if judge > 0 :
            nnn = nnn
        else:
            nnn = nnn + 1
            m12menmory = np.row_stack((m12menmory, kk))
            b[m1][m2][m3] = 1


    c = a + b

    Matran = np.random.randint(0,8)
    d = np.zeros((27,27,27))


    am1 = np.random.randint(-1,2)
    am2 = np.random.randint(-1,2)
    am3 = np.random.randint(-1,2)    

    for numk1 in range(0,ims):
        # print(numk1)
        for numk2 in range(0,ims):
            # print(numk2)
            for numk3 in range(0,ims):
                # print([numk1, numk2, numk3])
                if a[numk1, numk2, numk3] == 1:
                    d[numk1 + am1, numk2 + am2, numk3 + am3] = 1
                else:
                    pass
    d = d + b

    # ODC = Allomatrix[Matran,:]
    # a = move(ODC[0], a) 
    # a = a.T 
    # a = move(-ODC[1], a) 
    # a = a.T   
    # # ODC = ODC[::-1]
    # loc = np.nonzero(b)
    # loc = np.array(loc)
    # nums = loc.shape[1]

    # for num2 in range(nums):
    #     Matran0 = np.random.randint(0,8)
    #     ODC0 = Allomatrix[Matran0,:]
    #     LL = loc[:,num2]
    #     b[loc[:,num2][0],loc[:,num2][1]] = 0        
    #     b[loc[:,num2][0]-ODC0[0],loc[:,num2][1]+ODC0[1]] = 1
 



    # d = a + b
    # # d = np.int64(d>0)

    # d = np.array(d, dtype=bool)

    # c = c.flatten()
    # d = d.flatten()
    # e = np.concatenate((c,d),axis=0)

    # label = Matran + 1

    # file1 = 'G:/Data Base/learning/shift' + str(Sect0) + '/' + str(cata) + '/' + str(numk) + '.txt'

    # file2 = 'G:/Data Base/learning/shift' + str(Sect0) + '/' + str(cata) + '/' + str(numk) + '.txt' + '_' + str
    # path0 = 'G:/Data Base/learning/shift' + str(Sect0) + '/' + str(cata) + '/' + 'codex.txt'

    # with open(path0,'a') as file_handle:  
    #     file_handle.write(file2)    
    #     file_handle.write('\n')         
    # np.savetxt(file1,e,fmt='%d',delimiter=' ')

    OD = (am1,am2,am3)
    ODD = (am1 + 1)+3*(am2 + 1)+9*(am3 + 1)

    OD = np.zeros(27)

    OD[ODD] = 1

    # label = Matran + 1
    file1 = 'F:/Data Base/learning/shift' + str(oripixel) + str(noipixel) + '/before/' + str(numk) + '.npy'
    file2 = 'F:/Data Base/learning/shift' + str(oripixel) + str(noipixel) + '/after/' + str(numk) + '.npy' 
    file3 = 'F:/Data Base/learning/shift' + str(oripixel) + str(noipixel) + '/label/' + str(numk) + '.npy'

    np.save(file1, arr=c)
    np.save(file2, arr=d)
    np.save(file3, arr=OD)


print("The End")






