def solve(numheads, numlegs):
    for x in range(1, numheads + 1):
        for y in range (1, numheads + 1):
            if x + y == numheads and (2 * x) + (4 * y) == numlegs:
                print (x, y)
                break
            else:
                continue
solve(35, 94)

            