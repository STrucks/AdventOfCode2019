
def part1_and_2():
    start = 264360
    end = 746325

    possible_numbers1 = []
    possible_numbers2 = []
    for number in range(start, end):
        number_string = str(number)
        digits = [int(n) for n in number_string]

        # check if the digits are increasing and if there is a pair:
        increasing_flag = True
        pair_flag = False
        for index in range(len(digits)-1):
            if digits[index] > digits[index+1]:
                increasing_flag = False
            if digits[index] == digits[index+1]:
                pair_flag = True
        if increasing_flag is False or pair_flag is False:
            continue
        else:
            possible_numbers1.append(number)
            # check if the number meets the part 2 extra criteria:
            for digit in range(10):
                if number_string.count(str(digit)) == 2:
                    possible_numbers2.append(number)
                    print(number)


    print("part 1:", len(possible_numbers1))
    print("part 2:", len(set(possible_numbers2)))

part1_and_2()