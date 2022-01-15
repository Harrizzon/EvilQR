#!/usr/bin/python3
import qrcode, signal, sys
from alive_progress import alive_bar
from time import sleep
from os import system

# Colors
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

# Banner
system('clear')
banner =  style.RED + """
     7MMlllYMM            db   7MM    g8ll8q   7MMlllMq  
      MM     7                  MM  dP      YM  MM    MM 
      MM   d  7M     MF  7MM    MM dM        MM MM    M9  
      MMmmMM   VA    V    MM    MM MM        MM MMmmdM9  """ +style.RESET  + style.CYAN + """(by: Harrizzon) """ + style.RESET +  style.RED + """
      MM   Y    VA  V     MM    MM MM        MP MM  YM  
      MM      M  VVV      MM    MM  Mb      dP  MM    Mb 
     JMMmmmmMMM   W      JMML  JMML  llbmmdl   JMML   JMM
                                         MMb              
                                          bood    
""" + style.RESET


# Exit
def ctrl_c(sig, frame):
    system('clear')
    print(style.RED + "\n [!] Saliendo")
    sys.exit(0)
signal.signal(signal.SIGINT, ctrl_c)
# MAIN
if __name__ == '__main__':
    print(banner)

    if len(sys.argv) == 1:
        main_url = input("Enter an URL: ")
        #Empty URL
        if len(main_url) == 0:

            print(style.RED + "[!]" + style.WHITE + "Enter a valid URL" + style.RESET)
            sys.exit(1)
        #URL
        if len(main_url) == 1:
            while True:
                choose_mask = input(style.YELLOW + "¿do you want to mask the url? " + style.GREEN + "(y/m)\n" + style.RESET)
                if choose_mask == "n":
                    system('clear')
                    qr = qrcode.QRCode(
                    version=4,
                    box_size=10,
                    border=1
                    )
                    qr.add_data(main_url)
                    qr.make(fit=True)
                    img = qr.make_image(fill='black', back_color='white')
                    print(style.YELLOW + "\nGenerando Codigo QR\n" + style.RESET)
                    
                    # QR GENERATING
                    with alive_bar(100, spinner='pulse') as progrs:
                        for i in range(100):
                            sleep(0.01)
                            progrs()
                    system('clear')        
                    print(style.GREEN + "\n\n[>] QR Generado con exito [<]" + style.RESET)
                    print(style.GREEN + "Archivo almacenado en el repositorio: " + style.RESET + style.CYAN + "EvilQR/eQRCode.png " + style.RESET)
                    sleep(4)
                    system('clear')
                    img.save('eQRCode.png')
                    sys.exit(0)
                if choose_mask == "y":
                    system('clear')
                    





                else:
                    system('clear')
                    print(style.RED + "\n [!] Please enter a valid option" + style.RESET)
                    sleep(2)
                    system('clear')

    else:
        print(style.RED + "[!]" + style.WHITE + "Invalid Argument" + style.RESET)
        sys.exit(1)
        
    
    
    
    
    




# QR 
qr = qrcode.QRCode(
version=4,
box_size=10,
border=1
)
qr.add_data(main_url)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')

print(style.GREEN + "Generando Codigo QR\n")

# QR GENERATING
with alive_bar(100, spinner='pulse') as progrs:
    for i in range(100):
        sleep(0.01)
        progrs()
        system('clear')
        print(style.GREEN + "\n[>] QR Generado con exito [<]" + style.RESET)
        print(style.GREEN + "Archivo almacenado en el repositorio: " + style.RESET + style.CYAN + "EvilQR/eQRCode.png " + style.RESET)
        sleep(5)
        system('clear')
        img.save('eQRCode.png')

    

