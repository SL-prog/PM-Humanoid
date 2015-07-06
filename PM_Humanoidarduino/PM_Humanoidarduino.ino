uint8_t LED = 13;

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
  digitalWrite(LED, LOW);
}

void loop() {
  if (Serial.available())
  {
    char received = Serial.read();
    if (received == 'O1')
      digitalWrite(LED, HIGH);
    else
      digitalWrite(LED, LOW);
     Serial.flush();
  }
}
