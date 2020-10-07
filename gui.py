#!/usr/bin/env python3

from tkinter import *
import tkinter.font as tkFont
import RPi.GPIO as GPIO
import time
import serial

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600)
    timeout=3
    
root = Tk() #Fenster erstellen
root.wm_title("Raspberry Pi GUI") #Fenstertitel
root.config(background = "#FFFFFF") #Hintergrundfarbe
root.attributes("-fullscreen", True)

rootHeight = root.winfo_height()
rootWidth = root.winfo_width()
myFont = tkFont.Font(family="Times New Roman", size=15)
myFontSmall = tkFont.Font(family="Times New Roman", size=10)

coinText5=StringVar()
coinText10=StringVar()
coinText20=StringVar()
coinText50=StringVar()
coinText100=StringVar()
coinText200=StringVar()
coinText500=StringVar()

coinError=StringVar()

count=0
counter=0

root.bind("<Return>", lambda e: root.destroy())

with open("/home/pi/Desktop/def/coins.txt", "r") as data:
    for line in data:
        a,b,c,d,e,f,g = line.strip().split()
        c1 = int(a)
        c2 = int(b)
        c3 = int(c)
        c4 = int(d)
        c5 = int(e)
        c6 = int(f)
        c7 = int(g)
        
coinText5.set(c1)
coinText10.set(c2)
coinText20.set(c3)
coinText50.set(c4)
coinText100.set(c5)
coinText200.set(c6)
coinText500.set(c7)

coinError5 = "Nicht genügend 5 Räppler vorhanden!"
coinError10 = "Nicht genügend 10 Räppler vorhanden!"
coinError20 = "Nicht genügend 20 Räppler vorhanden!"
coinError50 = "Nicht genügend 50 Räppler vorhanden!"
coinError100 = "Nicht genügend 1 Fränkler vorhanden!"
coinError200 = "Nicht genügend 2 Fränkler vorhanden!"
coinError500 = "Nicht genügend 5 Fränkler vorhanden!"

coinError.set("Willkommen! Warte auf Anweisungen...")
 
            
#Funktionen
def aus5(x):
    global c1
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    s5 = GPIO.PWM(11,50)
    s5.start(7.4)
    for i in range(x):
        s5.ChangeDutyCycle(7.8)
        time.sleep(0.05)
        s5.ChangeDutyCycle(5.5)
        time.sleep(0.15)
        s5.ChangeDutyCycle(7.4)
        time.sleep(0.15)
        c1=c1-1
        coinText5.set(c1)
        root.update()
    GPIO.cleanup()
def aus10(x):
    global c2
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13,GPIO.OUT)
    s10 = GPIO.PWM(13,50)
    s10.start(7)
    for i in range(x):
        s10.ChangeDutyCycle(7.4)
        time.sleep(0.05)
        s10.ChangeDutyCycle(5.6)
        time.sleep(0.15)
        s10.ChangeDutyCycle(7)
        time.sleep(0.15)
        c2=c2-1
        coinText10.set(c2)
        root.update()
    GPIO.cleanup()
def aus20(x):
    global c3
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(15,GPIO.OUT)
    s20 = GPIO.PWM(15,50)
    s20.start(7.2)
    for i in range(x):
        s20.ChangeDutyCycle(7.6)
        time.sleep(0.05)
        s20.ChangeDutyCycle(5.8)
        time.sleep(0.15)
        s20.ChangeDutyCycle(7.2)
        time.sleep(0.15)
        c3=c3-1
        coinText20.set(c3)
        root.update()
    GPIO.cleanup()
def aus50(x):
    global c4
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12,GPIO.OUT)
    s50 = GPIO.PWM(12,50)
    s50.start(8.3)
    for i in range(x):
        s50.ChangeDutyCycle(8.)
        time.sleep(0.05)
        s50.ChangeDutyCycle(6.9)
        time.sleep(0.15)
        s50.ChangeDutyCycle(8.3)
        time.sleep(0.15)
        c4=c4-1
        coinText50.set(c4)
        root.update()
    GPIO.cleanup()
