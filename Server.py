from socket import *
from random import *

serverPort = 27123
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(5) # o argumento “listen” diz à biblioteca de soquetes que queremos enfileirar no máximo 5 requisições de conexão (normalmente o máximo) antes de recusar começar a recusar conexões externas. Caso o resto do código esteja escrito corretamente, isso deverá ser o suficiente.
print ("TCP Server: Online\n")
connectionSocket, addr = serverSocket.accept()
convert = connectionSocket.recv(1024)
convert2 = int.from_bytes(convert, "big")
turn = int(convert2)
yourhp = 15 * turn
cpuhp = 15 * turn
battle = True
while battle == True:
    sentence = connectionSocket.recv(1024)
    d = int.from_bytes(sentence, "big")
    received = int(d)
    print("Confirmação da escolha do jogador:", received)
    attack = randrange(2)
    if ((received == 1 and attack == 0) or (received == 2 and attack == 1) or (received == 3 and attack == 2)):
            result = 2
    elif ((received == 1 and attack == 1) or (received == 2 and attack == 2) or (received == 3 and attack == 0)):
            result = 3
            yourhp = yourhp - 15
    else:
            result = 1
            cpuhp = cpuhp - 15
    print("Resultado desse round: 1 = Vitória do Jogador / 2 = Empate / 3 = Vitória do CPU")
    print("Resultado da disputa:", result)
    x = result.to_bytes((result.bit_length() + 7) // 8, byteorder='little')
    connectionSocket.send(bytes(x))
    if (cpuhp <= 0 and yourhp <= 0):
        print("Resultado final: Empate")
        battle = False
        print("TCP Server: Offline")
    elif (cpuhp > 0 and yourhp <= 0):
        print("Resultado final: Vitória do CPU")
        battle = False
        print("TCP Server: Offline")
    elif (cpuhp <= 0 and yourhp > 0):
        print("Resultado final: Vitória do Jogador")
        battle = False
        print("TCP Server: Offline")
    else:
        battle = True

connectionSocket.close()
