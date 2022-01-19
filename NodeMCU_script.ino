// Librerias
#include "ESP8266WiFi.h"
#include <aREST.h>
#include <DHT.h>
#include <DHT_U.h>
// Libreia master 
#include <Adafruit_Sensor.h>

// Definir las entradas
#define DHTPIN D2
#define DHTTYPE DHT22
#define MQ A0

// inicializamos las entradas del sensor DHT
DHT dht(DHTPIN, DHTTYPE);

// inicializamos la API
aREST rest = aREST();

// ingresamos credenciales de wifi
const char* ssid = "Tu Wifi";
const char* password = "Tu contraseña";

// Definir puerto que debe estar escuchando la apí
#define LISTEN_PORT 80

//Creación de la instancia del servidor
WiFiServer server(LISTEN_PORT);

//Variables API
float mq, humidity, temperature;