def aus100(x):
    global c5
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16,GPIO.OUT)
    s100 = GPIO.PWM(16,50)
    s100.start(7.2)
    for i in range(x):
        s100.ChangeDutyCycle(7.6)
        time.sleep(0.05)
        s100.ChangeDutyCycle(5.6)
        time.sleep(0.15)
        s100.ChangeDutyCycle(7.2)
        time.sleep(0.15)
        c5=c5-1
        coinText100.set(c5)
        root.update()
    GPIO.cleanup()
def aus200(x):
    global c6
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(18,GPIO.OUT)
    s200 = GPIO.PWM(18,50)
    s200.start(7.2)
    for i in range(x):
        s200.ChangeDutyCycle(7.6)
        time.sleep(0.05)
        s200.ChangeDutyCycle(5.6)
        time.sleep(0.15)
        s200.ChangeDutyCycle(7.2)
        time.sleep(0.15)
        c6=c6-1
        coinText200.set(c6)
        root.update()
    GPIO.cleanup()
def aus500(x):
    global c7
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(22,GPIO.OUT)
    s500 = GPIO.PWM(22,50)
    s500.start(7)
    for i in range(x):
        s500.ChangeDutyCycle(7.4)
        time.sleep(0.05)
        s500.ChangeDutyCycle(5.2)
        time.sleep(0.15)
        s500.ChangeDutyCycle(7)
        time.sleep(0.15)
        c7=c7-1
        coinText500.set(c7)
        root.update()
    GPIO.cleanup()

def getGo():
    m5=int(slider5.get())
    m10=int(slider10.get())
    m20=int(slider20.get())
    m50=int(slider50.get())
    m100=int(slider100.get())
    m200=int(slider200.get())
    m500=int(slider500.get())
    #print(m5,m10,m20,m50,m100,m200,m500)
    if c1-m5<0:
        coinError.set(coinError5)
    elif c2-m10<0:
        coinError.set(coinError10)
    elif c3-m20<0:
        coinError.set(coinError20)
    elif c4-m50<0:
        coinError.set(coinError50)
    elif c5-m100<0:
        coinError.set(coinError100)
    elif c6-m200<0:
        coinError.set(coinError200)
    elif c7-m500<0:
        coinError.set(coinError500)
    else:
        coinError.set("Münzausgabe gestartet!")
        if m500 > 0:
            aus500(m500)
        if m200 > 0:
            aus200(m200)
        if m100 > 0:
            aus100(m100)
        if m20 > 0:
            aus20(m20)
        if m10 > 0:
            aus10(m10)
        if m50 > 0:
            aus50(m50)
        if m5 > 0:
            aus5(m5)
        dataFile = open("/home/pi/Desktop/def/coins.txt", "w")
        s1 = str(c1)
        s2 = str(c2)
        s3 = str(c3)
        s4 = str(c4)
        s5 = str(c5)
        s6 = str(c6)
        s7 = str(c7)
        dataFile.write(s1 + " ")
        dataFile.write(s2 + " ")
        dataFile.write(s3 + " ")
        dataFile.write(s4 + " ")
        dataFile.write(s5 + " ")
        dataFile.write(s6 + " ")
        dataFile.write(s7)
        dataFile.flush()
        coinError.set("Münzausgabe abgeschlossen!")
    
    
def cStart():
    global count
    global counter
    coinError.set("Sortiervorgang gestartet!")
    ser.write(b"Go\n")
    count = 1
    counter = 0
    countings()
    
    
    
def cStop():
    global count
    global counter
    coinError.set("Sortiervorgang abgebrochen!")
    ser.write(b"Stop\n")
    count = 0
    counter = 0
    
##def close():
##    root.destroy()
    
#Hier kommen die Elemente hin
top = Frame(root)
top.grid(row=0,column=0,pady=2)

middle = Frame(root)
middle.grid(row=1,column=0,pady=2)
middle.configure(bg="white")

