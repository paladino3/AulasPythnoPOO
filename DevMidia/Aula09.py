print('Test loop with FOR')
"""
sum = htmlPag

for number in range(10):
    sum = sum + number
print('The sum is',sum)
"""
"""
for x in range(50,100):
    if x == 88:
        break
    print(x)
print('\nBreak in x = ',x)
"""

print('Test FOR -  sum odd numbers')

total = 0

number = int(input('Enter with number: '))

if (number % 2 ) == 0:
    number = number - 1
for i in range(number,0,-2):
    total = total +i
    print('i is ',i)
print('The sum of odd numbers is ',total)
