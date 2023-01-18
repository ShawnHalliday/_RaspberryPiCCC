import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)#A
GPIO.setup(19,GPIO.OUT)#F
GPIO.setup(13,GPIO.OUT)#B
GPIO.setup(6,GPIO.OUT)#E
GPIO.setup(5,GPIO.OUT)#D
GPIO.setup(22,GPIO.OUT)#C
GPIO.setup(27,GPIO.OUT)#G
GPIO.setup(21,GPIO.OUT)#DP1
GPIO.setup(20,GPIO.OUT)#DP2
GPIO.setup(16,GPIO.OUT)#DP3
GPIO.setup(12,GPIO.OUT)#DP4
GPIO.setup(18,GPIO.OUT)#DP5
GPIO.setup(15,GPIO.OUT)#DP6
GPIO.setup(14,GPIO.OUT)#DP7
GPIO.setup(7,GPIO.OUT)#DP8
GPIO.setup(4,GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(17,GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23,GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(24,GPIO.IN, pull_up_down = GPIO.PUD_UP)

GPIO.output(21, False)#1
GPIO.output(20, False)#2
GPIO.output(16, False)#3
GPIO.output(12, False)#4
GPIO.output(18, False)#5
GPIO.output(15, False)#6
GPIO.output(14, False)#7
GPIO.output(7, False)#8
GPIO.output(26,True)#A
GPIO.output(13,True)#B
GPIO.output(22,True)#C
GPIO.output(5,True)#D
GPIO.output(6,True)#E
GPIO.output(19,True)#F
GPIO.output(27,True)#G

order = ['A','b','C','d','E']
placeHolder = ''

def A():
    GPIO.output(26,False)#A
    GPIO.output(13,False)#B
    GPIO.output(22,False)#C
    GPIO.output(5,True)#D
    GPIO.output(6,False)#E
    GPIO.output(19,False)#F
    GPIO.output(27,False)#G

def b():
    GPIO.output(26,True)#A
    GPIO.output(13,True)#B
    GPIO.output(22,False)#C
    GPIO.output(5,False)#D
    GPIO.output(6,False)#E
    GPIO.output(19,False)#F
    GPIO.output(27,False)#G


def C():
    GPIO.output(26,False)#A
    GPIO.output(13,True)#B
    GPIO.output(22,True)#C
    GPIO.output(5,False)#D
    GPIO.output(6,False)#E
    GPIO.output(19,False)#F
    GPIO.output(27,True)#G

def d():
    GPIO.output(26,True)#A
    GPIO.output(13,False)#B
    GPIO.output(22,False)#C
    GPIO.output(5,False)#D
    GPIO.output(6,False)#E
    GPIO.output(19,True)#F
    GPIO.output(27,False)#G

def E():
    GPIO.output(26,False)#A
    GPIO.output(13,True)#B
    GPIO.output(22,True)#C
    GPIO.output(5,False)#D
    GPIO.output(6,False)#E
    GPIO.output(19,False)#F
    GPIO.output(27,False)#G

def button2(order):
    defPlaceholder1 = order[0]
    order[0] = order[4]
    defPlaceholder2 = order[1]
    order[1] = defPlaceholder1
    defPlaceholder1 = order[2]
    order[2] = defPlaceholder2
    defPlaceholder2 = order[3]
    order[3] = defPlaceholder1
    defPlaceholder1 = order[4]
    order[4] = defPlaceholder2
    return order

def button1(order):
    defPlaceholder1 = order[4]
    order[4] = order[0]
    order[0] = order[1]
    order[1] = order[2]
    order[2] = order[3]
    order[3] = defPlaceholder1
    return order

def button3(order):
    defPlaceholder1 = order[0]
    order[0] = order[1]
    order[1] = defPlaceholder1
    return order

def displayAll(order):
    GPIO.output(21, True)#1
    if (order[0] == 'A'):
        A()
    elif (order[0] == 'b'):
        b()
    elif (order[0] == 'C'):
        C()
    elif (order[0] == 'd'):
        d()
    elif (order[0] == 'E'):
        E()
    time.sleep(0.003)
    GPIO.output(21, False)#1
    GPIO.output(20, True)#2
    if (order[1] == 'A'):
        A()
    elif (order[1] == 'b'):
        b()
    elif (order[1] == 'C'):
        C()
    elif (order[1] == 'd'):
        d()
    elif (order[1] == 'E'):
        E()
    time.sleep(0.003)
    GPIO.output(20, False)#2
    GPIO.output(16, True)#3
    if (order[2] == 'A'):
        A()
    elif (order[2] == 'b'):
        b()
    elif (order[2] == 'C'):
        C()
    elif (order[2] == 'd'):
        d()
    elif (order[2] == 'E'):
        E()
    time.sleep(0.003)
    GPIO.output(16, False)#3
    GPIO.output(12, True)#4
    if (order[3] == 'A'):
        A()
    elif (order[3] == 'b'):
        b()
    elif (order[3] == 'C'):
        C()
    elif (order[3] == 'd'):
        d()
    elif (order[3] == 'E'):
        E()
    time.sleep(0.003)
    GPIO.output(12, False)#4
    GPIO.output(18, True)#5
    if (order[4] == 'A'):
        A()
    elif (order[4] == 'b'):
        b()
    elif (order[4] == 'C'):
        C()
    elif (order[4] == 'd'):
        d()
    elif (order[4] == 'E'):
        E()
    time.sleep(0.003)
    GPIO.output(18, False)#5

def button4(balls):
    print(order)
    while True:
        displayAll(balls)

try:
    while True:
        button_state1 = GPIO.input(4)
        button_state2 = GPIO.input(17)
        button_state3 = GPIO.input(23)
        button_state4 = GPIO.input(24)
        if button_state1 == False:
            button1(order)
            time.sleep(0.2)
        if button_state2 == False:
            button2(order)
            time.sleep(0.2)
        if button_state3 == False:
            button3(order)
            time.sleep(0.2)
        if button_state4 == False:
            button4(order)
            time.sleep(0.2)
        displayAll(order)
except:
    GPIO.cleanup()