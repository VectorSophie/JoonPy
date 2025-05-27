tri = [int(input()) for _ in range(3)]
if sum(tri) == 180:
    if tri[0] == tri[1] == tri[2]:
        print("Equilateral")
    elif len(set(tri)) == 2:
        print("Isosceles")
    elif len(set(tri)) == 3:
        print("Scalene")
else:
    print("Error")