print('Test logical operators ')

"""
if 1 == 1 and 2 == 2:
    print('Condition is true')
else:
    print('Condition is false')

if 1 == 11 and 2 == 3:
    print('New condition is true')
else:
    print('New condition is false')

# and, ambas as condições tem que ser verdadeiras
"""

"""
if 1 == 1 or 2 == 3:
    print('Condition is true')
else:
    print('Condition is false')

if 1 == 2 or 2 == 3:
    print('New contition is true')
else:
    print('New condition is false')

# or , basta uma ser verdadeira para a condição ser aceita 
"""
"""
if not (1 == 2 or 1 == 1):
    print('Condition is true')
else:
    print('Condition is false')

# if not, ele inverte o valor Porta inversora
"""

correctUser1 = 'wesley'
correctPw1 = 123456

correctUser2 = 'devmedia'
correctPw2 = 'admin'

inputUser = str(input('Type your name: ')).lower()
inputPassword = input('Type your password: ')


if (inputUser == correctUser1 and inputPassword == correctPw1) or (inputUser == correctUser2 and inputPassword == correctPw2):
    print('You has been sucess login')
else:
    print('Something are wrong, please check your loggin and passWord!')