n = int(input('Enter the number of elements : '))
arr = []
for i in range(0, n):
    arr.append(int(input(f'enter the element {i+1} : ')))
    
pos1 = int(input("Enter the first position : "))
pos2 = int(input("Enter the second position : "))

arr[pos1-1], arr[pos2-1] = arr[pos2-1], arr[pos1-1]
print(arr)