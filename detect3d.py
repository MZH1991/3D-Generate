import numpy as np
import matplotlib.pyplot as plt
import math
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
import os

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
Allo = np.array([0,0.5,1,1.5,2,2.5,3,3.5,4])
 

batch_size = 40
xt = 27
random_va = 0

ims = 27

correct = 0
total = 0

oripixel = 64 #原始像素数量
noipixel = 48 #干扰像素数量

for numk in range(1,2001): 

    total += 1 
    # file1 = 'F:/Data Base/test/learning/rec' + str(oripixel) + str(noipixel) + '/before/' + str(numk) + '.npy'
    # file2 = 'F:/Data Base/test/learning/rec' + str(oripixel) + str(noipixel) + '/after/' + str(numk) + '.npy' 
    # file3 = 'F:/Data Base/test/learning/rec' + str(oripixel) + str(noipixel) + '/label/' + str(numk) + '.npy' 
    file1 = 'F:/Data Base/origin/shiftgenerate' + str(oripixel) + str(noipixel) + '/1/' + str(numk) + '.npy'
    file2 = 'F:/Data Base/origin/shiftgenerate' + str(oripixel) + str(noipixel) + '/2/' + str(numk) + '.npy' 
    file3 = 'F:/Data Base/retina/shiftgenerate' + str(oripixel) + str(noipixel) + '/label/' + str(numk) + '.npy'

    a = np.load(file1)
    b = np.load(file2)
    c = np.load(file3)





    a1 = np.zeros((3,7)) #三行七列
    a2 = np.zeros((3,7)) #三行七列

    OD = np.zeros(27)



    for numk1 in range(0,ims):
        # print(numk1)
        for numk2 in range(0,ims):
            # print(numk2)
               for numk3 in range(0,ims):
                    if a[numk1, numk2, numk3] == 1:
                        a1 = np.zeros((3,7))
                        a2 = np.zeros((3,7))


                        for am1 in range(-1,2):
                            for am2 in range(-1,2):
                                for am3 in range(-1,2):

                                    if b[numk1 + am1, numk2 + am2, numk3 + am3] == 1:   #转化为两张二维图
                                        a1[am2+1,2*am3+3+am1] = 1
                                        a2[am2+1,2*am3+3-am1] = 1
                                    else:
                                        pass
                        # print("a1")
                        # print(a1)
                        # print("a2")
                        # print(a2)
                        # print("OD")
                        # print(OD)
                        # print("C")
                        # print(c)

                        for am2 in range(-1,2):
                            if (a1[am2+1,2] == 1) & (a2[am2+1,4] == 1):
                                am1 = -1
                                am3 = 0

                                ODD = (am1 + 1)+3*(am2 + 1)+9*(am3 + 1)

                                kc = OD[ODD]

                                kc += 1

                                OD[ODD] = kc


                            else:
                                pass

                            if (a1[am2+1,0] == 1) & (a2[am2+1,2] == 1):
                                am1 = -1
                                am3 = -1

                                ODD = (am1 + 1)+3*(am2 + 1)+9*(am3 + 1)

                                kc = OD[ODD]

                                kc += 1

                                OD[ODD] = kc                            
                            else:
                                pass

                            if (a1[am2+1,4] == 1) & (a2[am2+1,6] == 1):
                                am1 = -1
                                am3 = +1

                                ODD = (am1 + 1)+3*(am2 + 1)+9*(am3 + 1)

                                kc = OD[ODD]

                                kc += 1

                                OD[ODD] = kc                            
                            else:
                                pass

                            if (a1[am2+1,3] == 1) & (a2[am2+1,3] == 1):
                                am1 = 0
                                am3 = 0

                                ODD = (am1 + 1)+3*(am2 + 1)+9*(am3 + 1)

                                kc = OD[ODD]

                                kc += 1

                                OD[ODD] = kc                            
                            else:
                                pass

                            if (a1[am2+1,1] == 1) & (a2[am2+1,1] == 1):
                                am1 = 0
                                am3 = -1

                                ODD = (am1 + 1)+3*(am2 + 1)+9*(am3 + 1)

                                kc = OD[ODD]

                                kc += 1

                                OD[ODD] = kc                            
                            else:
                                pass

                            if (a1[am2+1,5] == 1) & (a2[am2+1,5] == 1):
                                am1 = 0
                                am3 = 1

                                ODD = (am1 + 1)+3*(am2 + 1)+9*(am3 + 1)

                                kc = OD[ODD]

                                kc += 1

                                OD[ODD] = kc                            
                            else:
                                pass

                            if (a1[am2+1,4] == 1) & (a2[am2+1,2] == 1):
                                am1 = 1
                                am3 = 0

                                ODD = (am1 + 1)+3*(am2 + 1)+9*(am3 + 1)

                                kc = OD[ODD]

                                kc += 1

                                OD[ODD] = kc                            
                            else:
                                pass

                            if (a1[am2+1,2] == 1) & (a2[am2+1,0] == 1):
                                am1 = 1
                                am3 = -1

                                ODD = (am1 + 1)+3*(am2 + 1)+9*(am3 + 1)

                                kc = OD[ODD]

                                kc += 1

                                OD[ODD] = kc                            
                            else:
                                pass

                            if (a1[am2+1,6] == 1) & (a2[am2+1,4] == 1):
                                am1 = 1
                                am3 = 1

                                ODD = (am1 + 1)+3*(am2 + 1)+9*(am3 + 1)

                                kc = OD[ODD]

                                kc += 1

                                OD[ODD] = kc                            
                            else:
                                pass                                


                    else:
                        pass

    print(OD)
    print(c)
    m = np.argmax(OD)
    n = np.argmax(c)
    print(m)
    print(n)

    if m == n:
        correct += 1
    else:
        pass

print(correct)




