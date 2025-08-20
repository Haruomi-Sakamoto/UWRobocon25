#include "thctrl.h"

th::th() {} 

const int thvpin[THRUSTER] = {3,9,6,5};
const int thvec[THRUSTER][THRUSTER] = {
    {0, 1, 0,  1},
    {0, 1, 0, -1},
    {0, 0, 1,  0},
    {0, 0, 1,  0}
};

float thpwr[THRUSTER] = {0,0,0,0};
float target[THRUSTER] = {0,0,0,0};
const float maxStep = 0.05;

int pwm[THRUSTER] = {ESCSTOP, ESCSTOP, ESCSTOP, ESCSTOP};

Servo servo[THRUSTER];

extern float cmdvel[THRUSTER];

void th::begin() {
    for (int i = 0; i < THRUSTER; i++) {
        servo[i].attach(thvpin[i]);
        servo[i].writeMicroseconds(ESCSTOP);
    }
}

void th::drive(float power ) {
    for (int i = 0; i < THRUSTER; i++) {
        target[i] = 0.0;
        for (int j = 0; j < THRUSTER; j++) {
            target[i] += thvec[i][j] * cmdvel[j];
        }
    }
    for (int i = 0; i < THRUSTER; i++) {
        float diff = target[i] - thpwr[i];
        if (diff > maxStep) diff = maxStep;
        if (diff < -maxStep) diff = -maxStep;
        thpwr[i] += diff;
    }
    for (int i = 0; i < THRUSTER; i++) {
        pwm[i] = ESCSTOP + (int)(thpwr[i] * ESCWIDTH * power);
        servo[i].writeMicroseconds(pwm[i]);
    }

    Serial.print(F("Arduino data: "));
    for (int i = 0; i < CONTENTS; i++) {
        Serial.print(pwm[i]);
        if (i < CONTENTS - 1) Serial.print(F(", "));
    }
    Serial.println();
}
