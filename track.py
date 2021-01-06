# Coded by FUEGO
# Looking to work with other hit me up on my email fuego770@protonmail.com <--

from random import choice
from time import ctime,sleep,time
from os import system


def clearscreen():
    system('clear')


color={
    'PURPLE':'\033[95m',
    'CYAN':'\033[96m',
    'BLUE':'\033[94m',
    'OFFYELLOW':'\033[37m',
    'RED':'\033[91m',
    'CWHITE':'\33[37m',
    'BOLD':'\033[1m',
    'TIME':'\033[5m'
    }

colors = ['PURPLE','CYAN','BLUE','OFFYELLOW','RED','CWHITE']


def random_color_choice():
    color1=color[choice(colors)]
    color2=color[choice(colors)]
    color3=color[choice(colors)]
    color4=color[choice(colors)]
    color5=color[choice(colors)]

    if (color1==color2) or (color1==color3) or (color1==color4) or (color1==color5) or (color2==color3) or (color2==color4) or (color2==color5) or (color3==color4) or (color3==color5) or (color4==color5):
        random_color_choice()

    return (color1,color2,color3,color4,color5)

color1,color2,color3,color4,color5=random_color_choice()
counter=0


while True:

    if counter %2 == 0:
        banner = color['BOLD'] + color1 + '''

            88888888888 8888888b.         d8888  .d8888b.  888    d8P
                888     888   Y88b       d88888 d88P  Y88b 888   d8P
                888     888    888      d88P888 888    888 888  d8P
                888     888   d88P     d88P 888 888        888d88K
                888     8888888P"     d88P  888 888        8888888b
                888     888 T88b     d88P   888 888    888 888  Y88b
                888     888  T88b   d8888888888 Y88b  d88P 888   Y88b
                888     888   T88b d88P     888  "Y8888P"  888    Y88b

    {}Welcome to TRACK, the app that helps you to overcome your laptop addiction.
                 {}It lets you concerntrate and focus on your work.

                            {}TIME:{}{}

            {}------------------ Coded By Fuego ------------------{}
        '''.format(color2,color3,color4,color['TIME']+ctime(),'\33[m',color4,'\33[m')

    else:
        banner = color['BOLD'] + color1 + '''

            88888888888 8888888b.         d8888  .d8888b.  888    d8P
                888     888   Y88b       d88888 d88P  Y88b 888   d8P
                888     888    888      d88P888 888    888 888  d8P
                888     888   d88P     d88P 888 888        888d88K
                888     8888888P"     d88P  888 888        8888888b
                888     888 T88b     d88P   888 888    888 888  Y88b
                888     888  T88b   d8888888888 Y88b  d88P 888   Y88b
                888     888   T88b d88P     888  "Y8888P"  888    Y88b

    {}Welcome to TRACK, the app that helps you to overcome your laptop addiction.
                 {}It lets you concerntrate and focus on your work.

                            {}TIME:{}{}

            {}------------------ Coded By Fuego ------------------{}
        '''.format(color2,color3,color4,color['TIME']+ctime(),'\33[m',color5,'\33[m')


    print(banner)
    sleep(.5)
    clearscreen()
    counter+=1

    if counter==10:
        break


from functionalities import Functionalities
function=Functionalities()

try:
    if open('tasks','r'):
        function.assign_time()
        function.lock()
except FileNotFoundError:
    choice=input('Do you want to create lock your pc timing(y/n): ')
    if choice=='y':
        print('You have not created any to do tasks for  to do, please do that first.')
        function.start()
    else:
        function.start()

#Main part of Program
#program version 1.0.1
#https://janakiev.com/blog/python-background/
