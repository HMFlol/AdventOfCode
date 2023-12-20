from aocd import get_data
from time import time
from shapely.geometry.polygon import Polygon

data = get_data(day=18, year=2023)
data = open('test.txt').read()
data = [line.split() for line in data.splitlines()]

# Pick's theorem says: A = i + b/2 - 1, where i is the number of interior points and b is the number of exterior points.
# Thus, i = A + b/2 + 1

directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1), '3': (-1, 0), '1': (1, 0), '2': (0, -1), '0': (0, 1)}

# This is my solution. The other functions are from other people. Wanted to see how they worked!
def shoelacePick(colour):
    x, y = 0, 0  # Beginning coordinates
    shoelace_sum = 0  # This will be used to calculate an area using the Shoelace formula
    edge_boundary = 0  # This will keep track of the total distance traveled

    for line in data:
        if colour:
            plans = line[2]  # Get the third element from 'line'.
            dist = int(plans[2:-2], 16)  # Convert a part of 'plans' from hexadecimal to integer.
            direction = plans[-2]  # Get the second last character from 'plans'.
        else:
            direction, dist = line[:2]  # Get the first two elements from 'line'.
            dist = int(dist)  # Convert 'dist' to an integer.

        dirx, diry = directions[direction] # Get the direction coordinates from the 'directions' dictionary.
        x += dirx * dist # Update the coordinates 'x' and 'y' based on the direction and distance.
        y += diry * dist
        shoelace_sum += x * (y + diry * dist) - (x + dirx * dist) * y # Update the 'shoelace_sum' using the Shoelace formula.
        edge_boundary += dist # Update the 'edge_boundary' by adding the distance.

    # Calculate the total using the Shoelace area, path length, and Pick's theorem.
    '''A = (abs(shoelace_sum) // 2) - edge_boundary // 2 + 1
    i = A + edge_boundary
    print(i)'''
    total = (abs(shoelace_sum) >> 1) - (edge_boundary >> 1) + 1 + edge_boundary # Do some fun bitwise operations to divide by 2

    # Return the total.
    return total

def wtf(colour):
    pos = 0
    ans = 1
    for line in data: # copied this block from mine cuz this other one was doing some fuckery with the print statements
        if colour:
            plans = line[2]
            dist = int(plans[2:-2], 16)
            direction = plans[-2]
        else:
            direction, dist = line[:2]
            dist = int(dist)  # convert only the distance to an integer

        dirx, diry = directions[direction]
        pos += diry*dist
        ans += dirx*dist * pos + dist/2

    return int(ans)

def complex(colour):
    dirs = {"R": 1, "D": 1j, "L": -1, "U": -1j}
    dirs2 = {0: "R", 1: "D", 2: "L", 3: "U"}
    trench = [0]
    for line in data:
        if colour:
            temp = line.split(" ")[2]
            dist = int(temp[2:-2], 16)
            dir_ = dirs[dirs2[int(temp[-2])]]
        else:
            dir_ = dirs[line[0]]
            dist = int(line.split(" ")[1])
        trench.append(trench[-1] + dist*dir_)
    
    corners = [(int(p.real), int(p.imag)) for p in trench]
    polygon = Polygon(corners)
    return int(polygon.area + polygon.length/2 + 1)

def hn(colour):
    # More shoelace
    points = [(0,0)]
    
    b = 0

    for line in data:
        if colour:
            _, _, x = line
            x = x[2:-1]
            dr, dc = directions["RDLU"[int(x[-1])]]
            n = int(x[:-1], 16)
        else:
            d, n, _ = line
            dr, dc = directions[d]
            n = int(n)
        b += n
        r, c = points[-1]
        points.append((r + dr*n, c + dc*n))
    # Shoelace area
    A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) // 2
    # Picks theorem to get interior points
    i = A - b // 2 + 1
    return i + b



start_time = time()

# print(f"Total (Part1):", shoelacePick(False))
# print(f"Total (Part2):", shoelacePick(True))

'''print(f"Total (Part1) wtf:", wtf(False))
print(f"Total (Part2) wtf:", wtf(True))'''

'''print(f"Total (Part1) complex:", complex(False))
print(f"Total (Part2) complex:", complex(True))'''

print(f"Total (Part1) hn:", hn(False))
print(f"Total (Part2) hn:", hn(True))

end_time = time()
print(f"Total execution time: {end_time - start_time:.6f} seconds")