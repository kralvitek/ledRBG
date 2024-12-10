from machine import Pin
from time import sleep

button1 = Pin(3, Pin.IN)
led1 = Pin(0, Pin.OUT)
led2 = Pin(1, Pin.OUT)
led3 = Pin(2, Pin.OUT)


button2 = Pin(4, Pin.IN) 
  
while True:
   print(button1.value())
   print(button2.value())
   
   
   
   
   if button1.value() == 1:
       led1.value(1)
       led2.value(1)
       led3.value(1)
        if button2.value() == 1:
            else:
                    led1.value(0)
                    led2.value(0)
                    led3.value(0)
                sleep(0.1)

     



