#include <Servo.h>

int sensorPin7 = A0;    //Lichtsensoren
int sensorValue7 = 0;
int sensorPin6 = A1;
int sensorValue6 = 0;
int sensorPin5 = A2;
int sensorValue5 = 0;
int sensorPin4 = A3;
int sensorValue4 = 0;
int sensorPin3 = A4;
int sensorValue3 = 0;
int sensorPin2 = A5;
int sensorValue2 = 0;
int sensorPin1 = A6 ;
int sensorValue1 = 0;

int coinCycleInterval = 3000;                //Interval, in dem Münzen sortiert werden
 
unsigned long currentMillis = 0;              //speichert die Anzahl Millis() in jedem loop()
unsigned long previousCoinCycleMillis = 0;    //speichert die Zeit, in der zuletzt eine Münze sortiert wurde          
int servoMillis = 0;

int input1 = 0;   //Signal vom Lichtsensor, wenn eine Münze durchgeht
int input2 = 0;
int input3 = 0;
int input4 = 0;
int input5 = 0;
int input6 = 0;
int input7 = 0;
int coin1 = 0;    //Im System gelagerte Münzen dieser Art
int coin2 = 0;
int coin3 = 0;
int coin4 = 0;
int coin5 = 0;
int coin6 = 0;
int coin7 = 0;
int c1=1;
int c2=4;
int c3=2;
int c4=3;
int c5=5;
int c6=6;
int c7=7;
int c0=0;

int servoState=0;

int idleCount=0;

boolean coinsCounted = false;

Servo servo1;
int pos = 80;
int turn1 = 0;
int turn2 = 0;
int turn3 = 0;

void setup() {
  Serial.begin(9600);
  servo1.attach(53);                        //Servo
  servo1.write(90);
}

void loop() {
  //Speichert die Zeit in Millisekunden und führt die Funktionen zum Zählen der Münzen aus 
  currentMillis = millis();                 //Speichert Zeit in ms

  piSignal();
  if (servoState == 1) {
    servoTurn();
  }
  sensorInputs();                           //Führt die Funktionen aus
  coinCounting();
  if (idleCount == 20){
    servoState = 0;
  }
}

void sensorInputs() {
  sensorValue1 = analogRead(sensorPin1);    //Liest den Input der Lichtsensoren ab
  sensorValue2 = analogRead(sensorPin2);
  sensorValue3 = analogRead(sensorPin3);
  sensorValue4 = analogRead(sensorPin4);
  sensorValue5 = analogRead(sensorPin5);
  sensorValue6 = analogRead(sensorPin6);
  sensorValue7 = analogRead(sensorPin7);


  if (sensorValue1 > 500) {input1++;}       // >500 -> Infrarotsignal unterbrochen -> Münze  geht durch
  if (sensorValue2 > 500) {input2++;}
  if (sensorValue3 > 500) {input3++;}
  if (sensorValue4 > 500) {input4++;}
  if (sensorValue5 > 500) {input5++;}
  if (sensorValue6 > 500) {input6++;}
  if (sensorValue7 > 500) {input7++;}
}

void coinCounting() {
  /*Serial.print(sensorValue1);
  Serial.print(", ");
  Serial.print(sensorValue2);
  Serial.print(", ");
  Serial.print(sensorValue3);
  Serial.print(", ");
  Serial.print(sensorValue4);
  Serial.print(", ");
  Serial.print(sensorValue5);
  Serial.print(", ");
  Serial.print(sensorValue6);
  Serial.print(", ");
  Serial.println(sensorValue7);*/
  if (currentMillis - previousCoinCycleMillis >= coinCycleInterval) { //Nach bestimmter Zeit werden die Münzen wieder gezählt, genau dann, wenn eine neue Münze sortiert wurde
    previousCoinCycleMillis += coinCycleInterval;     //Damit das Zeitintervall wieder stimmt
    servoMillis = 0;
    pos = 80;
    turn1 = 0;
    turn2 = 0;
    turn3 = 0;
    coinsCounted = false;
  }  
    
  if (currentMillis - previousCoinCycleMillis >= 2500 && coinsCounted == false) { //Nach bestimmter Zeit werden die Münzen wieder gezählt, genau dann, wenn eine neue Münze sortiert wurde
    if (input1 > 0) {                                                 //überprüft die letzte Lichtschranke, bei der das Signal unterbrochen wurde und bestimmt so, was für eine Münze in das System sortiert wurde
      if (input2 > 0) {
        if (input3 > 0) {
          if (input4 > 0) {
            if (input5 > 0) {
              if (input6 > 0) {
                if (input7 > 0) {
                  Serial.println(c7);
                  idleCount=0;
                }
                else{
                Serial.println(c6);
                  idleCount=0;
                }
              }
              else{
              Serial.println(c5);
              idleCount=0;
            }
            }
            else{
            Serial.println(c4);
            idleCount=0;
          }
          }
          else{
          Serial.println(c3);
          idleCount=0;
        }
        }
        else{
        Serial.println(c2);
        idleCount=0;
      }
      }
      else{
      Serial.println(c1);
      idleCount=0;
    }
    }
    else{
    Serial.println(c0);
    idleCount++;
  }
    
  input1 = 0;
  input2 = 0;
  input3 = 0;
  input4 = 0;
  input5 = 0;
  input6 = 0;
  input7 = 0;
  
  coinsCounted = true;
  }

//Serial.println("x");
}

void piSignal() {                      //nimmt Signal von PI auf
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    if (data == "Go") {
      servoState = 1;
    }
    if (data == "Stop") {
      servoState = 0;
    }
  }
}


void servoTurn() {   //eine Drehung des Servos
  if (currentMillis - previousCoinCycleMillis >= 500 && turn1 == 0){
    servo1.write(180);
    turn1++;
  }
  if (currentMillis - previousCoinCycleMillis >=1000 && turn2 == 0){
    servo1.write(120);
    turn2++;
  }
  if (currentMillis - previousCoinCycleMillis >1500 && turn3 == 0){
    servo1.write(160);
    turn3++;
  }
  if (currentMillis - previousCoinCycleMillis >= 2000 + servoMillis){
    servo1.write(pos);
    pos = pos - 5;
    servoMillis = servoMillis + 50;
  }
    /*
    delay(1000);
    servo1.write(180);
    delay(500);
    servo1.write(120);
    delay(500);
    servo1.write(160);
    delay(250);
    for(pos=80; pos>=5;pos=pos-5){
      servo1.write(pos);
      delay(50);
    }*/
}


//Schaltung:
//D und E zu -
//+ bei D zu 10K Widerstand von + -> Kabel zu A0 (steckt bei tieferer Zahl)
//+ bei E zu 220 Widerstand von + (verbrennt sonst) (steckt bei höherer Zahl)
