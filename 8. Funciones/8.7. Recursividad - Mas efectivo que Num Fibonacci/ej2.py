""" Del 1 al 10, te tiene que dar n! = n x (n-1)!:
1 -> 1
2 -> 2
3 -> 6
4 -> 24
5 -> 120
6 -> 720
7 -> 5040
8 -> 40320
9 -> 362880 """
def message(b):
    if b<1:
        return None
    if b<2:
        return 1
    return b*message(b-1)
for b in range(1,10):
    print(b,"->",message(b))