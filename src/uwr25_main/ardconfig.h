#pragma once

#define DELAY 10

#define COMSPEED 115200
#define CONTENTS 4
#define THRUSTER 4

#define ESCSTOP 1500
#define ESCWIDTH 400

extern float cmdvel[CONTENTS];

extern const int thvpin[4];
extern int pwm[4];

