
from calculadora import Calculadora
calc = Calculadora()


largura: float = float(input('Qual a largura do comodo? '))
profundidade: float = float(input('Qual a profundidade do comodo? '))
altura:float = 2.9

calc.area_paredes: float = 2 *(largura + profundidade)

print('A area das paredes é:{} '.format(calc.area_paredes))

calc.area_teto: float = largura * profundidade

print('A área do teto é: {}'.format(calc.area_teto))