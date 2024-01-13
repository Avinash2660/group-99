def maxpair():
 n=6
 print(n)
 a=[8,4,5,10,6,9]
 mp=[-1,-1]
 mpp=float('-inf')
 for i in range(n):
  for j in range(i+1,n):
    if (a[i]+a[j]==18 and a[i]>a[j]):
      pro=a[i]*a[j]
      if (pro>mpp):
        mpp=pro
        mp=[a[i],a[j]]
 print(mp)