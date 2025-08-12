#include "ardconfig.h"
#include <Arduino.h>
#include <Servo.h>

class th {
public:
    th();
    void begin();
    void drive(float power);
};
