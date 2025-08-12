#include "thctrl.h"

th::th() {} 

const int thvpin[THRUSTER] = {3,5,6,9};
int pwm[THRUSTER] = {ESCSTOP, ESCSTOP, ESCSTOP, ESCSTOP};

Servo servo[THRUSTER];

void th::begin() {
    for (int i = 0; i < THRUSTER; i++) {
        servo[i].attach(thvpin[i]);
        servo[i].writeMicroseconds(ESCSTOP);
    }
}

void th::drive(float power) {
    for (int i = 0; i < THRUSTER; i++) {
        pwm[i] = ESCSTOP + (int)(cmdvel[i] * ESCWIDTH * power);
        servo[i].writeMicroseconds(pwm[i]);
    }
    Serial.print(F("Arduino data: "));
    for (int i = 0; i < CONTENTS; i++) {
      Serial.print(pwm[i]);
    if (i < CONTENTS - 1) Serial.print(F(", "));
    }
    Serial.println();
}
