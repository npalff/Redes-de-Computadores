'''
Nicolau Pereira Alff

Pequeno simulador que terá como saída o comportamento do TCP Reno

A saída se dará com uma linha imprimindo as informações:
cwnd ; ssthresh ; duplicate ACK counter ; estado

'''

import sys
import math

estados = ("slow start", "congestion avoidance", "fast recovery")
cwnd = 1
ssthresh = 64
dupACKcount = 0
estadoAtual = 0

def duplicateACK(dupACKcount):
    dupACKcount = dupACKcount+1


def imprimeSaida(cwnd, ssthresh, dupACKcount, estado):
    print("\n- - - - - - - - - - - - - - - - - - - - - - -")
    print("|| cwnd: ", cwnd, "  | ssthresh: ", ssthresh,"  | duplicate ACK counter: ", dupACKcount,"  | Estado: ", estado,"||")
    print("- - - - - - - - - - - - - - - - - - - - - - - \n")

def imprimeMenu():
    print("\n ____________________________________________________")
    print("Ordem o TCP deverá executar: ")
    print("( 1 ) ACK não duplicado")
    print("( 2 ) ACK duplicado")
    print("( 3 ) Expiração do temporizador")
    print("( 5 ) Reset para os valores iniciais")
    print("( 6 ) Iniciar experimento com novos valores")
    print("( 9 ) Encerrar programa\n")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")

def imprimeInicial():
    print("_________________________________________________________\n")
    print("0. Estado Inicial do sistema:")
    imprimeSaida(cwnd, ssthresh, dupACKcount, estados[estadoAtual])

def ACK_nao_Duplicado(counter_Comandos):
    global cwnd, ssthresh, dupACKcount,estadoAtual
    print(counter_Comandos,".\tACK não Duplicado: \n")
    
    if(estadoAtual==0):
        cwnd = cwnd + 1
        dupACKcount = 0
        if cwnd >= ssthresh:
            estadoAtual=1

    elif(estadoAtual==1):
        cwnd = cwnd + 1*(1/cwnd)
        dupACKcount=0

    elif(estadoAtual==2):
        cwnd = ssthresh
        dupACKcount = 0
        estadoAtual = 1

    return

def ACK_Duplicado(counter_Comandos):
    global cwnd, ssthresh, dupACKcount,estadoAtual
    print(counter_Comandos,".\tACK Duplicado: \n")
    
    if(estadoAtual==0):
        dupACKcount+=1
        if dupACKcount==3:
            ssthresh = math.floor(cwnd/2)
            cwnd = ssthresh + 3
            estadoAtual = 2

    elif(estadoAtual==1):
        dupACKcount+=1
        if dupACKcount==3:
            ssthresh = math.floor(cwnd/2)
            cwnd = ssthresh + 3
            estadoAtual = 2

    elif(estadoAtual==2):
        cwnd += 1
    
    return


def timeout(counter_Comandos):
    global cwnd, ssthresh, dupACKcount,estadoAtual
    print(counter_Comandos,".\tExpiração do Temporizador: \n")
    
    if(estadoAtual==0):
        ssthresh = math.floor(cwnd/2)
        cwnd=1
        dupACKcount=0

    elif(estadoAtual==1):
        ssthresh = math.floor(cwnd/2)
        cwnd=1
        dupACKcount=0
        estadoAtual = 0

    elif(estadoAtual==2):
        ssthresh = math.floor(cwnd/2)
        cwnd=1
        dupACKcount=0
        estadoAtual = 0
    
    
    return


def main():
    global cwnd, ssthresh, dupACKcount,estadoAtual
    Comando = 0
    counter_ACK_nD =0
    counter_ACK_D =0
    counter_Timeout =0
    counter_Comandos =0

    if len(sys.argv)==3:
        cwnd = int(sys.argv[1])
        ssthresh = int(sys.argv[2])
    elif len(sys.argv) != 1:
        print(" ####\t\tErro na chamada!\t\t####\nChamada deve ser python3 TCP_Reno_sim.py <tamanho da janela inicial (cwnd)> <tamanho do ssthresh inicial>\nIniciando com os valores default de cwnd=1 e ssthresh=64\n\n")

    imprimeInicial()
    counter_Comandos+=1

    while(Comando !=9):
        imprimeMenu()
        Comando=input("Insira seu comando: ")
        Comando = int(Comando)
        if Comando == 1:
            ACK_nao_Duplicado(counter_Comandos)
            imprimeSaida(cwnd, ssthresh, dupACKcount, estados[estadoAtual])
            counter_ACK_nD+=1
            counter_Comandos+=1
        elif Comando == 2:
            ACK_Duplicado(counter_Comandos)
            imprimeSaida(cwnd, ssthresh, dupACKcount, estados[estadoAtual])
            counter_ACK_D+=1
            counter_Comandos+=1
        elif(Comando == 3):
            timeout(counter_Comandos)
            imprimeSaida(cwnd, ssthresh, dupACKcount, estados[estadoAtual])
            counter_Timeout+=1
            counter_Comandos+=1
        elif(Comando == 5):
            cwnd = 1
            ssthresh = 64
            dupACKcount = 0
            estadoAtual = 0
            counter_ACK_D = 0
            counter_ACK_nD = 0
            counter_Timeout = 0
            counter_Comandos = 0
            imprimeInicial()
            counter_Comandos+=1

        elif(Comando == 6):
            print("\n\n\n\n\n\n\n\n")
            cwnd = int(input("Tamanho da janela (cwnd): "))
            ssthresh = int(input("Tamanho do ssthresh: "))
            dupACKcount = 0
            estadoEscolhido = input("Estado atual(slow start, congestion avoidance, fast recovery): ")
            if not(estadoEscolhido in estados):
                print("Estado escolhido inválido -- estado iniciará em slow start")
                estadoAtual=0
            else:
                estadoAtual= estados.index(estadoEscolhido)
            counter_ACK_D = 0
            counter_ACK_nD = 0
            counter_Timeout = 0
            counter_Comandos = 0
            imprimeInicial()
            counter_Comandos+=1


        elif(Comando == 9):
            return
        else:
            print("#\tComando inválido\t#\n\n")


main()
