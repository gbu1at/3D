from Game.POLYGON.Polygon import Polygon

polygons = []
with open("ROOT/file.txt", 'r') as file:
    for line in file.readlines():
        data = eval(line)
        polygons.append(Polygon(polygon=data[:-1], parameters=data[-1]))

file = open("ROOT/file.txt", 'w')
file.close()


def write(data):
    file = open("ROOT/file.txt", "a")
    file.write(str(data) + '\n')
    file.close()
