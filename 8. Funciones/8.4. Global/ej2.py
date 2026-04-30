def variable():
    global var
    var=2
    return var
var=1
variable()
print(var)