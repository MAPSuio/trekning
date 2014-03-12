from random import randint
from time import sleep
from math import exp as e
import string

def clear_screen():
    print "\n"*200

def print_name(name, spaces=40, linebreaks=15):
    prefix = " "*spaces
    postfix = "\n"*linebreaks
    print prefix, name, postfix


def perform_draw(names, num_iterations=32, print_multiplier=1):
    for i in range(1,num_iterations):
        clear_screen() 

        delay = e(i/float(num_iterations))-1.5
        if delay < 0: delay = 0.1
        
        name = names[randint(0, len(names)-1)]*print_multiplier
        print_name(name)

        sleep(delay)

    
    clear_screen() 
    sleep(3)
    
    winner = names[randint(0, len(names)-1)]*print_multiplier
    message = "Vinneren er: " + winner + ". Gratulerer!"
    print_name(message, spaces=30)

    raw_input()

if __name__ == '__main__':

    names = list(string.ascii_lowercase) #["fredrik", "torkil", "torgeir"]

    perform_draw(names, print_multiplier=5)

