#LISTA 1 - IA - EXERCICIOS PRATICOS SAMUEL BORONI

#1 - EXERCÍCIOS DA APOSTILA

#A
A = "Um elefante incomoda muita gente";
print (A)

x = A[3:21]
print (x)

#B
frase = input("Olá!! Digite sua frase: ")

x = frase.upper()
y = x.replace(" ","")

print(y)

#C
x = int(input("Digite um valor inteiro para X: "))

y = int(input("Digite um valor inteiro para Y: "))

z = (((x**2)+(y**2))/((x-y)**2))

print("O valor da equacao e: ", z)

#D
salario = float(input("Digite o seu salário atual: "))

ns = (salario*(1.35))

print("O seu salario reajustado e: ", ns)

#E
L = [5, 7, 2, 9, 4, 1, 3]

tam = len(L)
print("O tamanho da lista L e: ", tam)

maior = max(L)
print("O maior valor da lista L e: ", maior)

menor = min(L)
print("O menor valor da lista L e: ", menor)

soma = sum(L)
print("A soma de todos os elementos da lista L e: ", soma)

L.sort()
print("A ordem crescente da lista L e: ", L)

L.sort(reverse = True)
print("A ordem decrescente da lista L e: ", L)

#F
lista = list(range(3,50,3))

print(lista)

#G "ERRO"
dicionario_lanchonete = {"Salgado" : 4.50, "Lanche" : 6.50, "Suco" : 3.00, "Refrigerante" : 3.50, "Doce":1.00}
print(dicionario_lanchonete)

#H
alunos_notas = {"Samuel" : 9.50, "Luis" : 6.50, "Marcos" : 9.00, "Lidia" : 9.80, "Maria":7.00}

print(alunos_notas)
notas = alunos_notas.values()
soma = sum(notas)

media = soma/5

print("A média das notas dos alunos foi: ", media)

#I
nota1 = float(input("Digite o valor da nota 1: "))
nota2 = float(input("Digite o valor da nota 2: "))

media = (nota1 + nota2)/2

if media > 6:
    print("Parabens! Voce foi aprovado e sua media e: ", media)
else:
    print("Voce foi reprovado e sua media e: ", media)

#J
nota1 = float(input("Digite o valor da nota 1: "))
nota2 = float(input("Digite o valor da nota 2: "))

media = (nota1 + nota2)/2

if media > 6:
    print("Parabens! Voce foi aprovado e sua media e: ", media)
elif media >= 4:
    print("Voce podera realizar o exame e sua media e: ", media)
else:
    print("Voce foi reprovado e sua media e: ", media)

#K
S = 0
for x in range (3,334,3):
    S = S + x
print("A soma e: ",S)

#L
S = 0
for x in range (1,11):
    nota = float(input("Digite a nota " +str(x) + ": "))
    S = S + nota

media = S/x
print(media)

#M
num = int(input("Digite um numero de 1 a 10 para apresentar sua tabuada: "))

while (num < 1) or (num > 10):
    num = int(input("Digite um numero VALIDO de 1 a 10 para apresentar sua tabuada: "))


for x in range(1,11):
    print("%2d x %2d = %3d" %(x,num,x*num))

#N
def func_linha(x):
    for i in range (x):
        print(end='_')

func_linha(100)

#O - ERRO

#P - ERRO

#2
nums = [i for i in range(1,1001)]
sentence = "Practice Problems to Drill List Comprehension in Your Head."

#A
nums = [i for i in range(1,1001) if i%8 == 0]
print(nums)

#B



#C
sentence = "Practice Problems to Drill List Comprehension in Your Head."
x = len(sentence)
S = 0
for x in sentence:
    if x == " ":
        S =S+1
print("O número de espaços na sentença é: ",S)

#D
sentence = "Practice Problems to Drill List Comprehension in Your Head."

a = sentence.replace("a","")
e = a.replace("e","")
i = e.replace("i","")
o = i.replace("o","")
u = o.replace("u","")
print("A sentença sem as vogais fica: ", u)

#E
sentence = "Practice Problems to Drill List Comprehension in Your Head."
nova = sentence.split()
x = len(nova)
s = 0
for x in nova:
    tamanho = len(nova[s])
    if tamanho < 5:
        print(nova[s])
    s = s + 1


#3
#A
class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

samuel = Pessoa("Samuel")
print(samuel)
matheus = Pessoa("Matheus")
print(matheus)

#B
class Calculadora:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b

    def subtrai(self):
        return self.a - self.b

    def multiplica(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

c = Calculadora(10,5)
print('Soma:', c.soma())
print('Subtração:', c.subtrai())
print('Multiplicação:', c.multiplica())
print('Divisão:', c.divide())

#C
class Calculadora_Simples:

    def soma(self, a, b):
        return a + b

    def subtrai(self, a, b):
        return a - b

    def multiplica(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

c = Calculadora_Simples()
print('Soma:', c.soma(10,5))
print('Subtração:', c.subtrai(10,5))
print('Multiplicação:', c.multiplica(10,5))
print('Divisão:', c.divide(10,5))

#D





