with open("ex1.txt") as file:
    house_count = int(file.readline().rstrip().split(" ")[0]) # 12
    houses = [list(map(int, file.readline().rstrip().split(" "))) for _ in range(house_count)]
    windmills = [list(map(int, line.rstrip().split(" "))) for line in file]

    """
    houses = []
    windmills = []

    for i, line in enumerate(file):
        if i < house_count:
            houses.append(
                list(map(int, line.rstrip().split(" ")))
            )

        else:
            windmills.append(
                list(map(int, line.rstrip().split(" ")))
            )
    """
    
print(houses)
print(windmills)

def pyth(a, b, _a, _b):
    return ((a-_a)**2 + (b-_b)**2)**(1/2)


for i, windmill in enumerate(windmills):
    distances = [pyth(*house, *windmill) for house in houses]
    print(f"{i}: {min(distances)/10}")
