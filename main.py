import math
import sys
from realGradientANFIS import realGradient
from stohasticANFIS import stohastic
xy=[]
f=[]

def z(x,y):
    return (math.pow(x-1,2)+math.pow(y+2,2)-5*x*y+3)*math.pow(math.cos(x/5),2)
for x in range(-4,5):
    for y in range(-4,5):
        xy.append((x,y))
        f.append(z(x,y))
m=int(sys.argv[1])
max_iter=1000000
max_err=10
eta=0.2
stohasticResult=stohastic(xy,f,m,max_iter,max_err,eta)
realResult=realGradient(xy,f,m,max_iter,max_err,eta)


