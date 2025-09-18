import random

def vencedor(opP,opC):
    if opP == opC:
        return "Empate"
    elif (opP == "Pedra" and opC == "Tesoura") or \
        (opP == "Tesoura" and opC == "Papel") or \
            (opP == "Papel" and opC == "Pedra"):
                return "Jogador ganhou"
    else:
        return "Maquina Ganhou"

opcoes = ["Pedra","Papel","Tesoura"]
jogador = input(f"Ecolha uma das opções a seguir: {opcoes}\n")
computador = random.choice(opcoes)
print(f"Opção do Jogador: {jogador}\nOpção da Maquina: {computador}\n Resultado Final: {vencedor(jogador,computador)}")