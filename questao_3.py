# 3) Descubra a lógica e complete o próximo elemento:
##############################################################
# a) 1, 3, 5, 7, _9_
print("a)")

# P.A com razão de 2

def paRateOf2(number, quantity):

    sequence = []
    
    for i in range(0, quantity):
        sequence.append(number)
        number += 2

    return sequence

print(paRateOf2(1, 10))

##############################################################
# b) 2, 4, 8, 16, 32, 64, _128_
print("b)")

# P.G com razão de 2
def pgRateOf2(number, quantity):
    sequence = []

    for i in range(0, quantity):
        sequence.append(number)
        number *= 2

    print(sequence)

pgRateOf2(2, 10)

##############################################################
# c) 0, 1, 4, 9, 16, 25, 36, _49_
print("c)")

# P.A sobre P.A
def paOverPaOf2(number, quantity):
    sequence = []
    paOf2 = paRateOf2(1, quantity)
    sum = 0
    for i in range(0, quantity):
        sequence.append(sum)
        sum += paOf2[i]

    print(sequence)

paOverPaOf2(0, 10)

##############################################################
# d) 4, 16, 36, 64, _104_
print("d)")

def strange_sequence(number, quantity):
    
    sequence = [number]
    
    sequence.append(number * number)

    sum = number
    temp = sum
    for i in range(1, quantity + 1):
        temp = temp + i
        sum += temp
        sequence.append(4 * sum)

    print(sequence)
        
strange_sequence(4, 10)

##############################################################
# e) 1, 1, 2, 3, 5, 8, _13_
print("e)")

# Sequência de Fibonacci
def fibonacci(quantity):
    
    first_element = 0
    second_element = 1

    fibo = [first_element, second_element]

    for i in range(0, quantity):
        sum = first_element + second_element
        
        fibo.append(sum)

        first_element = second_element
        second_element = sum
    
    print(fibo)

fibonacci(10)

##############################################################
# f) 2, 10, 12, 16, 17, 18, 19, _20_
print("f)")

# Eu acho que a sequẽncia acima está errada, pois o número 12 deveria ser 14, ou seja, provavelmente foi um erro de digitação
# pois não há como a razão de uma pg ou pa que está descendo, subir sem motivo aparente.
# No caso a sequência correta seria: 2, 10, 14, 16, 17, 18, 19, 20

def paOfDescendingRate(number, quantity):
    rate = 8
    sequence = [number]
    for i in range(0, quantity - 1):
        if(rate > 1):
            number += rate
            sequence.append(int(number))
            rate /= 2
        else:
            number += 1
            sequence.append(int(number))
    
    print(sequence)

paOfDescendingRate(2, 10)