# Crie um programa que receba um número inteiro e calcule
# o fatorial desse número usando uma estrutura de repetição.
n = int(input("Digite o numero a ser fatorado:"))
c = n
f = 1
print(f'Calculando {n}!', end='')
while c > 0:
    print(f'{c}', end='')
    print('x' if c > 1 else '=', end='')
    f *= c
    c -=1
    print(f'{f}')
    
