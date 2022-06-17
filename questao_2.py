# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
#    (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
#    ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE:

# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
def findNumber(x, lis):
    
    for i in range(0, len(lis)):
        
        if(x == lis[i]):
            return True

    return False

def fibonacci(x):
    
    first_element = 0
    second_element = 1

    fibo = [first_element, second_element]

    for i in range(0, x):
        sum = first_element + second_element
        
        fibo.append(sum)

        first_element = second_element
        second_element = sum
    
    print(fibo)
    
    if(findNumber(x, fibo)):
        print(f"\nO número informado {x} pertece a sequência Fibonacci!\n")
    else:
        print(f"\nO número informado {x} não pertece a sequência Fibonacci!\n")

fibonacci(3)
fibonacci(5)
fibonacci(8)
fibonacci(12)
fibonacci(15)