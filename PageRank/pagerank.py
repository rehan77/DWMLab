import numpy as np
import sys

d=0.85  #damping factor
eps=1.0e-8 #epsilon quadratic error use for convergence

no_of_pages = int(input("Number Of Pages:"))
link = []
for i in range(no_of_pages):
    l = []
    for j in range(no_of_pages):
        try:
            l.append(int(input('page'+ str(i+1) + 'to page ' + str(j+1)+ ':')))
        except:
            print("You are Adding Element More than the No of pages.")
            sys.exit(1)
            
    Link.append(l)
M = np.array(Link)




outboundL = np.zeros((no_of_pages,), dtype=int )

for i in range(0,no_of_pages):
  for j in range(0,no_of_pages):
    if links[i][j]==1:
      outboundL[i] = outboundL[i]+1
      
      
M = np.zeros((no_of_pages,no_of_pages))
for i in range(0,no_of_pages):
  for j in range(0,no_of_pages):
    if links[j][i]==1:
      M[i][j] = 1/outboundL[i]
      
      
      
M = np.matrix(M)
oneColMat = np.matrix(np.ones((no_of_pages,1), dtype=int))

R=np.matrix(np.full((no_of_pages,1),1/N))

while True:
  Rnext = d*np.dot(M,R)+((1-d)/no_of_pages) * oneColMat
  diff = np.subtract(Rnext,R)
  if np.linalg.norm(diff) < eps:
    break;
R = Rnext
