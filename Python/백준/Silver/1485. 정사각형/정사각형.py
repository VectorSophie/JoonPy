def dist_sq(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def is_square(points):
    dists = []
    for i in range(4):
        for j in range(i+1, 4):
            dists.append(dist_sq(points[i], points[j]))
    dists.sort()
    return dists[0] > 0 and dists[0] == dists[1] == dists[2] == dists[3] and dists[4] == dists[5]

T = int(input())
for _ in range(T):
    points = [list(map(int, input().split())) for _ in range(4)]
    print(1 if is_square(points) else 0)