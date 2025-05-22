#1.pedir o numero de qual tabuada faremos
numero = int(input('digite a tabuada que iremos fazer:'))

#2.deve digitar da onde a tabuada deverá começar.
i = int(input('onde desejar começpar a tabuada:'))

#3.deve digitar da onde a tabuada deverá encerrar.
terminio = int(input('onde desejar encerrar a tabuadas:'))

while i <= 10:
    print(f' {i} x {numero} = {i* numero}') 
    i +=1