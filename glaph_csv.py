import numpy as np
import matplotlib.pyplot as plt

#x,y = np.loadtxt('test01.csv', delimiter=',', unpack=True)
#array = np.genfromtxt("test01.csv", dtype=None, delimiter=",", unpack=True)
array = np.genfromtxt("test01.csv", dtype=[("a",int),("b","S2"),("c",int)], delimiter=",")

#print array

array_trans = zip(*array) #tenchi

#print array[0]

#label  = ["MA", "MB", "MC", "MD", "ME"]
#left   = np.array([1,2])
#height = np.array([100, 200])

lista = list()
colorlist = list()
oklist    = list()
nglist    = list()
#lista = []

TARGETF = 300

for i in array_trans[2]:
    #array_trans[3].append = 300
    lista.append(i)
    if i <= TARGETF:
        colorlist.append("b")
        oklist.append(i)
        nglist.append(0)
    else:
        colorlist.append("r")
        oklist.append(TARGETF)
        nglist.append(i-TARGETF)
            
plt.bar(array_trans[0], oklist, tick_label=array_trans[1], align="center", color="royalblue")
plt.bar(array_trans[0], nglist, tick_label=array_trans[1], align="center", color="tomato", bottom=oklist)
plt.title("Title")
plt.grid(True)

plt.show()
