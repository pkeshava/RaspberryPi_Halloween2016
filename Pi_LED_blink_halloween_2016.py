# script to blink LED's two at a time like eyes for Bryce and Naz's bush outside during halloween

import time
#GPIOs that are available
#0,1,2,3,4,7,8,9,10,11,14,15,17,18,21,22,23,24,25,27
#Map
#6 pairs of red
#5 pairs of yellow
#3 pairs of green
#1 pair of blue
#Use the following GPIOs for LEDs
GPIO_redeyes1 = '24'
GPIO_redeyes2 = '25'
GPIO_redeyes3 = '2'
GPIO_redeyes4 = '3'
GPIO_redeyes5 = '4'
GPIO_redeyes6 = '7'
GPIO_yelloweyes1 = '8'
GPIO_yelloweyes2 = '9'
GPIO_yelloweyes3 = '10'
GPIO_yelloweyes4 = '11'
GPIO_yelloweyes5 = '14'
GPIO_greeneyes1 = '15'
GPIO_greeneyes2 = '17'
GPIO_greeneyes3 = '18'
GPIO_blueeyes1 = '21'
#GPIO_greeneyesX = '22'
#GPIO_blueeyesXX = '23'
#GPIO_blueeyesXXX = '24'
#GPIO_blueeyesXXXX = '25'
#GPIO_blueeyesXXXXX = '27'


try:
    f= open ('/sys/class/gpio/unexport','w')
    f.write(str(GPIO_redeyes1))
    f.write(str(GPIO_redeyes2))
    f.write(str(GPIO_redeyes3))
    f.write(str(GPIO_redeyes4))
    f.write(str(GPIO_redeyes5))
    f.write(str(GPIO_redeyes6))
    f.write(str(GPIO_yelloweyes1))
    f.write(str(GPIO_yelloweyes2))
    f.write(str(GPIO_yelloweyes3))
    f.write(str(GPIO_yelloweyes4))
    f.write(str(GPIO_yelloweyes5))
    f.write(str(GPIO_greeneyes1))
    f.write(str(GPIO_greeneyes2))
    f.write(str(GPIO_greeneyes3))
    f.write(str(GPIO_blueeyes1))
    f.close()
except IOError as e:
    lol=0

#Export pin number
f= open ('/sys/class/gpio/export','w')
f.write(str(GPIO_redeyes1))
f.write(str(GPIO_redeyes2))
f.write(str(GPIO_redeyes3))
f.write(str(GPIO_redeyes4))
f.write(str(GPIO_redeyes5))
f.write(str(GPIO_redeyes6))
f.write(str(GPIO_yelloweyes1))
f.write(str(GPIO_yelloweyes2))
f.write(str(GPIO_yelloweyes3))
f.write(str(GPIO_yelloweyes4))
f.write(str(GPIO_yelloweyes5))
f.write(str(GPIO_greeneyes1))
f.write(str(GPIO_greeneyes2))
f.write(str(GPIO_greeneyes3))
f.write(str(GPIO_blueeyes1))
f.close()

#Define Pin Direction as Output for LED
path = '/sys/class/gpio/gpio' + GPIO_redeyes1 + '/direction'
f= open (path,'w')
f.write('out')
f.close()
path = '/sys/class/gpio/gpio' + GPIO_redeyes2 + '/direction'
f= open (path,'w')
f.write('out')
f.close()
path = '/sys/class/gpio/gpio' + GPIO_redeyes3 + '/direction'
f= open (path,'w')
f.write('out')
f.close()
path = '/sys/class/gpio/gpio' + GPIO_redeyes4 + '/direction'
f= open (path,'w')
f.write('out')
f.close()
path = '/sys/class/gpio/gpio' + GPIO_redeyes5 + '/direction'
f= open (path,'w')
f.write('out')
f.close()
path = '/sys/class/gpio/gpio' + GPIO_redeyes6 + '/direction'
f= open (path,'w')
f.write('out')
f.close()
path = '/sys/class/gpio/gpio' + GPIO_yelloweyes1 + '/direction'
f= open (path,'w')
f.write('out')
f.close()
path = '/sys/class/gpio/gpio' + GPIO_yelloweyes2 + '/direction'
f= open (path,'w')
f.write('out')
f.close()
path = '/sys/class/gpio/gpio' + GPIO_yelloweyes3 + '/direction'
f= open (path,'w')
f.write('out')
f.close()
path = '/sys/class/gpio/gpio' + GPIO_yelloweyes4 + '/direction'
f= open (path,'w')
f.write('out')
f.close()
path = '/sys/class/gpio/gpio' + GPIO_yelloweyes5 + '/direction'
f= open (path,'w')
f.write('out')
f.close()
path = '/sys/class/gpio/gpio' + GPIO_greeneyes1 + '/direction'
f= open (path,'w')
f.write('out')
f.close()
path = '/sys/class/gpio/gpio' + GPIO_greeneyes2 + '/direction'
f= open (path,'w')
f.write('out')
f.close()
path = '/sys/class/gpio/gpio' + GPIO_greeneyes3 + '/direction'
f= open (path,'w')
f.write('out')
f.close()
path = '/sys/class/gpio/gpio' + GPIO_blueeyes1 + '/direction'
f= open (path,'w')
f.write('out')
f.close()

