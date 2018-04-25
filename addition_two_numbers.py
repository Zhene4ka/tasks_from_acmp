a = None
b = None
with open('input.txt', 'r') as input_file:
    a, b = input_file.readline().split(' ')
with open('output.txt', 'w') as output_file:
    output_file.write(str(int(a) + int(b)))
