n = int(input('Enter the number of elements : '))
arr = []
even, odd = 0, 0
for i in range(0, n):
    arr.append(int(input(f'enter the element {i+1} : ')))
    if arr[i]%2==0:
        even += 1
    else: 
        odd+=1
print(f"Even = {even}, Odd = {odd}")