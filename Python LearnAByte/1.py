n = int(input('Enter the number of elements : '))
arr = []
for i in range(0, n):
    arr.append(int(input(f'enter the element {i+1} : ')))

arr[0], arr[n-1] = arr[n-1], arr[0]
print(arr)