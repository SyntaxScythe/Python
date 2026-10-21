a1 = (1, 2, 3)
b2 = (4, 5, 6)
result = map(lambda x, y: x + y, a1, b2)
print("addition of 2 lists")
print(list(result))

c3 = [1, 2, 3, 4, 5]
def sq(n):
    return n*n
square = list(map(sq, c3))
print("square of number in list")
print(square)