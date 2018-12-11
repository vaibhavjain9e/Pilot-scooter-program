class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


def return_exploitable_list_by_element(exploitable_list, node):
    new_exploitable_list = []
    for i in range(0, len(exploitable_list)):
        if not (exploitable_list[i][1] == node[1] or exploitable_list[i][2] == node[2] or (abs(exploitable_list[i][1] - node[1]) == abs(exploitable_list[i][2] - node[2]))):
            new_exploitable_list.append(exploitable_list[i])
    return new_exploitable_list


def next_valid_position_index(main_list, index_list, start_index):
    final_list = main_list

    for i in range(0, len(index_list)):
        final_list = return_exploitable_list_by_element(final_list, main_list[index_list[i]])

    if not final_list:
        return -1
    else:
        for i in range(0, len(final_list)):
            if final_list[i][3] >= start_index:
                return final_list[i][3]
        return -1


def compute_max(main_list, n, p):
    x = 0
    index = -1
    count = 0
    index_list = Stack()
    maximum_activity_point = 0
    flag = 0
    flag2 = 0
    main_flag = 0

    while x < n*n and not (maximum_activity_point >= main_list[x][0]*p and main_flag == 1):
        if index == n*n:
            index_list.pop()
            index = index_list.peek()

        index = next_valid_position_index(main_list, index_list.items, index + 1)

        if index == -1:
            index = index_list.peek()
            index_list.pop()
            count -= 1
            flag2 = 1
        else:
            index_list.push(index)
            count += 1

            if count == p:
                flag = 1
                main_flag = 1

                sum_list = 0
                for i in index_list.items:
                    sum_list += main_list[i][0]

                if maximum_activity_point < sum_list:
                    maximum_activity_point = sum_list

                while index_list.size() > 1:
                    index_list.pop()

                index = index_list.peek()

        if (x == index and flag == 1) or (x == index and flag2 == 1):
            index = x
            x += 1
            if index_list.size() > 0:
                index_list.pop()
            count = 0
            flag = 0
            flag2 = 0

    return maximum_activity_point


def sort_list(problem_space, n, p):
    total_elements = n*n
    sorted_list = [0] * total_elements
    for i in range(total_elements):
        sorted_list[i] = [0] * 4

    index = 0
    for i in range(n):
        for j in range(n):
            sorted_list[index][0] = int(problem_space[i][j])
            sorted_list[index][1] = i
            sorted_list[index][2] = j
            index += 1
    sorted_list.sort(reverse=True)

    for i in range(0, len(sorted_list)):
        sorted_list[i][3] = i

    output = compute_max(sorted_list, n, p)
    with open('output.txt', 'w') as outputFile:
        outputFile.write(str(output))


def put_data_into_list(input_string):
    input_string = input_string.replace(' ', '')
    input_list = input_string.split("\n")
    n = int(input_list[0])
    p = int(input_list[1])
    s = int(input_list[2])

    problem_space = [[0 for x in range(n)] for y in range(n)]

    for item in input_list[3:]:
        if item:
            location = item.split(",")
            row = int(location[0])
            column = int(location[1])
            problem_space[row][column] += 1

    sort_list(problem_space, n, p)


def main():
    input_file = open("input.txt", "r")
    input_string = input_file.read()
    put_data_into_list(input_string)


main()