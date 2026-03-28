import pandas as pd 
import matplotlib.pyplot as plt
import sklearn
from sklearn.preprocessing import StandardScaler
import numpy
from sklearn.decomposition import PCA
X = pd.read_excel("voiture.xlsx", sheet_name=0, header=0, index_col=0)
print(X.shape)
n=X.shape[0]
p=X.shape[1]
print(X)
sc = StandardScaler()
Z = sc.fit_transform(X)
print(Z)
print(numpy.mean(Z,axis=0))
print(numpy.std(Z,axis=0,ddof=0))
acp = PCA(svd_solver='full')
print(acp)
coord = acp.fit_transform(Z)
print(acp.n_components_)
print(acp.explained_variance_)
eigval =((n-1)/n*acp.explained_variance_)
print(eigval)
print(acp.singular_values_**2/n)
print(acp.explained_variance_ratio_)
plt.plot(numpy.arange(1,p+1),eigval)
plt.title("Scree plot")
plt.ylabel("Eigen values")
plt.xlabel("Factor number")
plt.show()

plt.plot(numpy.arange(1,p+1),numpy.cumsum(acp.explained_variance_ratio_))
plt.title("Explained variance vs. # of factors")
plt.ylabel("Cumsum explained variance ratio")
plt.xlabel("Factor number")
plt.show()
fig, axes = plt.subplots(figsize=(12,12))
axes.set_xlim(-6,6) 
axes.set_ylim(-6,6) 

for i in range(n):
    plt.annotate(X.index[i],(coord[i,0],coord[i,1]))

plt.plot([-6,6],[0,0],color='silver',linestyle='-',linewidth=1)
plt.plot([0,0],[-6,6],color='silver',linestyle='-',linewidth=1)
plt.show()
di = numpy.sum(Z**2,axis=1)
print(pd.DataFrame({'ID':X.index,'d_i':di}))
cos2 = coord**2
for j in range(p):
   cos2[:,j] = cos2[:,j]/di
print(pd.DataFrame({'id':X.index,'COS2_1':cos2[:,0],'COS2_2':cos2[:,1]}))
print(numpy.sum(cos2,axis=1))
print(acp.components_)
ctr = coord**2

for j in range(p):
    ctr[:,j] = ctr[:,j] / (n * eigval[j])

print(pd.DataFrame({'id':X.index,
                    'CTR_1':ctr[:,0],
                    'CTR_2':ctr[:,1]}))

print("Somme des contributions par axe :")
print(numpy.sum(ctr,axis=0))
print(acp.components_)
sqrt_eigval = numpy.sqrt(eigval)
corvar = numpy.zeros((p,p))
for k in range(p):
       corvar[:,k] = acp.components_[k,:] * sqrt_eigval[k]
print(corvar)
print(pd.DataFrame({'id':X.columns,'COR_1':corvar[:,0],'COR_2':corvar[:,1]}))
fig, axes = plt.subplots(figsize=(8,8))
axes.set_xlim(-1,1)
axes.set_ylim(-1,1)
for j in range(p):
    plt.annotate(X.columns[j],(corvar[j,0],corvar[j,1]))
plt.plot([-1,1],[0,0],color='silver',linestyle='-',linewidth=1)
plt.plot([0,0],[-1,1],color='silver',linestyle='-',linewidth=1)


cercle = plt.Circle((0,0),1,color='blue',fill=False)
axes.add_artist(cercle)
plt.show()

indSupp = pd.read_excel("voiture.xlsx", sheet_name=0, header=0, index_col=0)
print(indSupp)
ZIndSupp = sc.transform(indSupp)
print(ZIndSupp)
coordSupp = acp.transform(ZIndSupp)
print(coordSupp)
fig, axes = plt.subplots(figsize=(12,12))
axes.set_xlim(-6,6)
axes.set_ylim(-6,6)
for i in range(n):
  plt.annotate(X.index[i],(coord[i,0],coord[i,1]))
for i in range(coordSupp.shape[0]):
   plt.annotate(indSupp.index[i],(coordSupp[i,0],coordSupp[i,1]),color='b')
plt.plot([-6,6],[0,0],color='silver',linestyle='-',linewidth=1)
plt.plot([0,0],[-6,6],color='silver',linestyle='-',linewidth=1)
plt.show()