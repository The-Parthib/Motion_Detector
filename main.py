from machine import Pin
import time
import urequests as rq
import internet


stat = True

led = Pin(9, Pin.OUT)
led2 = Pin(2, Pin.OUT)
buzzer = Pin(16, Pin.OUT)
motion_sensor = Pin(15, Pin.IN)

def alert_system(state):
    if state == 1:
        for i in range(11):
            led2.value(1)
            buzzer.value(1)
            time.sleep(0.1)
            led2.value(0)
            buzzer.value(0)
            time.sleep(0.1)
            
    else:
        led2.value(0)
        buzzer.value(0)

def sys_on():
    led.value(1)
    time.sleep(0.7)
    led.value(0)
    time.sleep(0.7)

try:
    while True:
        
        if motion_sensor.value() == 1:
            print("Motion detected!")
            
            if stat == True:
                rq.post("https://intruder-alert-system.onrender.com/api/intruder-alert")
                stat = False

            alert_system(1)  
            time.sleep(1)  
        else:
            sys_on()
            alert_system(0)
            stat = True
            
        time.sleep(0.1)  
        
except KeyboardInterrupt:
    print("Program stopped")
    alert_system(0)  




