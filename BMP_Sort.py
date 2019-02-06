

def bmp_sort(array):
    max_val = max(array)
    sort_arr = ['x' for x in range(max_val)]
   
    for value in array:
        sort_arr.insert(value, value)

    sort_arr = list(filter(('x').__ne__, sort_arr))

    return sort_arr

inArr = [3, 2, 1, 100]
print('Input Array: ', inArr)
print('Sorted Output: ', bmp_sort(inArr))