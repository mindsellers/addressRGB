import time
import neopixel
from machine import Pin
from random import randint
np = neopixel.NeoPixel(machine.Pin(0), 5)
br_max=90
br_min=10
g_max=50
g_min=12
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
        time.sleep_ms(randint(10,200))
    #time.sleep(1)