bottom = Frame(root)
bottom.grid(row=2,column=0,pady=2)
bottom.configure(bg="white")

errorTextfeld = Frame(top)
errorTextfeld.grid(row=0, column=0, padx=10, pady=10)
errorTextfeld.configure(bg="white")
Label(errorTextfeld, textvariable=coinError, bg="white", font=myFont).grid(row=0, column=0, padx=2, pady=10)

#shutdown = Button(top, text="close", bg="#00FFFF", width=20, height=1, command=close, font=myFontSmall)
#shutdown.grid(row=0, column=1, padx=10, pady=10)

kontostand = Frame(middle)
kontostand.grid(row=0, column=0, padx=50, pady=5)
kontostand.configure(bg="white")
#image1 = PhotoImage(file = "bsp1")
#Label(kontostand, image=image1).grid(row=x,column=x,padx=x,pady=y)
Label(kontostand, textvariable=coinText5, bg="white", font=myFontSmall).grid(row=0, column=0, pady=14)
Label(kontostand, text="x 5 Rappen", bg="white", font=myFontSmall).grid(row=0, column=1, pady=14)
Label(kontostand, textvariable=coinText10, bg="white", font=myFontSmall).grid(row=1, column=0, pady=14)
Label(kontostand, text="x 10 Rappen", bg="white", font=myFontSmall).grid(row=1, column=1, pady=14)
Label(kontostand, textvariable=coinText20, bg="white", font=myFontSmall).grid(row=2, column=0, pady=15)
Label(kontostand, text="x 20 Rappen", bg="white", font=myFontSmall).grid(row=2, column=1, pady=15)
Label(kontostand, textvariable=coinText50, bg="white", font=myFontSmall).grid(row=3, column=0, pady=15)
Label(kontostand, text="x 50 Rappen", bg="white", font=myFontSmall).grid(row=3, column=1, pady=15)
Label(kontostand, textvariable=coinText100, bg="white", font=myFontSmall).grid(row=4, column=0, pady=15)
Label(kontostand, text="x 1 Franken", bg="white", font=myFontSmall).grid(row=4, column=1, pady=15)
Label(kontostand, textvariable=coinText200, bg="white", font=myFontSmall).grid(row=5, column=0, pady=14)
Label(kontostand, text="x 2 Franken", bg="white", font=myFontSmall).grid(row=5, column=1, pady=14)
Label(kontostand, textvariable=coinText500, bg="white", font=myFontSmall).grid(row=6, column=0, pady=14)
Label(kontostand, text="x 5 Franken", bg="white", font=myFontSmall).grid(row=6, column=1, pady=14)



ausgabe = Frame(middle)
ausgabe.configure(bg="white")
ausgabe.grid(row=0, column=1, pady=5)
Label(ausgabe, text="5 Rappen", bg="white", font=myFontSmall).grid(row=0, column=0, padx=2, pady=10)
slider5 = Scale(ausgabe, from_=0, to=50, resolution=1, orient=HORIZONTAL, length= 300, width=13, borderwidth=1, font=myFontSmall)
slider5.grid(row=0, column=1, padx=10, pady=5)
Label(ausgabe, text="10 Rappen", bg="white", font=myFontSmall).grid(row=1, column=0, padx=2, pady=10)
slider10 = Scale(ausgabe, from_=0, to=50, resolution=1, orient=HORIZONTAL, length=300, width=13, borderwidth=1, font=myFontSmall)
slider10.grid(row=1, column=1, padx=10, pady=5)
Label(ausgabe, text="20 Rappen", bg="white", font=myFontSmall).grid(row=2, column=0, padx=2, pady=10)
slider20 = Scale(ausgabe, from_=0, to=50, resolution=1, orient=HORIZONTAL, length=300, width=13, borderwidth=1, font=myFontSmall)
slider20.grid(row=2, column=1, padx=10, pady=5)
Label(ausgabe, text="50 Rappen", bg="white", font=myFontSmall).grid(row=3, column=0, padx=2, pady=10)
slider50 = Scale(ausgabe, from_=0, to=50, resolution=1, orient=HORIZONTAL, length=300, width=13, borderwidth=1, font=myFontSmall)
slider50.grid(row=3, column=1, padx=10, pady=5)
Label(ausgabe, text="1 Franken", bg="white", font=myFontSmall).grid(row=4, column=0, padx=2, pady=10)
slider100 = Scale(ausgabe, from_=0, to=50, resolution=1, orient=HORIZONTAL, length=300, width=13, borderwidth=1, font=myFontSmall)
slider100.grid(row=4, column=1, padx=10, pady=5)
Label(ausgabe, text="2 Franken", bg="white", font=myFontSmall).grid(row=5, column=0, padx=2, pady=10)
slider200 = Scale(ausgabe, from_=0, to=50, resolution=1, orient=HORIZONTAL, length=300, width=13, borderwidth=1, font=myFontSmall)
slider200.grid(row=5, column=1, padx=10, pady=5)
Label(ausgabe, text="5 Franken", bg="white", font=myFontSmall).grid(row=6, column=0, padx=2, pady=10)
slider500 = Scale(ausgabe, from_=0, to=50, resolution=1, orient=HORIZONTAL, length=300, width=13, borderwidth=1, font=myFontSmall)
slider500.grid(row=6, column=1, padx=10, pady=5)

