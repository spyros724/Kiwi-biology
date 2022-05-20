import math
from scipy.stats import t
array = []
z = []
var = []
file_in = open("matrix1.txt", "r")
for y in file_in.read().split():
    array.append(float(y))

i=0
for x in array:
    if i%2==0:
        z.append(array[i]-array[i+1])
    i=i+1

sumz=0.0
for x in z:
    sumz=sumz+x
zbar=sumz/20.0

j=0
for x in z:
    var.append(pow(x-zbar, 2))

varsum=0.0
for x in var:
    varsum=varsum+x
varz=varsum/20.0

T=zbar/math.sqrt(varz/20)

if ((t.cdf(x=T, df=19))<T):
    print("The consumption of kiwi helps reduce the level of bad cholesterol in the human body.")
if ((t.cdf(x=T, df=19))>T):
    print("The consumption of kiwi does not help reduce the level of bad cholesterol in the human body.")
