#Biblioteca
import os

#Variáveis e funções
def clear():
     os.system('cls' if os.name == 'nt' else 'clear')

excelente = 0 
ruim = 0

for i in range(10):
    #INPUT
    nome=input("Digite o seu nome: ")
    idade=int(input("Digite sua idade: "))
    print("Como foi seu atendimento?\n")
    feedback=input("1-Excelente\n2-Bom\n3-Ruim\n")
    clear()
    #Avaliação do Feedback
    match feedback.lower():
        case "1" | "excelente":
            excelente+=1
        case "3" | "ruim":
            ruim+=1
#OUTPUT
print(f"Feedback de Avaliações:\n Excelentes:{excelente}\nRuins:{ruim}")
