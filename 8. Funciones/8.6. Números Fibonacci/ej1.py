""" Al hacer la formula Fibonacci, pues te tiene que dar:
1 -> 1
2 -> 1
3 -> 2
4 -> 3
5 -> 5
6 -> 8
7 -> 13
8 -> 21
9 -> 34 """


def fb(n):
    if n<0:
        return None
    if n<3:
        return 1
    elem1=elem2=1
    sum=0
    for i in range(3,n+1):
        sum=elem1+elem2
        elem1,elem2=elem2,sum
    return sum
for n in range(1,10):
    print(n,"->",fb(n))