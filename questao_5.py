# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:

# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

# b) Evite usar funções prontas, como, por exemplo, reverse;


def reverse_string(string):
    new_string = []
    string = list(string)
    for i in range(0, len(string)):
        size = len(string)
        new_string.append(string[size - 1])
        string.pop()

    return "".join(new_string)

print(reverse_string("): ocincét etset o lagel otiuM"))
print(reverse_string("reverse_string"))
print(reverse_string("ABCDEFGHIJKLMNOPQRSTUVWYXZ"))
