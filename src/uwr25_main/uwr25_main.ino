#include "com.h"
#include "thctrl.h"

com SerialHandler;
th TrusterController;

void setup() {
  SerialHandler.begin();
  TrusterController.begin();
}

void loop() {
  SerialHandler.update();
  TrusterController.drive(0.2);
  //power 0.0 ~ 1.0
  delay(DELAY);
}
