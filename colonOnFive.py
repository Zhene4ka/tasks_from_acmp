square_of_a = None
with open('input.txt', 'r') as input_file:
    a = input_file.readline().strip()
    if len(a) == 1:
        square_of_a = str(int(a) ** 2)
    else:
#        square_of_a = str(int(a[0:-1]) * (int(a[0:-1]) + 1)) + '25'
         square_of_a = str((int(a) // 10) * (int(a) // 10 + 1)) + '25'

with open('output.txt', 'w') as output_file:
    output_file.write(square_of_a)