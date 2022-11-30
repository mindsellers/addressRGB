import time
import neopixel
from machine import Pin
from random import randint
from time import sleep_ms as sleep
#длина ленты
length=5
#номер пина подключения
pin_num=2
#номер пина кнопки
but_pin_num=15
button=Pin(but_pin_num,Pin.IN)
np = neopixel.NeoPixel(machine.Pin(pin_num), length)
#Задаем всем диодам красный
color=[]
for i in range(0,length):
    np[i]=[255,0,0]
#шаг изменения
step=15
#задержка
wait=80
button_wait=200
sleep_counter=0
button_counter=0
while True:
    sleep(1)
    if sleep_counter < wait:    
        sleep_counter +=1
        #some button code
#        print(button.value())
        if button.value()==1:
            button_counter+=1
        else:
            button_counter = 0
        
        
        if button_counter > button_wait:
            print("BUTTON PRESSED")
            button_counter=0
    else:
        sleep_counter=0

        for i in range(0,length):
            np.write()
            #Выбираем текущие цвета
            red,green,blue = np[i]
            #Последовательно перебираем - 255.0.0 - 255.255.0 - 0.255.0 - 0.255.255 -0.0.255 -255.0.255
            if red >= 255 and green <255 and blue == 0:
                red = 255
                green +=step
                if green >=255: green=255
                blue = 0
            if green >= 255 and red <=255 and blue ==0:
                red -=step
                green = 255
                blue = 0
                if red <=0: red = 0
            
            if green >=255 and red == 0 and blue <=255:
                red=0
                blue += step
                if blue >=255: blue = 255
        
            if blue == 255 and green <=255 and red == 0:
                red=0
                blue = 255
                green -= step
                if green <=0: green=0


            if blue == 255 and red <=255 and green == 0:
                blue = 255
                green = 0
                red += step
                if red >=255: red = 255


            if red == 255 and blue <= 255 and green == 0:
                green = 0
                red = 255
                blue -= step
                if blue <= 0: blue = 0

        #    print(i,red,green,blue)

            if blue <=0: blue = 0

            j=i+1
        #Задаем цвет следующему пикселю
            if j == length: j=0
            np[j]=[red,green,blue]
