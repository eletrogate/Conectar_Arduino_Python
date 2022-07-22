'''
 Blog Eletrogate - Como conectar o Arduino com Python
 Miguel Sena
 blog.eletrogate.com
'''

import serial #Importa a biblioteca

while True: #Loop para a conexão com o Arduino
    try:  #Tenta se conectar, se conseguir, o loop se encerra
        arduino = serial.Serial('COM4', 9600)
        print('Arduino conectado')
        break

    except:
        pass

while True: #Loop principal
    msg = str(arduino.readline()) #Lê os dados em formato de string
    msg = msg[2:-5] #Fatia a string
    print(msg) #Imprime a mensagem

    arduino.flush() #Limpa a comunicação