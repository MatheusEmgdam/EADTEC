"""A empresa de marketing TudoWeb precisa realizar uma pesquisa de opinião com seus clientes para saber o grau de satisfação no atendimento. Sua tarefa é:

    Desenvolver um programa em Python utilizando a estrutura de repetição FOR para coletar e exibir o retorno de uma pesquisa de atendimento ao cliente.
    O programa deve solicitar a digitação do nome, idade e opinião do entrevistado sobre o atendimento prestado, sendo:
        1: EXCELENTE
        2: BOM
        3: RUIM
    A pesquisa deve ser feita com 50 entrevistados.
    Ao final, o programa deverá exibir na tela:
    a) Quantidade de respostas “EXCELENTE”
    b) Quantidade de respostas “RUIM”
    Utilize estruturas de decisão para verificar a opinião do entrevistado.
    Realize testes com 10 entrevistados para validar o funcionamento do programa.
    Compartilhe o projeto completo no seu repositório Github, informe o link do repositório no ambiente virtual.
"""
excelente = 0 == "1"
ruim = 0 == "1"
for i in range(10):
    nome=input("Digite o seu nome: ")
    idade=input(int("Digite sua idade: "))
    feedback=input("Como foi o seu atendimento?\n1-Excelente\n2-Bom\n3-Ruim")
    match feedback.lower():
        case "1" | "excelente":
            excelente+=1
        case "3" | "ruim":
            ruim+=1
print("Feedback de Avaliações:\n Excelentes:{excelente}\nRuins:{ruins}")

