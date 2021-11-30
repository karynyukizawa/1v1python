from socket import *
serverName = "127.0.0.1"
serverPort = 27123
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

turn = int(input("Defina a quantidade mínima de turnos do jogo: "))
nturn = turn.to_bytes((turn.bit_length() + 7) // 8, byteorder='little')
clientSocket.send(bytes(nturn))

yourhp = 15 * turn
cpuhp = 15 * turn
battle = True

print("Você pode escolher entre [1] Finta, [2] Soco Forte ou [3] Contra-Ataque.")
print("Funciona como Pedra, Papel e Tesoura. Finta vence o Contra-Ataque, Soco Forte vence a Finta e o Contra-Ataque vence o Soco Forte.")
while (battle == True):
        while True:
                try:
                        chosenattack = int(input("Faça sua escolha: "))                
                        assert 0 < chosenattack < 4
                except ValueError:
                        print("Por favor, escolha a ação utilizando os números entre colchetes.")
                except AssertionError:
                        print("Ação não encontrada. Por favor, tente novamente.")
                else:
                        break
        x = chosenattack.to_bytes((chosenattack.bit_length() + 7) // 8, byteorder='little')
        clientSocket.send(bytes(x))
        res = clientSocket.recv(1024)
        r = int.from_bytes(res, "big")
        result = int(r)
        if (result == 1):
                if (chosenattack == 1):
                        print("O CPU tentou contra-atacar mas não esperava sua finta.")
                        cpuhp = cpuhp - 15
                        print("Seu HP é", yourhp)
                        print("O HP do CPU é", cpuhp, end='\n')
                elif (chosenattack == 2):
                        print("O CPU tentou usar uma finta, mas seu soco forte veio mais rápido.")
                        cpuhp = cpuhp - 15
                        print("Seu HP é", yourhp)
                        print("O HP do CPU é", cpuhp)
                else:
                        print("O CPU tentou um soco forte e você previu isso, dando um ótimo contra-ataque.")
                        cpuhp = cpuhp - 15
                        print("Seu HP é", yourhp)
                        print("O HP do CPU é", cpuhp)

        elif (result == 2):
                if (chosenattack == 1):
                        print("Vocês trocam socos leves mas nada demais.\n")
                elif (chosenattack == 2):
                        print("Vocês trocam socos fortes.\n")
                else:
                        print("Vocês esperam um ataque do outro... Mas nada acontece, feijoada.\n")
        else:
                if (chosenattack == 1):
                        print("Você tentou usar uma finta, mas o CPU previu seus movimentos e deu um soco forte antes de você poder reagir.")
                        yourhp = yourhp - 15
                        print("Seu HP é", yourhp)
                        print("O HP do CPU é", cpuhp, end='\n')
                elif (chosenattack == 2):
                        print("Você ataca com um soco forte... Porém o CPU desvia e aplica um contra-ataque bem certeiro.")
                        yourhp = yourhp - 15
                        print("Seu HP é", yourhp)
                        print("O HP do CPU é", cpuhp)
                else:
                        print("Antes de você conseguir preparar seu contra-ataque, uma finta rápida do CPU lhe acerta.")
                        yourhp = yourhp - 15
                        print("Seu HP é", yourhp)
                        print("O HP do CPU é", cpuhp)
                        
        if (cpuhp <= 0 and yourhp <= 0):
                battle = False
                print("Ambos cairam no chão exaustos! É um empate!")
        elif (cpuhp > 0 and yourhp <= 0):
                battle = False
                print("Que pena, você perdeu. Tente novamente.")
        elif (cpuhp <= 0 and yourhp > 0):
                battle = False
                print("Parabéns! Você venceu!")
        else:
                battle = True
                
clientSocket.close()
