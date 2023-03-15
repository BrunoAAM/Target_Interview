##2º Questão## 
#Solicita ao usuário um número inteiro#
number = int(input("Digite um número inteiro: "))

#Definição de variáveis#
a = 0
b = 1
c = 0

#Validação#
while b < number:
    c = b
    b = a + b
    a = c

# Resultado #
if b == number:
    print(f"O número {number} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number} não pertence à sequência de Fibonacci.")
    

    
string = "Exemplo de string a ser invertida"
string_invertida = ""

for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

print(string_invertida)