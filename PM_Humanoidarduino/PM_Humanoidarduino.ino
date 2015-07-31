//http://pastebin.fr/40393

#include "Servo.h"
 
#define G_GAUCHE_PIN 2
#define G_DROITE_PIN 3
#define H_1_GAUCHE_PIN 4
#define H_1_DROITE_PIN 5
#define H_2_GAUCHE_PIN 6
#define H_2_DROITE_PIN 7
#define E_1_GAUCHE_PIN 8
#define E_1_DROITE_PIN 9
#define E_2_GAUCHE_PIN 10
#define E_2_DROITE_PIN 11
#define C_GAUCHE_PIN 12
#define C_DROITE_PIN 13
#define T_1_PIN 44
#define T_2_PIN 46
 
#define LED_G 42
#define LED_D 40
 
Servo genou_gauche;
Servo genou_droit;
Servo hanche_1_gauche;
Servo hanche_1_droit;
Servo hanche_2_gauche;
Servo hanche_2_droit;
Servo epaule_1_gauche;
Servo epaule_1_droit;
Servo epaule_2_gauche;
Servo epaule_2_droit;
Servo coude_gauche;
Servo coude_droit;
Servo tete_1;
Servo tete_2;

int genou_gauche_v = 120;
int genou_droit_v = 60;
int hanche_1_gauche_v = 80;
int hanche_1_droit_v = 100;
int hanche_2_gauche_v = 117;
int hanche_2_droit_v = 80;
int epaule_1_gauche_v = -180;
int epaule_1_droit_v = 180;
int epaule_2_gauche_v = 90;    
int epaule_2_droit_v = 0;
int coude_gauche_v = 90;
int coude_droit_v = 90;
int tete_1_v = 10;
int tete_2_v = 10;

void setup() {
  Serial.begin(9600);
    genou_gauche.attach(G_GAUCHE_PIN);
    genou_droit.attach(G_DROITE_PIN);
    hanche_1_gauche.attach(H_1_GAUCHE_PIN);
    hanche_1_droit.attach(H_1_DROITE_PIN);
    hanche_2_gauche.attach(H_2_GAUCHE_PIN);
    hanche_2_droit.attach(H_2_DROITE_PIN);
    epaule_1_gauche.attach(E_1_GAUCHE_PIN);
    epaule_1_droit.attach(E_1_DROITE_PIN);
    epaule_2_gauche.attach(E_2_GAUCHE_PIN);
    epaule_2_droit.attach(E_2_DROITE_PIN);
    coude_gauche.attach(C_GAUCHE_PIN);
    coude_droit.attach(C_DROITE_PIN);
    tete_1.attach(T_1_PIN);
    tete_2.attach(T_2_PIN);
   
    genou_gauche.write(90);
    genou_droit.write(90);
    hanche_1_gauche.write(90);
    hanche_1_droit.write(90);
    hanche_2_gauche.write(90);
    hanche_2_droit.write(90);
    epaule_1_gauche.write(90);
    epaule_1_droit.write(90);
    epaule_2_gauche.write(90);
    epaule_2_droit.write(90);
    coude_gauche.write(90);
    coude_droit.write(90);
    tete_1.write(90);
    tete_2.write(90);
 
    pinMode(LED_D, OUTPUT);
    pinMode(LED_G, OUTPUT);
    digitalWrite(LED_D, HIGH);
    digitalWrite(LED_G, HIGH);
}
 
void loop() {
// if there's any serial available, read it:
 while (Serial.available() > 0) {
   int index=Serial.read(); // lire un premier caractère

   //Serial.print("index : "); Serial.println(index);

   // filtrer : il doit etre une lettre entre A et P
   if(index >= 'A' && index <= 'P'){
     int valeur = Serial.parseInt();

    // Serial.print("valeur : "); Serial.println(valeur);


     // traitement
     switch(index){
     case 'O': // allume/eteint la led en envoyant O1 et O0
       // allume la led si le chiffre est superieur a 0
       if(valeur > 0){
         digitalWrite(LED_D,HIGH);
       }
       else {
         digitalWrite(LED_D,LOW);
       }
       break;
       
     case 'P': // allume/eteint la led en envoyant P1 et P0
       // allume la led si le chiffre est superieur a 0
       if(valeur > 0){
         digitalWrite(LED_G,HIGH);
       }
       else {
         digitalWrite(LED_G,LOW);
       }
       break;

     case 'A':
       tete_1_v = valeur;
       break;

     case 'B':
       tete_2_v = valeur;
       break;

     case 'C':
       epaule_1_droit_v = valeur;
       break;
       
     case 'D':
      epaule_2_droit_v = valeur;
       break;
             
     case 'E':
      epaule_1_gauche_v = valeur;
       break;
             
     case 'F':
      epaule_2_gauche_v = valeur;
       break;

     case 'G':
      coude_droit_v = valeur;
       break;

     case 'H':
      coude_gauche_v = valeur;
       break;

     case 'I':
      hanche_1_droit_v = valeur;
       break;
    
     case 'J':
      hanche_1_gauche_v = valeur;
       break;
   
     case 'K':
      hanche_2_droit_v = valeur;
       break;
        
     case 'L':
      hanche_2_gauche_v = valeur;
       break;
   
     case 'M':
      genou_droit_v = valeur;
       break;

     case 'N':
      genou_gauche_v = valeur;
       break;
       
       }
   }

 }
   genou_gauche.write(genou_gauche_v);
   genou_droit.write(genou_droit_v);
   hanche_1_gauche.write(hanche_1_gauche_v);
   hanche_1_droit.write(hanche_1_droit_v);
   hanche_2_gauche.write(hanche_2_gauche_v);
   hanche_2_droit.write(hanche_2_droit_v);
   epaule_1_gauche.write(epaule_1_gauche_v);
   epaule_1_droit.write(epaule_1_droit_v);
   epaule_2_gauche.write(epaule_2_gauche_v);
   epaule_2_droit.write(epaule_2_droit_v);
   coude_gauche.write(coude_gauche_v);
   coude_droit.write(coude_droit_v);
   tete_1.write(tete_1_v);
   tete_2.write(tete_2_v);

}