while(1):
    #set1
    path = '/sys/class/gpio/gpio' + GPIO_redeyes1 + '/value'
    f= open (path,'w')
    f.write('1')
    f.close()
    path = '/sys/class/gpio/gpio' + GPIO_yelloweyes1 + '/value'
    f= open (path,'w')
    f.write('1')
    f.close()
    path = '/sys/class/gpio/gpio' + GPIO_greeneyes1 + '/value'
    f= open (path,'w')
    f.write('1')
    f.close()
    time.sleep(4)
    path = '/sys/class/gpio/gpio' + GPIO_redeyes1 + '/value'
    f= open (path,'w')
    f.write('0')
    f.close()
    path = '/sys/class/gpio/gpio' + GPIO_yelloweyes1 + '/value'
    f= open (path,'w')
    f.write('0')
    f.close()
    path = '/sys/class/gpio/gpio' + GPIO_greeneyes1 + '/value'
    f= open (path,'w')
    f.write('0')
    f.close()
    time.sleep(1)
    #set2
    path = '/sys/class/gpio/gpio' + GPIO_redeyes2 + '/value'
    f= open (path,'w')
    f.write('1')
    f.close()
    path = '/sys/class/gpio/gpio' + GPIO_yelloweyes2 + '/value'
    f= open (path,'w')
    f.write('1')
    f.close()
    path = '/sys/class/gpio/gpio' + GPIO_blueeyes1 + '/value'
    f= open (path,'w')
    f.write('1')
    f.close()
    time.sleep(4)
    path = '/sys/class/gpio/gpio' + GPIO_redeyes2 + '/value'
    f= open (path,'w')
    f.write('0')
    f.close()
    path = '/sys/class/gpio/gpio' + GPIO_yelloweyes2 + '/value'
    f= open (path,'w')
    f.write('0')
    f.close()
    path = '/sys/class/gpio/gpio' + GPIO_blueeyes1 + '/value'
    f= open (path,'w')
    f.write('0')
    f.close()
    time.sleep(1)
    #set3
    path = '/sys/class/gpio/gpio' + GPIO_redeyes3 + '/value'
    f= open (path,'w')
    f.write('1')
    f.close()
    path = '/sys/class/gpio/gpio' + GPIO_redeyes4 + '/value'
    f= open (path,'w')
    f.write('1')
    f.close()
    path = '/sys/class/gpio/gpio' + GPIO_yelloweyes3 + '/value'
    f= open (path,'w')
    f.write('1')
    f.close()
    time.sleep(4)
    path = '/sys/class/gpio/gpio' + GPIO_redeyes3 + '/value'
    f= open (path,'w')
    f.write('0')
    f.close()
    path = '/sys/class/gpio/gpio' + GPIO_redeyes4 + '/value'
    f= open (path,'w')
    f.write('0')
    f.close()
    path = '/sys/class/gpio/gpio' + GPIO_yelloweyes3 + '/value'
    f= open (path,'w')
    f.write('0')
    f.close()
    time.sleep(1)
    #set4
    path = '/sys/class/gpio/gpio' + GPIO_redeyes5 + '/value'
    f= open (path,'w')
    f.write('1')
    f.close()
    path = '/sys/class/gpio/gpio' + GPIO_yelloweyes4 + '/value'
    f= open (path,'w')
    f.write('1')
    f.close()
    path = '/sys/class/gpio/gpio' + GPIO_greeneyes2 + '/value'
    f= open (path,'w')
    f.write('1')
    f.close()
    time.sleep(4)
    path = '/sys/class/gpio/gpio' + GPIO_redeyes5 + '/value'
    f= open (path,'w')
    f.write('0')
    f.close()
    path = '/sys/class/gpio/gpio' + GPIO_yelloweyes4 + '/value'
    f= open (path,'w')
    f.write('0')
    f.close()
    path = '/sys/class/gpio/gpio' + GPIO_greeneyes2 + '/value'
    f= open (path,'w')
    f.write('0')
    f.close()
    time.sleep(1)
    #set 5
    path = '/sys/class/gpio/gpio' + GPIO_redeyes6 + '/value'
    f= open (path,'w')
    f.write('1')
    f.close()
    path = '/sys/class/gpio/gpio' + GPIO_yelloweyes5 + '/value'
    f= open (path,'w')
    f.write('1')
    f.close()
    path = '/sys/class/gpio/gpio' + GPIO_greeneyes3 + '/value'
    f= open (path,'w')
    f.write('1')
    f.close()
    time.sleep(4)
    path = '/sys/class/gpio/gpio' + GPIO_redeyes6 + '/value'
    f= open (path,'w')
    f.write('0')
    f.close()
    path = '/sys/class/gpio/gpio' + GPIO_yelloweyes5 + '/value'
    f= open (path,'w')
    f.write('0')
    f.close()
    path = '/sys/class/gpio/gpio' + GPIO_greeneyes3 + '/value'
    f= open (path,'w')
    f.write('0')
    f.close()
    time.sleep(1)

#Unexport Pin
f= open ('/sys/class/gpio/unexport','w')
f.write(str(GPIO_redeyes1))
f.write(str(GPIO_redeyes2))
f.write(str(GPIO_redeyes3))
f.write(str(GPIO_redeyes4))
f.write(str(GPIO_redeyes5))
f.write(str(GPIO_redeyes6))
f.write(str(GPIO_yelloweyes1))
f.write(str(GPIO_yelloweyes2))
f.write(str(GPIO_yelloweyes3))
f.write(str(GPIO_yelloweyes4))
f.write(str(GPIO_yelloweyes5))
f.write(str(GPIO_greeneyes1))
f.write(str(GPIO_greeneyes2))
f.write(str(GPIO_greeneyes3))
f.write(str(GPIO_blueeyes1))
f.close()
