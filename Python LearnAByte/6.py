n = int(input('Enter the number of elements : '))
arr = []
even = []
for i in range(0, n):
    arr.append(int(input(f'enter the element {i+1} : ')))
    if arr[i]%2==0:
        even.append(arr[i])
print(even)