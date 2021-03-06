import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

def faktorial(n):
   if n == 1:
       return n
   else:
       return n*faktorial(n-1)

factor = 3
szint = 2
beallitas = szint**factor
ismetles = 2
meres = 2


# Faktorok alsó és felső szintjei természetes mértékben

x_also_hullam = []
x_felso_hullam = []
for i in range(1,factor+1):
    print("x",i,"a: ",end='',sep="")
    also_hullam = int(input())
    x_also_hullam.append(also_hullam)
    print("x",i,"f: ",end='',sep="")
    felso_hullam = int(input())
    x_felso_hullam.append(felso_hullam)

# print("x_also_hullam:",len(x_also_hullam),len(x_felso_hullam))



# Faktorok alapszintjei

x_also = []
for i in range(factor):
    x_also_elem = (x_also_hullam[i]+x_felso_hullam[i])/2
    x_also.append(x_also_elem)

# print("x_also:", len(x_also))



# Variációs intervallumok

for i in range(len(x_also_hullam)):
    x_intervallum = (np.subtract(x_felso_hullam,x_also_hullam))/2
    
# print("intervall:",len(x_intervallum))



# Faktorok alsó és felső szintjeinek transzformált értékei

x_transzformalt = []
for i in range(factor):
    x_also_transzformalt = (x_also_hullam[i]-x_also[i])/x_intervallum[i]
    x_felso_transzformalt = (x_felso_hullam[i]-x_also[i])/x_intervallum[i]
    x_transzformalt.append(x_also_transzformalt)
    x_transzformalt.append(x_felso_transzformalt)

# print(x_transzformalt)


# X értékek táblázat [-1, 1]

if (factor == 1):
    x_elojeles_0 = np.array([1,1])
    x_elojeles_1 = np.array([-1,1])
    x_elojeles = [x_elojeles_0,x_elojeles_1]
elif (factor == 2):
    x_elojeles_0 = np.array([1,1,1,1])
    x_elojeles_1 = np.array([-1,1,-1,1])
    x_elojeles_2 = np.array([-1,-1,1,1])
    x_elojeles = [x_elojeles_0,x_elojeles_1,x_elojeles_2,
                    x_elojeles_1*x_elojeles_2]
elif (factor == 3):
    x_elojeles_0 = np.array([1,1,1,1,1,1,1,1])
    x_elojeles_1 = np.array([-1,1,-1,1,-1,1,-1,1])
    x_elojeles_2 = np.array([-1,-1,1,1,-1,-1,1,1])
    x_elojeles_3 = np.array([-1,-1,-1,-1,1,1,1,1])
    x_elojeles = [x_elojeles_0,x_elojeles_1,x_elojeles_2,x_elojeles_3,
                    x_elojeles_1*x_elojeles_2,x_elojeles_2*x_elojeles_3,x_elojeles_1*x_elojeles_3,
                        x_elojeles_1*x_elojeles_2*x_elojeles_3]
elif (factor == 4):
    x_elojeles_0 = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    x_elojeles_1 = np.array([-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1])
    x_elojeles_2 = np.array([-1,-1,1,1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,1])
    x_elojeles_3 = np.array([-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,1,1,1])
    x_elojeles_4 = np.array([-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1])
    x_elojeles = [x_elojeles_0,x_elojeles_1,x_elojeles_2,x_elojeles_3,x_elojeles_4,
                    x_elojeles_1*x_elojeles_2,x_elojeles_1*x_elojeles_3,x_elojeles_1*x_elojeles_4,
                        x_elojeles_2*x_elojeles_2,x_elojeles_2*x_elojeles_4,x_elojeles_3*x_elojeles_4,
                        x_elojeles_1*x_elojeles_2*x_elojeles_3,x_elojeles_1*x_elojeles_2*x_elojeles_4,
                        x_elojeles_1*x_elojeles_2*x_elojeles_4,x_elojeles_2*x_elojeles_3*x_elojeles_4,
                            x_elojeles_1*x_elojeles_2*x_elojeles_3*x_elojeles_4]
    
    

# print(x_elojeles)



# Az első sorozat mért eredményei

y_k = []
for i in range(ismetles): # factor
    for j in range(2**factor):
        print("y_k",i+1,"(x",j+1,"): ",end='',sep="")
        y_k.append(float(input()))

y_k_sum = []
for i in range(2**factor):
    y_k_sum.append((y_k[i]+y_k[i+(ismetles*factor)])/2)

print(y_k_sum)



# b értékek számítása

b = []
# b.append(sum(y_k_sum)/beallitas)
for i in range(len(y_k_sum)):
    j = np.round(sum(np.multiply(x_elojeles[i],y_k_sum)/beallitas),3)
    b.append(j)

print(b)



# Transzformált koordináta rendszerben a keresett polinom

if (factor == 4):
    print()
elif (factor == 3):
    print("y = b0 + b1 * x1 + b2 * x2 + b12 * x12 + b23 * x23 + b13 * x13 + b123 * x123")
elif (factor == 2):
    print("y = b0 + b1 * x1 + b2 * x2 + b12 * x12")
elif (factor == 1):
    print("y = b0 + b1 * x1")
