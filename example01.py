# # -*- coding: utf-8 -*-

# nombre = input('Cuál es tu nombre?')
# print('Tu nombre es: ', nombre)

# -*- coding: utf-8 -*-

import turtle

def main():
    window = turtle.Screen
    dave = turtle.Turtle()

    make_square(dave)

def make_square(dave):
    make_line_and_turn(dave, 100)

def make_line_and_turn(dave, length):
    dave.forward(length)
    dave.left(90)

if __name__ == '__main__':
   
   