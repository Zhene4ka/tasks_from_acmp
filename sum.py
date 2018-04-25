num = None
with open('input.txt', 'r') as input_file:
    num = int(input_file.readline())

with open('output.txt', 'w') as output_file:
    output_file.write(str(sum([i for i in range(num+1)])))