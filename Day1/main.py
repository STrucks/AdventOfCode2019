from util import load_txt_data
import queue


def part1():
    data = map(int, load_txt_data("Day1/part1_data.txt"))
    _sum = 0
    for module_weight in data:
        _sum += int(module_weight/3) - 2
    print(_sum)


def part2():
    data = map(int, load_txt_data("Day1/part1_data.txt"))
    # we will store the data in a queue (fifo)
    data_queue = queue.Queue()
    [data_queue.put(weight) for weight in data]
    _sum = 0
    while not data_queue.empty():
        module_weight = data_queue.get()
        amount_fuel = int(module_weight / 3) - 2
        if amount_fuel > 0:
            # if the fuel is above zero, we append it to the end
            _sum += amount_fuel
            data_queue.put(amount_fuel)
    print(_sum)

part2()