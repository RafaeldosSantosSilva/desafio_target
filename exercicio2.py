#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 
# e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, 
# informado um número, ele calcule a sequência de Fibonacci 
# e retorne uma mensagem avisando se o número informado pertence ou não a sequência.



numero = int(input('Digite um número: '))
fib1, fib2 = 0, 1

# Verifica se o número é 0 ou 1 (caso especial)
if numero == 0:
    print(f'O {numero} está na sequência de Fibonacci')
elif numero == 1:
    print(f'O {numero} está na sequência de Fibonacci')
else:
    # Loop para gerar a sequência de Fibonacci
    while True:
        fib1, fib2 = fib2, fib1 + fib2
        if fib1 == numero:
            print(f'O {numero} está na sequência de Fibonacci')
            break
        elif fib1 > numero:
            print(f'O {numero} não pertence à sequência de Fibonacci')
            break
