# Noah Dagne
# INST326
x = [1, 2, 3, 4, 5]
y = [4, 5, 6, 7]
def list_intersection(x, y):
    for vals in x:
        for vals2 in y:
            if vals == vals2:
                print(vals)
    return vals

list_intersection(x, y)
