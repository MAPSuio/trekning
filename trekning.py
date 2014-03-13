from random import randint
from time import sleep
from math import exp as e
import string

def read_file(filename):
    f = open(filename, "r")
    names = [s.strip() for s in f.readlines()]
    f.close()
    return names

def clear_screen():
    print "\n"*200

def print_message(message, spaces=40, linebreaks=15):
    prefix = " "*spaces
    postfix = "\n"*linebreaks
    print prefix, message, postfix


def perform_draw(names, num_winners=1, num_iterations=32, print_multiplier=1):
    for i in range(1,num_iterations):
        clear_screen() 

        delay = e(i/float(num_iterations))-1.5
        if delay < 0: delay = 0.1
        
        candidates = [names[randint(0, len(names)-1)]*print_multiplier for i in range(num_winners)]
        print_message(", ".join(candidates))

        sleep(delay)

    
    clear_screen() 
    sleep(3)
    
    winners = [names[randint(0, len(names)-1)]*print_multiplier for i in range(num_winners)]
    
    if num_winners > 1: title = "Vinnerne" 
    else: title = "Vinneren"
    
    message = title + " er: " + ", ".join(winners) + ". Gratulerer!"
    print_message(message, spaces=30)

    raw_input()

if __name__ == '__main__':
    names = read_file("navn.txt")

    num_winners = input("Hvor mange vinnere skal jeg trekke? ")

    perform_draw(names, num_winners=num_winners, print_multiplier=5)

