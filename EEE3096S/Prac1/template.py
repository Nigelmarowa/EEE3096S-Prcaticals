#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: <Nigel Marowa>
Student Number: <MRWNIG002>
Prac: <Prac 1>
Date: <29/07/2019>
"""
# import Relevant Librares
# import Librares
import RPi.GPIO as GPIO
from time import sleep
from itertools import product

#LEDs pin out
outputpin = [13, 31, 37] 

#pin out for the button pins
inputpin = [15, 29] 

# outputs showing the list for the 3-bit counter
listCounter =list(product([0,1], repeat=3)) 