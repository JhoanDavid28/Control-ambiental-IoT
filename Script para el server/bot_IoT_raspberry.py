# Importamos paquetes que necesitamos
import json
import requests
import datetime
import time
import tweepy

# toquen para enviar al bot y conectar con twitter
consumer_key = "************"
consumer_secret = "***************"
access_token = "******************"
access_token_secret = "********************"

# IP de los sensores en red local
IP_SENSOR_OUTDOOR = 'IP del sensor outdoor'
IP_SENSOR_INDOOR = 'IP del sensor indoor'

mediciones = {}
mediciones2 = {}


def autenticacionDeLlaves():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api


def obtencionYEnvioDeVariables(api, sensor_data, ahora):
    # obtencion de variables  para sensor outddor para twiteer
    temperatura = sensor_data['variables']['temperature']
    humedad = sensor_data['variables']['humidity']
    contaminacion = sensor_data['variables']['contaminacion']
    hora = ahora.strftime('%H:%M:%S')
    fecha = ahora.strftime('%d/%m/%Y')
    # print(temperatura, humedad, contaminacion, hora, fecha)
    api.update_status(
        'Soy un bot creado para hacer mediciones en la ciudad de Pelileo Centro \n La temperatura es: {0} ℃ \n La '
        'humedad es: {1} % HR \n La concentración de gases es: {2} ppm \n Fecha: {3}, Hora: {4}'.format(
            temperatura, humedad, contaminacion, fecha, hora))


def main():
    a = 0
    api = autenticacionDeLlaves()
    while True:
        time.sleep(10)
        # Consulta los datos del sensor en la IP del NodeMCU
        response = requests.get(IP_SENSOR_OUTDOOR)
        # Convierte la respuesta del servidor de NodeMCU en un diccionario de Python
        sensor_data = response.json()
        # print(sensor_data)

        response2 = requests.get(IP_SENSOR_INDOOR)
        sensor_data2 = response2.json()
        # print(sensor_data2)

        ahora = datetime.datetime.now()
        sensor_data["fecha"] = ahora.strftime('%d/%m/%Y')
        sensor_data["hora"] = ahora.strftime('%H:%M:%S')

        sensor_data2["fecha"] = ahora.strftime('%d/%m/%Y')
        sensor_data2["hora"] = ahora.strftime('%H:%M:%S')

        # almacenamiento de las mediciones
        tf = open("mediciones_outdoor.json", "w")
        mediciones['med' + str(a)] = sensor_data
        json.dump(mediciones, tf)
        tf.close()

        tf2 = open("mediciones_indoor.json", "w")
        mediciones2['med' + str(a)] = sensor_data2
        json.dump(mediciones2, tf2)
        tf2.close()

        # obtencion de datos para tweet
        obtencionYEnvioDeVariables(api, sensor_data, ahora)
        time.sleep(1800)
        a += 1


if __name__ == "__main__":
    main()
