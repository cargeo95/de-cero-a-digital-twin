// Bibliotecas
#include <Wire.h> // Biblioteca para la comunicación I2C
#include <Adafruit_Sensor.h>
#include <Adafruit_ADXL345_U.h> // Biblioteca para el sensor ADXL345

// Sensor de distancia 1 y 2
const int trigPin_13 = 13; // Pin de trig para el sensor 1
const int echoPin_12 = 12; // Pin de echo para el sensor 1
const int trigPin_8 = 8; // Pin de trig para el sensor 2
const int echoPin_7 = 7; // Pin de echo para el sensor 2

// Sensor de Vibración
const int sensorPin_A0 = A0; // Pin al que está conectada la salida analógica del sensor de vibración
const int sensorPin_A1 = A1; // Pin al que está conectada la salida analógica del sensor de vibración
const int sensorPin_A2 = A2; // Pin al que está conectada la salida analógica del sensor de vibración

// Declaracion de variables
long pingTravelTime_sensor1;
long pingTravelTime_sensor2;
float distance_1;
float distance_2;

// Objeto para manejar el sensor ADXL345
Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified(); // El número opcional es la dirección I2C del sensor, por defecto es 0x53

unsigned long previousMillis = 0;
unsigned long interval = 2000; // Intervalo de tiempo para los sensores de distancia y acelerómetro
float referenceX = 0;
float referenceY = 0;
bool referenceSet = false;

// Variables para almacenar el tiempo de detección de ruido
unsigned long lastNoiseTime_A0 = 0;
unsigned long lastNoiseTime_A1 = 0;
unsigned long lastNoiseTime_A2 = 0;

void setup() {
  Serial.begin(9600);
  pinMode(trigPin_13, OUTPUT);
  pinMode(echoPin_12, INPUT);
  pinMode(trigPin_8, OUTPUT);
  pinMode(echoPin_7, INPUT);

  // Inicializar el sensor ADXL345
  if (!accel.begin()) {
    Serial.println("No se encontró el sensor ADXL345. Verifica la conexión.");
    while (1);
  }
}

void loop() {
  unsigned long currentMillis = millis();

  // SENSOR1
  digitalWrite(trigPin_13, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin_13, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin_13, LOW);

  pingTravelTime_sensor1 = pulseIn(echoPin_12, HIGH);

  // Convertir el tiempo en distancia
  distance_1 = pingTravelTime_sensor1 * 0.0343 / 2;

  // SENSOR 2
  digitalWrite(trigPin_8, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin_8, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin_8, LOW);

  pingTravelTime_sensor2 = pulseIn(echoPin_7, HIGH);

  // Convertir el tiempo en distancia
  distance_2 = pingTravelTime_sensor2 * 0.0343 / 2;

  // Imprimir las distancias separadas por un guión
  Serial.print(distance_1);
  Serial.print("|");
  Serial.print(distance_2);

  // ACELERÓMETRO
  // Leer los datos de aceleración
  sensors_event_t event;
  accel.getEvent(&event);

  if (!referenceSet) {
    // Establecer los valores de referencia en la primera lectura
    referenceX = event.acceleration.x;
    referenceY = event.acceleration.y;
    referenceSet = true;
  }

  // Calcular los desplazamientos en relación a los valores de referencia
  float displacementX = event.acceleration.x - referenceX;
  float displacementY = event.acceleration.y - referenceY;

  // Imprimir los valores de desplazamiento en los ejes X, Y, Z
  Serial.print("|");
  Serial.print(displacementX);
  Serial.print("|");
  Serial.print(displacementY);
  

  // SENSORES DE VIBRACIÓN (leer continuamente sin bloqueo)
  int sensorValue_A0 = analogRead(sensorPin_A0);
  int sensorValue_A1 = analogRead(sensorPin_A1);
  int sensorValue_A2 = analogRead(sensorPin_A2);

  // Actualizar el tiempo de detección de ruido
  if (sensorValue_A0 < 1000) {
    lastNoiseTime_A0 = currentMillis;
  }
  if (sensorValue_A1 < 1000) {
    lastNoiseTime_A1 = currentMillis;
  }
  if (sensorValue_A2 > 500) {
    lastNoiseTime_A2 = currentMillis;
  }

  // Verificar si hubo ruido en los últimos 2 segundos y mostrar "SI" o "NO"
  Serial.print("|");
  Serial.print((currentMillis - lastNoiseTime_A0) < 2000 ? "SI" : "NO");
  Serial.print("|");
  Serial.print((currentMillis - lastNoiseTime_A1) < 2000 ? "SI" : "NO");
  Serial.print("|");
  Serial.println((currentMillis - lastNoiseTime_A2) < 2000 ? "SI" : "NO");

  delay(2000);
}

const int sensorPin = A0;  // Pin donde está conectado el sensor

void setup() {
  Serial.begin(9600); // Inicia comunicación con la computadora
}

void loop() {
  int valorSensor = analogRead(sensorPin);  // Lee el valor del sensor
  float temperatura = valorSensor * 0.488; // Convierte el valor en grados Celsius
  Serial.println(temperatura);             // Muestra la temperatura en el monitor serial
  delay(1000);                             // Espera 1 segundo
}
