from util import load_txt_data


class OpCodeReader:

    def __init__(self, opcode, input_noun=12, input_verb=2):
        self.opcode = opcode
        self.opcode[1] = input_noun
        self.opcode[2] = input_verb
        self.current_index = 0

    def read_next(self):
        """
        :return: If the op code is finished
        """
        if self.opcode[self.current_index] == 99:
            # stop the program:
            return True
        else:
            [method, source1, source2, destination] = self.opcode[self.current_index:self.current_index+4]
            # overwrite the opcode:
            if method == 1:
                self.opcode[destination] = self.opcode[source1] + self.opcode[source2]
            elif method == 2:
                self.opcode[destination] = self.opcode[source1] * self.opcode[source2]
            else:
                print("unkown method %d" % method)
            self.current_index += 4
            return False

def part1():
    data = list(map(int, load_txt_data("Day2/part1_data.txt")[0].split(",")))
    reader = OpCodeReader(data)
    while reader.read_next() is False:
        print("reading...")
    print("done!")
    print(reader.opcode)


def __start_reader(opcode, noun, verb):
    reader = OpCodeReader(opcode, noun, verb)
    try:
        while reader.read_next() is False:
            pass
        if reader.opcode[0] == 19690720:
            return "--------------> Yaaaay, found a solution at noun=%d and verb=%d" % (noun, verb)
        else:
            return "No solution for noun=%d and verb=%d" % (noun, verb)
    except:
        return "Error"

def part2():
    from copy import deepcopy
    data = list(map(int, load_txt_data("Day2/part1_data.txt")[0].split(",")))
    inputs = [(deepcopy(data), i, j) for i in range(100) for j in range(100)]
    from multiprocessing.dummy import Pool as ThreadPool
    pool = ThreadPool(4)
    results = pool.starmap(__start_reader, inputs)
    print("\n".join(results))

part2()
