max_count_of_coins = None
with open('input.txt', 'r') as input_file:
    max_count_of_coins = max((input_file.readline().split(' ')))

with open('output.txt', 'w') as output_file:
    output_file.write(str(max_count_of_coins))