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
  
  CurrentMillis = millis();                          // Pick up current running time in milliseconds
  DiffMillis = CurrentMillis - PreviousMillis;       // Calculate 
  tDiffMillis = CurrentMillis - tPreviousMillis;

  if (PreAdaptationFlag == false){
    if (DiffMillis >= ResolutionMillis) {
      PreviousMillis = millis();

      if (StimulusFlag == true){
        Serial.println(i);
        i += 1;
        if(i >= iLoop){
          i = 1;
        }
      }
    }
  }
  
  if (PreAdaptationFlag == true){
    if (DiffMillis >= PreAdaptMillis) {
      PreviousMillis = millis();
      PreAdaptationFlag = false;

      if (StimulusFlag == true){
        Serial.println(i);
        i += 1;
      }
    }
  }


 
  if (tDiffMillis >= TriggerTime ) {
    tPreviousMillis = millis();

    if (StimulusFlag == true){
  
      if (TriggerModeFlag == true) {
        TriggerFlag = true;
        tPreviousMillis = CurrentMillis;
        digitalWrite(Trigger, HIGH);
        
        tr +=1;
        if (tr >= TriggerMode){
          tr = 0;
        }    
        TriggerTime = TriggerArray[tr];
      }
    }
  }

  if (TriggerFlag == true){ 

    if (CurrentMillis >= tPreviousMillis+TriggerDuration){
      digitalWrite(Trigger, LOW);
      TriggerFlag = false;
    }
  }
}