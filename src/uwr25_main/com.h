#include "ardconfig.h"
#include <Arduino.h>

class com {
  private:
    String inputString;
    void parseInput();

  public:
    com();
    void begin();
    void update();
};
