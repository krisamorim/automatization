import pyautogui
from time import sleep

# print("Aguardando 3 segundos para iniciar o processo..")
# sleep(3)

UnfollowingButtonPositionX = 736
UnfollowingButtonPositionY = 1837
FollowingButtonPositionX = 753
FollowingButtonPositionY = 1519
positionX = 826
positionY = 1654
movePosition = 60

#obtendo quantidade de veses desejadas
repeticaoVezes = input("Quantas vezes deseja repetir o processo? (Digite um número): \n")
if not repeticaoVezes.isdigit() or int(repeticaoVezes) <= 0:
    repeticaoVezes = 1
    print("Entrada inválida. O processo será repetido 1 vez.\n")

#criando laço para repetir movimento do mouse
for i in range(int(repeticaoVezes)):
    print(f"Repetição {i+1} de {repeticaoVezes}...")

    # Clicando no item
    print(f'Y em {positionY}...\n')
    pyautogui.click(positionX, positionY)
    sleep(5)

    #clicando no following
    pyautogui.click(FollowingButtonPositionX, FollowingButtonPositionY)
    sleep(2)

    #clicando no unfollow
    pyautogui.click(UnfollowingButtonPositionX, UnfollowingButtonPositionY)
    sleep(2)

    #fechar aba
    pyautogui.hotkey('ctrl','w')
    sleep(1)

    positionY += movePosition
    print(f'Y atualizado para {positionY}...\n')



# print("Mostrando posição do mouse para o usuário...")
# #Obtendo posição do mouse
# x, y = pyautogui.position()
# print(f"Posição do mouse: x={x}, y={y}")
# sleep(2)
# #Obtendo posição do mouse
# x, y = pyautogui.position()
# print(f"Posição do mouse: x={x}, y={y}")
