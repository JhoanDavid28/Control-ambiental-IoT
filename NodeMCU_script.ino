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

//ejecucion, y script para probar conexión
void setup(){
    Serial.begin(9600); //ambos sensores funcionan a 9600 baudios
    dht.begin();//iniciamos el sensor DHT22

//inicialicacion de variables para la API (se genera el formato JSON)
    rest.variable("temperature",&temperature);
    rest.variable("humidity",&humidity);
    rest.variable("contaminacion",&mq);

//Name ID
    rest.set_id("0");
    rest.set_name("sensor_outdoor");

//Conectar al WiFi
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED){  // WL_CONNECTED: asignado cuando se conecta a una red WiFi
        delay(500); //0,5 segundos
        Serial.print(".");
    }
    Serial.println("");
    Serial.println("WiFi Conectado!");

//Empezar Server
    server.begin();
    Serial.println("Servidor Iniciado");

//visualizacion de  IP
    Serial.println(WiFi.localIP());
}

void loop(){
  //sensado de 1s
    delay(100);
    mq = analogRead(MQ); //MQ135 ppm(particulas por millón)
    humidity = dht.readHumidity(); //RH (humedad relativa 0% -100%(punto de rocio) ) 
    temperature = dht.readTemperature(); //0 - 100°C

//llamadas de Api REST
    WiFiClient client = server.available();
    if (!client) {
    return;
    }

    while(!client.available()){
    delay(1);
    }
    rest.handle(client);

}
