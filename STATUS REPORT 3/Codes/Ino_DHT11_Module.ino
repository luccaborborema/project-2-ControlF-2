//#include <SoftwareSerial.h>
#include <SimpleDHT.h>

//SoftwareSerial RFID(2, 3); // RX and TX

// for DHT11, 
//      VCC: 5V or 3V
//      GND: GND
//      DATA: 2
int pinDHT11 = 2;
SimpleDHT11 dht11(pinDHT11);

long int timeStamp;
bool executa = false;

void setup()
{
  //RFID.begin(9600);
  Serial.begin(9600);
  pinMode(3,INPUT);
}
  
void loop() 
{
  byte temperature = 0;
  byte humidity = 0;
  int err = SimpleDHTErrSuccess;
  if (digitalRead(3))
    { 
    executa = true; 
    timeStamp = millis();
    } 
    
   if (executa)
   {
    if ((err = dht11.read(&temperature, &humidity, NULL)) != SimpleDHTErrSuccess)
      {
        Serial.print("Read DHT11 failed, err="); Serial.println(err);delay(1000);
        return;
      }
    Serial.print("t"); Serial.println((int)temperature); Serial.print("h"); Serial.println((int)humidity);
    delay(1000);
    
    
    if ((millis() - timeStamp) > 5000)
      { 
        executa = false;
        Serial.print("pause"); 
      } 
    }
    delay(500);
}
