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

//ejecucion, y script para probar conección
void setup(){
    Serial.begin(9600); //ambos sensores funcionan a 9600 baudios
    dht.begin();//iniciamos el sensor DHT22

//inicialicacion de variables para la API (se genera el formato JSON)
    rest.variable("temperature",&temperature);
    rest.variable("humidity",&humidity);
    rest.variable("contaminacion",&mq);

//Name ID
    rest.set_id("0");
    rest.set_name("sensor_nodemcu");

}
