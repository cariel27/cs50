l2 = ["3","5","9","12","25"]
l2 = list(map(int,l2))
y = l2[0]+1
print("l2[0]+1 = " + str(y))

# ANOTHER EXAMPLE WITH square function


def sq(a):
    return a*a


l3 = [3, 5, 7, 2, 9]
l4 = list(map(sq,l3))
print("list(map(sq,l3)) = " + str(l4))

# Get the square and cube o number from 0,8


def sq(a):
    return a * a


def cube(a):
    return a*a*a

func = [sq, cube]

for i in range(8):
    res = list(map(lambda x: x(i), func))
    print(res)



