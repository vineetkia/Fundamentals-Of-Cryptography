import numpy as np

RESULT=""

a=[[6,24,1],[13,16,10],[20,17,15]] # KEY=GYBNQKURP
b=[0,2,19] # PlainText=ACT
c=[0,0,0] # ENCRYPT CIPHER MATRIX

for i in range(3):
    c[i]=a[i][0]*b[0]+a[i][1]*b[1]+a[i][2]*b[2]
for i in range(3):
    c[i]%=26
    RESULT+=chr(65 + c[i])
print(RESULT)
