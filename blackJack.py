import random
import string
import sys

# Duas cartas iniciais
# Ás vale 1 ou 11
# J, K e Q valem 10
# https://stackoverflow.com/questions/69946172/how-can-i-print-my-ascii-cards-side-by-side


valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
naipe = ['♥', '♦', '♣', '♠']
cartas_do_baralho = []


for v in valores:
    cartas_do_baralho.append(str(v) + '♥')
    cartas_do_baralho.append(str(v) + '♦')
    cartas_do_baralho.append(str(v) + '♣')
    cartas_do_baralho.append(str(v) + '♠')


def jogo():
    print("\nBem vindo ao jogo de BlackJack.")
    escolha = int(input("\nDigite 1 para começar ou 0 para voltar: "))
    if escolha == 1:
        jogada_cpu(cartas_do_baralho)
        jogada(cartas_do_baralho)

    else:
        import menuAps
        menuAps.menu()


def jogada(cartas_do_baralho):
    cartas_jogador = []
    print("\n\nSuas cartas:")
    for i in range(2):
        carta = random.choice(cartas_do_baralho)
        cartas_do_baralho.remove(carta)
        cartas_jogador.append(carta)
        valor = str(carta).strip("♥♦♣♠")
        naipe = carta[-1]
        desenha_carta(valor, naipe)
    continua = int(
        input("Deseja continuar? \nDigite 1 para continuar e 0 para parar: "))
    if continua == 1:
        pedir_carta(carta, cartas_do_baralho, cartas_jogador)
    else:
        global pontos_jogador
        pontos_jogador = conta_carta(
            carta, cartas_jogador, string='total jogador')
        global pontos_cpu
        ver_ganhador(pontos_jogador, pontos_cpu)


def jogada_cpu(cartas_do_baralho):
    cartas_cpu = []
    contador = 0
    print("\n\nCartas do adversário:")
    while contador < 17:
        carta = random.choice(cartas_do_baralho)
        cartas_do_baralho.remove(carta)
        cartas_cpu.append(carta)
        valor = str(carta.strip("♥♦♣♠"))
        naipe = carta[-1]
        desenha_carta(valor, naipe)
        contador = conta_carta(carta, cartas_cpu, string='Total Cpu')
    global pontos_cpu
    pontos_cpu = conta_carta(carta, cartas_cpu, string='total cpu')


def desenha_carta(v, n):  # v de valor e n de naipe.
    if v == '11':
        v = 'J'
    elif v == '12':
        v = 'Q'
    elif v == '13':
        v = 'K'
    elif v == '1':
        v = 'A'
    if len(v) == 1:
        v = (v + " ")
    print(" _____________________")
    print("|                     |")
    print(f"|  {v}                 |")
    print(f"|  {n}                  |")
    print("|                     |")
    print("|                     |")
    print("|                     |")
    print(f"|          {n}          |")
    print("|                     |")
    print("|                     |")
    print("|                     |")
    print(f"|                  {n}  |")
    print(f"|                  {v} |")
    print("|_____________________|")

# print("\n".join(map('  '.join, zip(*(desenha_carta(v, n))))))


def pedir_carta(carta, cartas_do_baralho, cartas_na_mao):
    carta = random.choice(cartas_do_baralho)
    cartas_do_baralho.remove(carta)
    cartas_na_mao.append(carta)
    valor = str(carta).strip("♥♦♣♠")
    naipe = carta[-1]
    desenha_carta(valor, naipe)
    continua = int(
        input("Deseja continuar? \nDigite 1 para continuar e 0 para parar: "))
    if continua == 1:
        pedir_carta(carta, cartas_do_baralho, cartas_na_mao)
    else:
        global pontos_jogador
        pontos_jogador = conta_carta(
            carta, cartas_na_mao, string='total jogador')
        global pontos_cpu
        ver_ganhador(pontos_jogador, pontos_cpu)


def conta_carta(carta, cartas_na_mao, string):
    total_jogador = 0
    for carta in cartas_na_mao:
        carta = carta.strip("♥♦♣♠")
        carta = int(carta)
        if carta == 11:
            carta = 10
        if carta == 12:
            carta = 10
        if carta == 13:
            carta = 10
        if carta == 1:
            if total_jogador < 11:
                carta = 11
            else:
                carta = 1
        total_jogador += carta
    print(total_jogador, string)
    return total_jogador


def ver_ganhador(jogador, cpu):
    if jogador == cpu:
        print("Empate!")
    elif jogador > 21 and cpu > 21:
        print("Empate!")
    elif jogador > cpu:
        if jogador <= 21:
            print("Você venceu!")
        else:
            print("Você perdeu!")
    else:
        if cpu <= 21:
            print("Você perdeu!")
        else:
            print("Você venceu!")


jogo()
