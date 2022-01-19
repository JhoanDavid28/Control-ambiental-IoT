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



