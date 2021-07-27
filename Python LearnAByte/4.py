n = int(input('Enter the number of elements : '))
arr = []
sum = 0
for i in range(0, n):
    arr.append(int(input(f'enter the element {i+1} : ')))
    sum += arr[i]

print(f"Sum : {sum} \nAverage : {sum/n}")