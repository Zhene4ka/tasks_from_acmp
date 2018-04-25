s = None
m = None
with open('input.txt', 'r') as input_file:
    n = int(input_file.readline())
    arr = list(map(int, input_file.readline().split(' ')))
    s = str(sum([i for i in arr if i > 0]))
    print(s)
    min_elem_position = arr.index(min(arr))
    max_elem_position = arr.index(max(arr))
    m = arr[min_elem_position:max_elem_position + 1]

