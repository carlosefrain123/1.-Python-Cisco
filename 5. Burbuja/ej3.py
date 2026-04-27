my_list = [851, 50, 116, 422, 84]
swapped=True
while swapped:
    swapped=False
    for i in range(len(my_list)-1):
        if(my_list[i]>my_list[i+1]):
            swapped=True
            my_list[i],my_list[i+1]=my_list[i+1],my_list[i]
print(my_list)