buttons = Frame(bottom)
buttons.grid(row=0, column=0, pady=2)
buttons.configure(bg="white")
go = Button(buttons, text="Münzausgabe starten", bg="#00FFFF", width=20, height=1, command=getGo, font=myFontSmall)
go.grid(row=8, column=2, padx=40, pady=5)
countStart = Button(buttons, text="Sortiervorgang starten", bg="#00FFFF", width=20, height=1, command=cStart, font=myFontSmall)
countStart.grid(row=8, column=0, padx=40, pady=5)
countStop = Button(buttons, text="Sortiervorgang abbrechen", bg="#00FFFF", width=20, height=1, command=cStop, font=myFontSmall)
countStop.grid(row=8, column=1, padx=40, pady=5)


def countings():
    global counter
    global count
    global c1
    global c2
    global c3
    global c4
    global c5
    global c6
    global c7
    while count == 1:
        dataFile = open("/home/pi/Desktop/def/coins.txt", "w")
        arduinoData = ser.readline().decode().strip()
        coin = str(arduinoData)
        if coin == "0" or coin == "1" or coin == "2" or coin == "3" or coin == "4" or coin == "5" or coin == "6" or coin == "7" : 
            if coin == "1":
                c1=c1+1
                counter=0
            elif coin == "2":
                c2=c2+1
                counter=0
            elif coin == "3":
                c3=c3+1
                counter=0
            elif coin == "4":
                c4=c4+1
                counter=0
            elif coin == "5":
                c5=c5+1
                counter=0
            elif coin == "6":
                c6=c6+1
                counter=0
            elif coin == "7":
                c7=c7+1
                counter=0
            elif coin == "0":
                counter=counter+1
            print(coin, c1, c2, c3, c4, c5, c6, c7)
            s1 = str(c1)
            s2 = str(c2)
            s3 = str(c3)
            s4 = str(c4)
            s5 = str(c5)
            s6 = str(c6)
            s7 = str(c7)
            dataFile.write(s1 + " ")
            dataFile.write(s2 + " ")
            dataFile.write(s3 + " ")
            dataFile.write(s4 + " ")
            dataFile.write(s5 + " ")
            dataFile.write(s6 + " ")
            dataFile.write(s7)
            dataFile.flush()
            coinText5.set(c1)
            coinText10.set(c2)
            coinText20.set(c3)
            coinText50.set(c4)
            coinText100.set(c5)
            coinText200.set(c6)
            coinText500.set(c7)
            root.update()
            if counter > 20:
                ser.write(b"Stop\n")
                count = 0
                counter = 0
                coinError.set("Sortiervorgang abgeschlossen!")
                break
            
    


root.mainloop() #GUI wird geupdatet