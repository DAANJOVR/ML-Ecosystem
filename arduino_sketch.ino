const int relayPin = 8;  // Pin connected to the relay

void setup() {
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, LOW);  // Start with the relay off (door locked)
  Serial.begin(9600);           // Start serial communication
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    if (command == '1') {
      digitalWrite(relayPin, HIGH);  // Unlock the door
      Serial.println("Door Unlocked");
    } 
    else if (command == '0') {
      digitalWrite(relayPin, LOW);  // Lock the door
      Serial.println("Door Locked");
    }
  }
}
