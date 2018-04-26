num = None

with open('input.txt', 'r') as input_file:
    num = int(input_file.readline())

with open('output.txt', 'w') as output_file:
    count = abs(num)
    sum_for_positive_numbers = sum([i for i in range(count + 1)])
    if num < 0:
        output_file.write(str(int('-' + str(sum_for_positive_numbers)) + 1))
    else:
        output_file.write(str(sum_for_positive_numbers))