
"""
texto_string = 'Devimidia\nis\n' + 'a great\ncompany'

print(texto_string)
"""

#print('_'*80)

print('Test format strings')

myInterger = 12345
myFloat =3.14155
myString = 'Devmidia is a great company'

print('Interger ',myInterger)
print('Decimal interger %d' % myInterger)
print('Hexacecimal interger %x' %myInterger)

print('float',myFloat)
print('Default %f' % myFloat)
print('Exponential %e' % myFloat)
print('Right justify (%10d)' % myFloat)
print('Left justify (%-10d)' % myFloat)

print('Force nice digits %.9d' % myInterger)
print('Three digits after decimal in float %.3f' % myFloat)
print('Ten and five characters allowed in strings: ')
print('(%.11s) (%.5s)' % (myString,myString))