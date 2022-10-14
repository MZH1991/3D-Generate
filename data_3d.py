import numpy as np
import matplotlib.pyplot as plt
import math
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
import os


imgsize = 5001  # pic num
oripixel = 1
noipixel = 0
bkgrate = 0


def move(direction, img):  # object motion
    assert direction in [-1, 0, 1], "direction should be in [-1, 0, 1]"
    if direction == 0:
        return img
    elif direction == 1:
        return np.concatenate((img[1:, 1:], np.zeros(img.shape[1]).reshape(1, -1)), axis=0)
    elif direction == -1:
        return np.concatenate((np.zeros(img.shape[1]).reshape(1, -1), img[:-1]), axis=0)


ims = 27

Allo = np.array([0, 0.5, 1, 2, 4, 8, 16])


Allo1 = np.array([8, 16, 32])


for k2ii in Allo1:
    oripixel = 4
    # oripixel = 0
    for k2i in Allo:
        noipixel = 0

        print(oripixel)
        print(noipixel)
        for numk in range(1, imgsize):
            nn = 0
            nnn = 0
            mm = 0

            folder1 = path
            folder2 = path
            folder3 = path

            if not os.path.exists(folder1):
                os.makedirs(folder1)
            if not os.path.exists(folder2):
                os.makedirs(folder2)
            if not os.path.exists(folder3):
                os.makedirs(folder3)

            m12menmory = [[0, 0, 0], [0, 0, 0]]
            a = np.zeros((ims, ims, ims))
            b = np.zeros((ims, ims, ims))
            c = np.zeros((ims, ims, ims))
            m12menmory = np.array(m12menmory)
            while nn < oripixel:    # random-dot generate ------ object pixel
                m1 = np.random.randint(3, ims-3)
                m2 = np.random.randint(3, ims-3)
                m3 = np.random.randint(3, ims-3)

                kk = [m1, m2, m3]
                k01 = a[m1-1, m2-1, m3]
                k02 = a[m1-1, m2, m3]
                k03 = a[m1-1, m2+1, m3]
                k04 = a[m1, m2-1, m3]
                k05 = a[m1, m2, m3]
                k06 = a[m1, m2+1, m3]
                k07 = a[m1+1, m2-1, m3]
                k08 = a[m1+1, m2, m3]
                k09 = a[m1+1, m2+1, m3]

                k11 = a[m1-1, m2-1, m3-1]
                k12 = a[m1-1, m2, m3-1]
                k13 = a[m1-1, m2+1, m3-1]
                k14 = a[m1, m2-1, m3-1]
                k15 = a[m1, m2, m3-1]
                k16 = a[m1, m2+1, m3-1]
                k17 = a[m1+1, m2-1, m3-1]
                k18 = a[m1+1, m2, m3-1]
                k19 = a[m1+1, m2+1, m3-1]

                k21 = a[m1-1, m2-1, m3+1]
                k22 = a[m1-1, m2, m3+1]
                k23 = a[m1-1, m2+1, m3+1]
                k24 = a[m1, m2-1, m3+1]
                k25 = a[m1, m2, m3+1]
                k26 = a[m1, m2+1, m3+1]
                k27 = a[m1+1, m2-1, m3+1]
                k28 = a[m1+1, m2, m3+1]
                k29 = a[m1+1, m2+1, m3+1]

                judge = k01 + k02 + k03 + k04 + k05 + k06 + k07 + k08 + k09 + k11 + k12 + k13 + k14 + \
                    k15 + k16 + k17 + k18 + k19 + k21 + k22 + \
                    k23 + k24 + k25 + k26 + k27 + k28 + k29

                if k05 > 0:
                    nn = nn
                else:
                    nn = nn + 1
                    m12menmory = np.row_stack((m12menmory, kk))
                    a[m1][m2][m3] = 1
            aaa = a
            while nnn < noipixel:  # random-dot generate ------ noise
                m1 = np.random.randint(3, ims-3)
                m2 = np.random.randint(3, ims-3)
                m3 = np.random.randint(3, ims-3)
                kk = [m1, m2, m3]

                k10 = b[m1, m2, m3]
                judge = k10
                if judge > 0:
                    nnn = nnn
                else:
                    nnn = nnn + 1
                    m12menmory = np.row_stack((m12menmory, kk))
                    if b[m1][m2][m3] == 1:
                        b[m1][m2][m3] = 0
                    else:
                        b[m1][m2][m3] = 1
            c = a + b

            Matran = np.random.randint(0, 8)
            d = np.zeros((27, 27, 27))

            am1 = np.random.randint(-1, 2)
            am2 = np.random.randint(-1, 2)
            am3 = np.random.randint(-1, 2)

            while am1 == 0 & am2 == 0 & am3 == 0:
                am1 = np.random.randint(-1, 2)
                am2 = np.random.randint(-1, 2)
                am3 = np.random.randint(-1, 2)

            for numk1 in range(0, ims):
                # print(numk1)
                for numk2 in range(0, ims):
                    # print(numk2)
                    for numk3 in range(0, ims):
                        # print([numk1, numk2, numk3])
                        if a[numk1, numk2, numk3] == 1:
                            d[numk1 + am1, numk2 + am2, numk3 + am3] = 1
                        else:
                            pass
            d = d + b

            OD = (am1, am2, am3)
            ODD = (am1 + 1)+3*(am2 + 1)+9*(am3 + 1)

            OD = np.zeros(27)

            OD[ODD] = 1



            np.save(file1, arr=c)
            np.save(file2, arr=d)
            np.save(file3, arr=OD)


