# function to give maximum of two
def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y

# function to give max of three
def max_of_three(x, y, z):
    if (x > z and x > y):
            return x
    elif (y > x and y > z):
            return y
    elif (x == y and x > z):
            return x
    else:
        return z

# function to give max in a list and its attribute
def listMax(list):
    demo = list[0]
    for x in list:
        for y in range(0, len(list)):
            if (demo < list[y]):
                demo = list[y]
                pos = y+1
    value = (demo, pos)
    return value