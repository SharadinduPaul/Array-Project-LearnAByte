n = int(input('Enter the number of elements : '))
arr = []
mul = 1
for i in range(0, n):
    arr.append(int(input(f'enter the element {i+1} : ')))
    mul *= arr[i]

print(mul)