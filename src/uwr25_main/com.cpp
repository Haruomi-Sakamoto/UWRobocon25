#include "com.h"

com::com() {} 

float cmdvel[CONTENTS] = {0,0,0,0};

void com::begin() {
  Serial.begin(COMSPEED);
  while (!Serial);
}

void com::update() {
  while (Serial.available() > 0) {
    char c = Serial.read();
    if (c == '\n') { parseInput(); inputString = ""; }
    else inputString += c;
  }

}

void com::parseInput() {
  int idx = 0, start = 0;
  while (idx < CONTENTS && start < inputString.length()) {
    int comma = inputString.indexOf(',', start);
    if (comma == -1) comma = inputString.length();
    cmdvel[idx++] = inputString.substring(start, comma).toFloat();
    start = comma + 1;
  }
  /*
  Serial.print(F("Arduino data: "));
  for (int i = 0; i < CONTENTS; i++) {
    Serial.print(cmdvel[i]);
    if (i < CONTENTS - 1) Serial.print(F(", "));
  }
  Serial.println();
  */
}
