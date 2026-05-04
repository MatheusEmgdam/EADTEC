from colorama import init, Fore, Style
init(autoreset=True)

niveis = [1, 2, 3, 4, 5]

situacoes = {
    1: "Muito baixo (crítico)",
    2: "Baixo",                
    3: "Médio",                
    4: "Alto",                 
    5: "Muito alto (alerta)"   
}

cores = {
    1: Fore.RED,
    2: Fore.YELLOW,
    3: Fore.GREEN,
    4: Fore.CYAN,
    5: Fore.BLUE
}

def simulação(n):
     nivel_atual = n
     situacao_atual = situacoes[n]
     cor_atual = cores[n]
     print(f"Nível {nivel_atual}: {cor_atual}{situacao_atual}{Style.RESET_ALL}")
valor_teste=int(input("Digite um valor de entrada(1-5)\n>")) 
simulação(valor_teste)