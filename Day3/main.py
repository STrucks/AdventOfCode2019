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
    

part1()