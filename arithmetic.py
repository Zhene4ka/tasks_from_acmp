v = None
with open('input.txt', 'r') as input_file:
    a, b, c = input_file.readline().split(' ')
    if int(a) * int(b) == int(c):
        v = 'YES'
    else:
        v = 'NO'
with open('output.txt', 'w') as output_file:
    output_file.write(v)