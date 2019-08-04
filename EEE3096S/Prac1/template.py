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
# import Librares that are relevant
import RPi.GPIO as GPIO

from time import sleep

from itertools import product

#LEDs pin out for board
outputpin = [13, 31, 37] 

#pin out for the button pins
inputpin = [15, 29] 

# outputs showing the list for the 3-bit counter
listcount = list(product([0,1], repeat=3))


#This is where the main function starts
def main():
    
    #This line shows a count variable going to be used
    count = 0  
    sleep(2)
    
    function0 = GPIO.gpio_function(29)
    print(function0)
    
    function1 = GPIO.gpio_function(33)
    print(function1)
    
    while True:

        if GPIO.event_detected(29): #incrementing the LEDs by one
            count = count + 1
        
        if count == 8:
            
            count = 0

        print(counterList[count])

        GPIO.output(outputpin, listcount[count])
        
        sleep(.2)
        
        if GPIO.event_detected(31):  #decrementing the LEDs by one, opposing the previous command

            count-=1

            if count == -1:
                
                count = 7
                
            print(listcount[count])
            
            GPIO.output(outputpin, listcount[count])
            sleep(.2)
            
        sleep(2) 

if __name__ == "__main__":
    
    try:
        GPIO.setmode(GPIO.BOARD)  #This line is initialising mode out of main loop
        GPIO.setup(outputpin, GPIO.OUT, initial=GPIO.LOW)

        #The following line shows a list of GPIO set to input
        GPIO.setup(inputpin, GPIO.IN)
        GPIO.setup(inputpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        #The following lines we are adding edge detection as well as debouncing
        GPIO.add_event_detect(15, GPIO.RISING, bouncetime=300)
        GPIO.add_event_detect(29, GPIO.RISING, bouncetime=300)

        while True:
            main()
    except KeyboardInterrupt:
        
        print("Exiting gracefully")
        # The following line turns off the LEDs by cleaning up
        GPIO.cleanup()
        
    except Exception as e:
        
        GPIO.cleanup()
        
        print("Some other error occurred")#printing error message
        
        print(e.message)