'''list comprehenion.........input version
x=[,2,3,4,5]
for i in range(11):
    print(i,end=' ')
    '''
#step by step input of 1c
num=[int(input(f"Enter a number:{i+1}:"))for i in range(10)]
print(num)