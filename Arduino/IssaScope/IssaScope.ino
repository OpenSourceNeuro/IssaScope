#include "Serial_functions.h"

/* ----------------------------------------------------------------------------------*/
/* --------------------------- Settings and Initialisings ---------------------------*/

void setup() {
  HardwareSettings();             // Load Hardware Settings as described in "General_Settings.h"
  Connection();                   // Light up LED in sequence when the stimulator is reset
  SCmdAddCommand();               // Initiate Serial Command actions
}

/* ----------------------------------------------------------------------------------*/
/* ----------------------------------- Main Loop ------------------------------------*/
  
void loop() {
  SCmd.readSerial();                                 // Wait for Serial Command
}