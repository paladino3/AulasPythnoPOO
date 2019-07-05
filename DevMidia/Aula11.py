print('Teste of Functions')
"""def sum(arg1 , arg2):
    total = arg1 + arg2
    print('This print is inside function: ',total)
    return total;

total_soma_1 = sum(100,155)

total_soma_2 = sum(10,1000)
print(total_soma_1)
print(total_soma_2)

print(sum(30,100))"""

def fatorial (n):
    if n == 1:
        return 1
    else:
        resultado = n * fatorial(n - 1)
        print('intermediate result for {} = {}'.format(n,resultado))
        return resultado;
number = int(input('Type the number: '))
print('Final result: ',fatorial(number))


