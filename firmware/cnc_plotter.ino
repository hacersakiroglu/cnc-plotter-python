#include <AccelStepper.h>

AccelStepper stepperX(AccelStepper::DRIVER, 2, 5);
AccelStepper stepperY(AccelStepper::DRIVER, 3, 6);

String inputLine = "";

void setup() {
  Serial.begin(115200);

  stepperX.setMaxSpeed(800);
  stepperY.setMaxSpeed(800);

}

void loop() {
  if (Serial.available()) {
    char c = Serial.read();

    if (c == '\n') {
      processCommand(inputLine);
      inputLine = "";
    } else {
      inputLine += c;
    }
  }

  stepperX.run();
  stepperY.run();
}

void processCommand(String cmd) {
  cmd.trim();

  if (cmd.startsWith("G0") || cmd.startsWith("G1")) {
    float x = extractValue(cmd, 'X');
    float y = extractValue(cmd, 'Y');

    if (!isnan(x)) stepperX.moveTo(x * 80);
    if (!isnan(y)) stepperY.moveTo(y * 80);
  }
}

float extractValue(String data, char key) {
  int i = data.indexOf(key);
  if (i == -1) return NAN;

  int j = i + 1;
  while (j < data.length() && (isdigit(data[j]) || data[j] == '.' || data[j] == '-')) {
    j++;
  }

  return data.substring(i + 1, j).toFloat();
}

