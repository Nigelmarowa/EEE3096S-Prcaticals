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

#LEDs pin out for board
outputpin = [13, 31, 37] 

#pin out for the button pins
inputpin = [15, 29] 

# outputs showing the list for the 3-bit counter

listCounter =list(product([0,1], repeat=3))

#This is where the main function starts
def main():
    #This line shows a counter variable going to be used
    counter = 0  
    sleep(2)
    
    function0 = GPIO.gpio_function(29)
    
    print(function0)
    
    function1 = GPIO.gpio_function(33)
    
    print(function1)
    
    while True:

        if GPIO.event_detected(29): #incrementing the LEDs by 1
            
        counter=counter + 1
        
        if counter ==8:
            
            counter=0

        print(counterList[counter])

        GPIO.output(outputpin, listCounter[counter])
        
        sleep(.2)
        
        if GPIO.event_detected(31):  #decrementing the LEDs by 1

            counter-=1

            if counter ==-1:
                
                counter=7
                
            print(listCounter[counter])
            
            GPIO.output(outputpin, listCounter[counter])
            
            sleep(.2)
        sleep(2)    