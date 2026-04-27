my_list = [127, 23, 211, 2225, 51, 19, 37, 125, 103]
num_mayor=my_list[0]

for i in my_list:
    if i>num_mayor:
        num_mayor=i
print("-"+str(num_mayor))