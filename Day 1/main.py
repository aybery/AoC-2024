def part_one(left_list, right_list):
    distances = []

    left_list.sort()
    right_list.sort()

    for i in range(len(left_list)):
        if left_list[i] > right_list[i]:
            distances.append(left_list[i]-right_list[i])
        else:
            distances.append(right_list[i]-left_list[i])

    print(sum(distances))


def part_two(left_list, right_list):
    similarity = 0

    for i in left_list:
        num_times = right_list.count(i)
        similarity += i * num_times

    print(similarity)


if __name__ == '__main__':
    f = open("input", "r")
    data = f.readlines()
    f.close()

    left_list = []
    right_list = []

    for index in range(len(data)):
        left_list.append(int(data[index][0:5]))
        right_list.append(int(data[index][8:13]))

    part_one(left_list, right_list)
    part_two(left_list, right_list)

