import time
import neopixel
from machine import Pin
from random import randint
from time import sleep_ms as sleep
#длина ленты
length=5
#номер пина подключения
pin_num=0
np = neopixel.NeoPixel(machine.Pin(pin_num), length)
#Задаем всем диодам красный
color=[]
for i in range(0,length):
    np[i]=[255,0,0]
#направление изменения цвета    
r_way=0
g_way=1
b_way=0
#шаг изменения
step=50
#задержка
wait=50
while True:
    
    for i in range(0,length):
        np.write()
        red,green,blue = np[i]
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

        print(i,red,green,blue)

        if blue <=0: blue = 0

        j=i+1
        if j == length: j=0
        np[j]=[red,green,blue]
        sleep(wait)

















br_max=90
br_min=10
g_max=50
g_min=5
sleep_max=50
br_step_max=5
g_step_max=5
r=255
g=32
b=0
gm=[32,32,32,32,32]
#for i in range(0,5)
    
br = [30,30,30,30,30]
br_way=[1,1,1,1,1]
way=[1,1,1,1,1]

while True:
    for i in range(0,5):
        color = ((r*br[i])//100,(gm[i]*br[i])//100,b)
        print(br[i],gm[i])
        print(color)
        np[i]=color
        np.write()
        br[i]=br[i]+br_way[i]*randint(0,br_step_max)
        if br[i]<br_min or br[i]>br_max: br_way[i] = -br_way[i]
        if br[i]<=br_min: br[i] = br_min
        if br[i] >= br_max: br[i]=br_max
        gm[i]=gm[i]+way[i]*randint(0,g_step_max)
        
        if gm[i]<g_min or gm[i]>g_max: way[i] = -way[i]
        if gm[i] <=g_min: gm[i] = g_min
        if gm[i] >= g_max: gm[i] = g_max
        time.sleep_ms(randint(10,sleep_max))
    #time.sleep(1)
