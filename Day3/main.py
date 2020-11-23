from util import load_txt_data


def part1():
    wire_directions1 = load_txt_data("Day3/part1_data1.txt")[0].split(",")
    wire_directions2 = load_txt_data("Day3/part1_data2.txt")[0].split(",")

    # we save all wire positions and perform set operations afterwards:
    wire1_positions = [(0, 0)]
    wire2_positions = [(0, 0)]

    for wire_direction in wire_directions1:
        direction, amount = wire_direction[0], int(wire_direction[1:])
        for i in range(amount):
            if direction == "U":
                wire1_positions.append((wire1_positions[-1][0], wire1_positions[-1][1]+1))
            elif direction == "D":
                wire1_positions.append((wire1_positions[-1][0], wire1_positions[-1][1]-1))
            elif direction == "R":
                wire1_positions.append((wire1_positions[-1][0]+1, wire1_positions[-1][1]))
            elif direction == "L":
                wire1_positions.append((wire1_positions[-1][0]-1, wire1_positions[-1][1]))

    for wire_direction in wire_directions2:
        direction, amount = wire_direction[0], int(wire_direction[1:])
        for i in range(amount):
            if direction == "U":
                wire2_positions.append((wire2_positions[-1][0], wire2_positions[-1][1] + 1))
            elif direction == "D":
                wire2_positions.append((wire2_positions[-1][0], wire2_positions[-1][1] - 1))
            elif direction == "R":
                wire2_positions.append((wire2_positions[-1][0] + 1, wire2_positions[-1][1]))
            elif direction == "L":
                wire2_positions.append((wire2_positions[-1][0] - 1, wire2_positions[-1][1]))

    wire1_positions = set(wire1_positions)
    wire2_positions = set(wire2_positions)

    intersections = wire1_positions.intersection(wire2_positions)

    distances = {}
    for intersection in intersections:
        distances[intersection] = abs(intersection[0]) + abs(intersection[1])

    print(list(sorted(distances, key=lambda k: distances[k])))
    

#part1()

def part2():
    data = load_txt_data("Day3/part2.txt")
    wire_directions1 = data[0].split(",")
    wire_directions2 = data[1].split(",")

    # first, make a list of all coordinates of wire 1:
    wire1_coords = [(0, 0)]
    for wire_direction in wire_directions1:
        direction, amount = wire_direction[0], int(wire_direction[1:])
        for i in range(amount):
            if direction == "U":
                wire1_coords.append((wire1_coords[-1][0], wire1_coords[-1][1] + 1))
            elif direction == "D":
                wire1_coords.append((wire1_coords[-1][0], wire1_coords[-1][1] - 1))
            elif direction == "R":
                wire1_coords.append((wire1_coords[-1][0] + 1, wire1_coords[-1][1]))
            elif direction == "L":
                wire1_coords.append((wire1_coords[-1][0] - 1, wire1_coords[-1][1]))

    # next, we make the same for the wire2, but check if an intersection happend:
    wire2_coords = [(0, 0)]
    for wire_direction in wire_directions2:
        direction, amount = wire_direction[0], int(wire_direction[1:])
        for i in range(amount):
            if direction == "U":
                wire2_coords.append((wire2_coords[-1][0], wire2_coords[-1][1] + 1))
            elif direction == "D":
                wire2_coords.append((wire2_coords[-1][0], wire2_coords[-1][1] - 1))
            elif direction == "R":
                wire2_coords.append((wire2_coords[-1][0] + 1, wire2_coords[-1][1]))
            elif direction == "L":
                wire2_coords.append((wire2_coords[-1][0] - 1, wire2_coords[-1][1]))

            # check if the last coord is in the wire 1:
            if wire2_coords[-1] in wire1_coords:
                # we found the first intersection!
                steps_wire_1 = wire1_coords.index(wire2_coords[-1]) + 1
                steps_wire_2 = len(wire2_coords)
                print("Intersection in", steps_wire_1 + steps_wire_2 - 2, "steps")

part2()


