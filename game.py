k = None
with open('input.txt', 'r') as input_file:
    k = input_file.readline()

with open('output.txt', 'w') as output_file:
    output_file.write(k + '9' + str(9 - int(k)))