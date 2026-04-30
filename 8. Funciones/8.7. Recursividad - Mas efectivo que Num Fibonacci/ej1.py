""" Al hacer la formula Fibonacci, pues te tiene que dar del 1 al 10:
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
    return fb(n-1)+fb(n-2)
for n in range(1,10):
    print(n,"->",fb(n))