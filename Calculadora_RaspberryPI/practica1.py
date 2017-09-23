from time import sleep 
import RPi.GPIO as GPIO #Libreria GPIO
GPIO.setmode(GPIO.BOARD) #Configuracion de puertos
GPIO.setwarnings(False)

pinlist =(7,11,13,15,29,31,33,37)#Tupla que contiene puertos GPIO

#Inicializacion de puertos como salida
for i in pinlist: 
	GPIO.setup(i,GPIO.OUT)
#inicializacion de GPIO apagados
for i in pinlist:
	GPIO.output(i,False)

while 1==1:
    
#Solicitud de operacion al usuario por pantalla
    print (" Inserte el primer numero de la operacion: ")
    num1= input()
    print (" Inserte un operando: ")
    op= raw_input() #Lectura de dato tipo String
    print (" Inserte el segundo numero de la operacion: ")
    num2= input()

#Condiciones para ejecutar operacion
    if op == "+" :
        res = float(num1)+float(num2)
    elif op == "-" :
        res = float(num1)-float(num2)
    elif op == "x" :
        res = float(num1)*float(num2)
    elif op == "/":
        res = float(num1)/float(num2)


    if res > 255 or int(res)!= res : #Validacion del resultado
        print( " operacion no valida ")
	sleep(3)
    else:
        res= int (res) 
        for i in pinlist:
            GPIO.output( i, (res % 2) ) #Salida digital
            res=res//2
	sleep(3) #Espera
           
        
    
    
