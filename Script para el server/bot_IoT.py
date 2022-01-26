# Importamos paquetes que necesitamos
import os
import tweepy
import requests
import time


#toquen para enviar al bot y conectar con twitter
CONSUMER_KEY=''
CONSUMER_SECRET=''
ACCESS_TOKEN=''
ACCESS_TOKEN_SECRET=''

def consultaDeDatos():
    # Consulta los datos del sensor en la IP del Wemos
    response = requests.get('http://192.168.0.24:80')
    response2 = requests.get('http://192.168.0.27:80')

    # Convierte la respuesta del servidor de Wemos en un diccionario de Python
    sensor_data = response.json()
    sensor_data2 = response2.json()
    
    temperature = sensor_data['variables']['temperature']

    humidity = sensor_data['variables']['humidity']
    pollution = sensor_data['variables']['contaminacion']

    temperature2 = sensor_data2['variables']['temperature']
    humidity2 = sensor_data2['variables']['humidity']
    pollution2 = sensor_data2['variables']['contaminacion']


def guardarDatosOutdoor():
    sensor_outdoor = "C:\\Users\\" + os.getlogin() + "\\Desktop\\"
    a = open(sensor_outdoor + "Datos obtenidos de NodeMCU exterior.txt", "w")
    a.write("\n".join(sensor_outdoor))
    a.close()

def guardarDatosIndoor():
    sensor_indoor= "C:\\Users\\" + os.getlogin() + "\\Desktop\\"
    a = open(sensor_indoor + "Datos obtenidos de NodeMCU interior.txt", "w")
    a.write("\n".join(sensor_indoor))
    a.close()


def main():
    pass


if __name__ == "__main__":
    main()

