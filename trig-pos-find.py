import math

def LineInter(line1, line2):
    xdiff = [line1[0][0] - line1[1][0], line2[0][0] - line2[1][0]]
    ydiff = [line1[0][1] - line1[1][1], line2[0][1] - line2[1][1]]
    
    det = lambda a, b : a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return None
    
    d = [det(line1[0], line1[1]), det(line2[0], line2[1])]
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div

    return [x, y]

ToLine = lambda point, angle : [point, [point[0] + math.cos(angle), point[1] + math.sin(angle)]]

# Input
points = []
for i in range(2):
    print(f"Point #{i + 1}")
    points.append([])
    queries = ["Please enter the x position: ", "Please enter the y position: ", "Please enter the rotation in degrees: "]
    for query in queries:
        points[i].append(int(input(f"\t{query}")))
    points[i][2] = math.radians(points[i][2])

print(LineInter(ToLine(points[0][0:2], points[0][2]),
                ToLine(points[1][0:2], points[1][2])))
