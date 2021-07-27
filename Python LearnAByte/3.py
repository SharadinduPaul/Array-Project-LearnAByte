n = int(input('Enter the number of elements : '))
arr = []
for i in range(0, n):
    arr.append(int(input(f'enter the element {i+1} : ')))
x = int(input('Enter the number X :'))

count = 0
for i in range(0, n):
    if arr[i] == x: 
        count += 1
print(f" {x} appeared {count} times in this array")