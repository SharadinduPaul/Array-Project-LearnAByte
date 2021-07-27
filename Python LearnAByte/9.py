n = int(input('Enter the number of elements : '))
arr = []
positive = []
for i in range(0, n):
    arr.append(int(input(f'enter the element {i+1} : ')))
    if arr[i]>=0:
        positive.append(arr[i])
print(positive)