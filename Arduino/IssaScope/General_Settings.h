/*          ---  General Settings  ---
*/
  #include <SPI.h>                            // Include the arduino serial port interface library
  #include "Adafruit_TLC5947.h"               // Include the Adafruit TLC5947 libvrary. For better result one may change the number of channel defined in the Adafruit_TLC5947.cpp library

  #define   MISO           23                 // TLC SPI connection, Data Out
  #define   MOSI           19                 // TLC SPI connection, Data In 
  #define   CLK            18                 // TLC SPI connection, Clock 
  #define   latch          5                  // TLC Latch
  #define   Blank          17                 // TLC Ouput Enable, Also Optional feature to prevent LED to light up when powering up the TLC board
  #define   Trigger        33                 // Stimulus Tirgger channel output

  Adafruit_TLC5947 tlc = Adafruit_TLC5947(1, CLK, MISO, latch);

/* ----------------------------------------------------------------------------------*/
/* ------------------------------- Global Variables ---------------------------------*/

  word           BaudRate      = 921600;      // Baud Rate speed
  char           sCmd;                        // Serial monitor 
  float          aNumber;
  char           *arg;
  int            LED_Power     = 4095;


  int opto0 =  0;
  int opto1 =  1;
  int opto2 =  2;
  int opto3 =  3;
  int Opto_LED_Array[]{opto0, opto1, opto2, opto3};

  int  w0  =   8;
  int  w1  =   9;
  int  w2  =  10;
  int  w3  =  11;
  int  w4  =  12;
  int  w5  =  13;
  int  w6  =  14;
  int  w7  =  15;
  int White_LED_Array[]{w0, w2, w1, w3, w4, w6, w5, w7};

  int  r0  =  16;
  int  r1  =  17;
  int  r2  =  18;
  int  r3  =  19;
  int  r4  =  20;
  int  r5  =  21;
  int  r6  =  22;
  int  r7  =  23;
  int IR_LED_Array[]{r0, r2, r1, r3, r4, r6, r5, r7};


bool           StimulusFlag = false;
bool           flag;
int            i;                           // Iteration loop factor
int            iLoop;
int            CurrentMillis;               // Current Microsecond clock
int            PreviousMillis;              // Microsecond clock stamp
int            DiffMillis;                  // Difference in microseconds between the clock and the stamp
int            tPreviousMillis;             // Microsecond clock stamp
int            tDiffMillis;                 // Difference in microseconds between the clock and the stamp
int            tdPreviousMillis;            // Microsecond clock stamp
int            tdDiffMillis;                // Difference in microseconds between the clock and the stamp
int            ResolutionMillis;            // Microseconds delay between two i iteration
int            PreAdaptMillis;              // Preadaptation period in microseconds
bool           PreAdaptationFlag;
bool           TriggerModeFlag;
int            TriggerMode;                 // Set the Trigger mode
int            TriggerArray[100];

int            t;                           // Trigger counter
int            td;                          // Trigger Pulse counter
int            tr;                          // TriggerTime array counter
bool           TriggerFlag = false;         // Trigger Flag
int            TriggerTime;                 // Lenght of the Trigger loop in ms 
int            TriggerDuration = 100000;    // Length of the Trigger signal in us 

int            l;                           // LED iteration factor


/* ----------------------------------------------------------------------------------*/
/* ----------------------------- Initialising conditions ----------------------------*/

void HardwareSettings(){
// Set pins
  pinMode(Trigger, OUTPUT);  
  digitalWrite(Trigger, LOW);  

// Initialise the serial communication with PC
  Serial.begin(BaudRate);                      
  
// Initialise the Adafruit TLC driver 
  tlc.begin();
  tlc.write();  

// Initialise parameters
  l = 0;
  t = 0;
  td = 0;
  TriggerFlag = false;
  CurrentMillis = 0;
  PreviousMillis = 0;
  DiffMillis = 0;
  tPreviousMillis = 0;
  tDiffMillis = 0;
  tdPreviousMillis = 0;
  flag = true;
}

/* ----------------------------------------------------------------------------------*/
/* -----------------------------------  Connection ----------------------------------*/
void Connection(){
  for (int i = 0; i <= 7; i++) {
    tlc.setPWM(White_LED_Array[i],LED_Power);                        
    tlc.write();
    delay(100);
  }
  for (int i = 0; i <= 7; i++) {
    tlc.setPWM(White_LED_Array[i],0);                        
    tlc.write();
  }
}
