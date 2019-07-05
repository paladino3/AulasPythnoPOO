print('Test while')

"""
total = 0

while total <= 100:
    print('%d loop interaction\n' %total)
    total = total + 1
print('End')
"""

fatorial_numero= int(input('Enter whit number: '))

if fatorial_numero > 0:
    passo = fatorial_numero
    total = fatorial_numero
    while passo > 1:
        passo = passo -1
        total = total * passo
    print('The factorial of %d is %d' % (fatorial_numero,total))
elif fatorial_numero == 0:
    print('The factorial of 0 is 1 ')
else:
    print('Not exists fatorial of negative numbers')