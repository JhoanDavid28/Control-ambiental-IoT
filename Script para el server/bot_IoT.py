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

#IP de los sensores en red local
IP_SENSOR_OUTDOOR = 'http://192.168.0.24:80'
IP_SENSOR_INDOOR = 'http://192.168.0.27:80'

def obtenerDatosDeSensorOutdoor():
    # Consulta los datos del sensor en la IP del Wemos
    response = requests.get(IP_SENSOR_OUTDOOR)
    # Convierte la respuesta del servidor de NodeMCU en un diccionario de Python
    sensor_data = response.json()
    
    temperature = sensor_data['variables']['temperature']
    humidity = sensor_data['variables']['humidity']
    pollution = sensor_data['variables']['contaminacion']


def obtenerDatosDeSensorIndoor():
    # Consulta los datos del sensor en la IP del Wemos
    response = requests.get(IP_SENSOR_OUTDOOR)

    # Convierte la respuesta del servidor de NodeMCU en un diccionario de Python
    sensor_data = response.json()
    
    temperature = sensor_data['variables']['temperature']
    humidity = sensor_data['variables']['humidity']
    pollution = sensor_data['variables']['contaminacion']


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
    obtenerDatosDeSensorIndoor()
    obtenerDatosDeSensorOutdoor()


if __name__ == "__main__":
    main()

