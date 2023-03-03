#include <Wire.h>
#include <VL53L0X.h>
VL53L0X sensor;

//#include <LiquidCrystal_I2C.h>
//LiquidCrystal_I2C lcd(0x27, 16, 2);
//ultrasonico
const int pinTrigger = 2
const int pinEcho = 3;
//acelerometro
int max = 0;
float c =4.1/489;

void setup() {
  //distancia
  Wire.begin();
 
  sensor.init();
  sensor.setTimeout(500);
  sensor.startContinuous();

  Serial.begin(9600);//Configuramos la comunicación serial
  pinMode(pinTrigger, OUTPUT); //Configuramoms el pin de "trigger" como salida
  pinMode(pinEcho, INPUT);  //Configuramoms el pin de "echo" como entrada
  digitalWrite(pinTrigger, LOW);//Ponemos en voltaje bajo(0V) el pin de "trigger"
}

void loop() {
  //acelerometro
  int valueAc = analogRead(A4);
  Serial.print(c*value);
  Serial.println(" cm");

  //fotoresistenica
  int valueLuz = analogRead(A1);
  Serial.print(valueLuz);

  //nivel de agua
  int valueAgua = analogRead(A0);
  Serial.print((valueAgua));

  //ultrasonido
  unsigned long t;
  float d;
  digitalWrite(pinTrigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(pinTrigger, LOW);
  t = pulseIn(pinEcho, HIGH); 
  d = t * 0.000001 * 34300.0 / 2.0;
  Serial.print("Distancia: ");
  Serial.print(d);

  //distancia
  Serial.print(sensor.readRangeContinuousMillimeters());
  if (sensor.timeoutOccurred()) { Serial.print(" TIMEOUT"); }
 
  Serial.println(" mm");
  delay(300);



}
