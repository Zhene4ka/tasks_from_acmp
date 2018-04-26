numbers_of_month = None
even_numbers_of_month = None
uneven_numbers_of_month = None
mark = None
with open('input.txt', 'r') as input_file:
    n = input_file.readline()
    numbers_of_month = list(map(int, input_file.readline().split(" ")))
    even_numbers_of_month = list(filter(lambda n: n % 2 == 0, numbers_of_month))
    uneven_numbers_of_month = set(numbers_of_month) - set(even_numbers_of_month)
    if len(uneven_numbers_of_month) < len(even_numbers_of_month):
        mark = 'YES'
    else:
        mark = 'NO'

with open('output.txt', 'w') as output_file:
    output_file.write(str(uneven_numbers_of_month).strip('{}').replace(',','') + '\n' + str(even_numbers_of_month).strip('[]').replace(',','') + '\n' + mark)