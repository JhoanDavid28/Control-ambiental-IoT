# Importamos paquetes que necesitamos
import json
import requests
import datetime
import time


#toquen para enviar al bot y conectar con twitter
CONSUMER_KEY=''
CONSUMER_SECRET=''
ACCESS_TOKEN=''
ACCESS_TOKEN_SECRET=''

#IP de los sensores en red local
IP_SENSOR_OUTDOOR = 'http://192.168.101.35:80/'
IP_SENSOR_INDOOR = 'http://192.168.101.36:80/'

mediciones = {}
mediciones2 = {}
a = 0
def obtenerDatosDeSensores():
    while True:
        time.sleep(10)
        # Consulta los datos del sensor en la IP del
        response = requests.get(IP_SENSOR_OUTDOOR)
        # Convierte la respuesta del servidor de NodeMCU en un diccionario de Python
        sensor_data = response.json()
        print(sensor_data)

        response2 = requests.get(IP_SENSOR_INDOOR)
        sensor_data2 = response2.json()
        print(sensor_data2)

        ahora = datetime.datetime.now()
        sensor_data["fecha"] = ahora.strftime('%d/%m/%Y')
        sensor_data["hora"] = ahora.strftime('%H:%M:%S')

        sensor_data2["fecha"] = ahora.strftime('%d/%m/%Y')
        sensor_data2["hora"] = ahora.strftime('%H:%M:%S')

        tf = open("myDictionary_outdoor.json", "w")
        mediciones['dic' + str(a)] = sensor_data
        json.dump(mediciones, tf)
        tf.close()

        tf2 = open("myDictionary2_indoor.json", "w")
        mediciones2['dic' + str(a)] = sensor_data2
        json.dump(mediciones2, tf2)
        tf.close()

        a += 1





def main():
    obtenerDatosDeSensores()


if __name__ == "__main__":
    main()

