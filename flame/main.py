import time
import neopixel
from machine import Pin
from random import randint
import time
#длина ленты
length=100
#номер пина подключения
pin_num=2
#номер пина кнопки
but_pin_num=15
button=Pin(but_pin_num,Pin.IN)
np = neopixel.NeoPixel(machine.Pin(pin_num), length)
#Задаем всем диодам красный
color=[]
massive=[]
for i in range(0,length):
    np[i]=[255,0,0]
    massive.append([255,0,0])
#шаг изменения
step=255*6//length + 1
#задержка
wait=2
button_wait=5
sleep_counter=0
button_counter=0
long_button_counter=0
long_button_wait=50

br_max=90
br_min=10
g_max=50
g_min=12
br_step_max=5
g_step_max=5
r=255
g=32
b=0
gm=[32]
br = [30]
br_way=[1]
way=[1]
for i in range(0,length):
    gm.append(randint(g_min,g_max))
    br.append(randint(br_min,br_max))
    br_way.append(1)
    way.append(1)

def white(massive):
    for i in range(0,length):
        massive[i]=[200,200,200]
    return massive

def magenta(massive):
    for i in range(0,length):
        massive[i]=[200,0,200]
    return massive

def magenta_wave(massive):
    for i in range(0,length):
        br=randint(br_min,br_max)
        all_col=200*br//100
        massive[i]=[all_col,0,all_col]
    return massive

def fiolet(massive):
    for i in range(0,length):
        massive[i]=[128,0,255]
    return massive

def fiolet_wave(massive):
    for i in range(0,length):
        br=randint(br_min,br_max)
        massive[i]=[128*br//100,0,255*br//100]
    return massive

def randomized(massive):
    for i in range(0,length):
        massive[i]=[randint(20,240),randint(20,240),randint(20,240)]
    return massive

def white_wave(massive):
    for i in range(0,length):
        br=randint(br_min,br_max)
        all_col=255*br//100
        massive[i]=[all_col,all_col,all_col]
    return massive

def red_wave(massive):
    for i in range(0,length):
        br=randint(br_min,br_max)
        all_col=255*br//100
        massive[i]=[all_col,0,0]
    return massive

def green_wave(massive):
    for i in range(0,length):
        br=randint(br_min,br_max)
        all_col=255*br//100
        massive[i]=[0,all_col,0]
    return massive

def blue_wave(massive):
    for i in range(0,length):
        br=randint(br_min,br_max)
        all_col=255*br//100
        massive[i]=[0,0,all_col]
    return massive


def flame(massive):
    massive=[]
    for i in range(1,length+1):
        br=randint(br_min,br_max)
        g=randint(g_min,g_max)
        color = [(r*br)//100, (g*br)//100, 0]
        massive.append(color)
    return massive
    
def rainbow(massive):
        massive=massive
        for i in range(0,length):
            #Выбираем текущие цвета
            red,green,blue = massive[i]

            if red==green==blue==0:
                red=255
                green=i*step
        
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
            massive[j]=[red,green,blue]

        return massive




    

effects_max=12
active_effect=2
cur_counter=0

      

effects={1:rainbow,2:flame,3:white,4:magenta,5:fiolet,6:randomized,7:white_wave,8:red_wave,9:green_wave,10:blue_wave,11:magenta_wave,12:fiolet_wave}

while True:
    time.sleep(0.01)
    
    if button.value()==1:
            button_counter+=1
            print("HOLD")
            if button_counter > 10000:
                button_counter = 0
                print("DROP COUNTER")

            if button_counter > long_button_wait:
                wait=wait*2
                button_counter = 0
                if wait >256: wait = 2
                print("LONG PRESS")
                long_pressed=True

    else:                         
            if button_counter > button_wait and button_counter < long_button_wait and not long_pressed:
                print("BUTTON PRESSED")
                
                active_effect+=1
                for i in range(0,length):
                    np[i]=[0,0,0]
                    massive[i]=[0,0,0]
                if active_effect>effects_max: active_effect=1

            button_counter=0
            long_pressed=False
    if sleep_counter < wait:    
        sleep_counter +=1
        #some button code
#        print(button.value())
                   
    else:
        sleep_counter=0

        massive=effects[active_effect](massive)

        for i in range(0, length):
            np[i]=massive[i]
#            print(np[i])
        np.write()



