int incomingByte = 0; // for incoming serial data

void setup() {
  Serial.begin(9600); // opens serial port, sets data rate to picoscope value
}

void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
    
    // Character
    // https://www.arduino.cc/en/Reference/ASCIIchart
    char character = incomingByte;

    // say what you got:
    Serial.print(character);
    // Carriage return is 13 in DEC and should be passed through by PIC
  }
}
