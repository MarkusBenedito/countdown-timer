import time

horario = input("Você quer saber as horas?")
#Aqui a variável armazena a resposta do usuário.
#Logo depois é feita uma validação para ver se o usuário quer ou não saber as horas.
if (horario == "Sim"):
    print(time.strftime("O horário é: %H Horas: %M Minutos: %S Segundos"))
    #Caso a resposta seja sim, vai ser exibido as horas seguidas dos minutos e depois dos segundos.
else:
    print("Não foi possível continuar")
    #Caso a resposta for diferente de sim, o algoritmo vai ser encerrado.