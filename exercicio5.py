#5) Escreva um programa que inverta os caracteres de um string.
#IMPORTANTE:
# Essa string pode ser informada através de qualquer entrada de sua preferência ou 
# pode ser previamente definida no código;
# Evite usar funções prontas, como, por exemplo, reverse;




string = input('Digite uma palavra: ').lower()

print(string)

string_contrario = string[::-1]

print(string_contrario)