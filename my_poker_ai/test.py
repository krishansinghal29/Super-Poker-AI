import random
"""
def myfun(x):
    x[0]=300
    y=x
    y[0]=400

x=[200]
myfun(x)
y=x
y[0]=500
print(x)
"""
"""
a=[5,0,1,2,3,4,5]
#print(list(map(lambda x:0,a)))
a.sort()
print(a)
dic={}
dic[1]=[[7]*5]
#b= [ a[:] for i in range(5)]
#b[0][0] =1
b=[7]*5
dic[1].append(b)
dic[1][0]=[e/2 for e in dic[1][0]]
print(dic[1])
#print(b)
_value=[1]*5
_value[2]=None
value =3 
dic[1][0]=[(e+_value[i]-value if _value[i]!=None else e) for i,e in enumerate(dic[1][0])]
print(dic[1][0])

strategyI=[1,0,.2,0]
print(sum(strategyI))
ans=0
for i in range(100):
    temp =random.choices(range(len(strategyI)), strategyI)[0]
    #print(temp)
    if temp==0:
        ans+=1
print(ans,'yoyo')

print([True,False,True].count(True))
x=0
#assert x==1,"olaalaa"
if x==1:
    raise AssertionError ("olaalaa")

print("check")
raiseSizes=[1,2,3]
for e in raiseSizes:
    print(e)
    raiseSizes.pop(0)
print(raiseSizes)

pbetCurrentRound=[0, 3683.3333333333335, 0, 3683.333333333333, 1133.3333333333333, 0]
pFolded=[True, False, True, False, True, True]
pAllin= [False, False, False, False, False, False]
def ischanceNode():
    bet=None
    maxbet=max(pbetCurrentRound)
    if maxbet==0:
        if 1!=5:
            return False
        else:
            return True

    for i,e in enumerate(pbetCurrentRound):
        if pFolded[i]!=True and pAllin[i]!=True:
            if bet!=None:
                print(bet,e)
                if abs(bet-e)>.1:
                    return False
            else:
                bet=e
    return True
print(ischanceNode())
"""
d={1:0}
def discountRegrets(a,b):
    print("check")
    d[1]=0
    return 1
treeMap={1:0,2:0}
print(treeMap.keys())
list(map(lambda key : discountRegrets(key,1), treeMap.keys()))
print(d[1])