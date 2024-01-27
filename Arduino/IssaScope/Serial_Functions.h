#include "General_Settings.h"
#include <SerialCommand.h>   // SerialCommand Library by Steven Cogswell https://github.com/shyd/Arduino-SerialCommand
SerialCommand SCmd;



/* ----------------------------------------------------------------------------------*/
/* ------------------------------ Optogenetics LED 1 --------------------------------*/
void Opto_LED1_Off(){
  tlc.setPWM(opto0,0); 
  tlc.write(); 
}

void Opto_LED1_On(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
  }
  tlc.setPWM(opto0,aNumber/100*LED_Power); 
  tlc.write(); 
}

void Opto_LED1_Test(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
  }
  tlc.setPWM(opto0,aNumber/100*LED_Power); 
  tlc.write(); 
}


/* ----------------------------------------------------------------------------------*/
/* ------------------------------ Optogenetics LED 2 --------------------------------*/
void Opto_LED2_Off(){
  tlc.setPWM(opto1,0); 
  tlc.write(); 
}

void Opto_LED2_On(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
  }
  tlc.setPWM(opto1,aNumber/100*LED_Power); 
  tlc.write(); 
}

void Opto_LED2_Test(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
  }
  tlc.setPWM(opto1,aNumber/100*LED_Power); 
  tlc.write(); 
}


/* ----------------------------------------------------------------------------------*/
/* ------------------------------ Optogenetics LED 3 --------------------------------*/
void Opto_LED3_Off(){
  tlc.setPWM(opto2,0); 
  tlc.write(); 
}

void Opto_LED3_On(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
  }
  tlc.setPWM(opto2,aNumber/100*LED_Power); 
  tlc.write(); 
}

void Opto_LED3_Test(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
  }
  tlc.setPWM(opto2,aNumber/100*LED_Power); 
  tlc.write(); 
}


/* ----------------------------------------------------------------------------------*/
/* ------------------------------ Optogenetics LED 4 --------------------------------*/
void Opto_LED4_Off(){
  tlc.setPWM(opto3,0); 
  tlc.write(); 
}

void Opto_LED4_On(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
  }
  tlc.setPWM(opto3,aNumber/100*LED_Power); 
  tlc.write(); 
}

void Opto_LED4_Test(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
  }
  tlc.setPWM(opto3,aNumber); 
  tlc.write(); 
}




/* ----------------------------------------------------------------------------------*/
/* ----------------------------- Turn all White LED off -----------------------------*/
void White_LED_Off(){
  for (int i = 0; i <= 7; i++) {
    tlc.setPWM(White_LED_Array[i],0);                        
  } 
  tlc.write();   
}


/* ----------------------------------------------------------------------------------*/
/* ----------------------------- Turn all White LED on ------------------------------*/
void White_LED_On(){
  for (int i = 0; i <= 7; i++) {
    tlc.setPWM(White_LED_Array[i],LED_Power);                        
  } 
  tlc.write();   
}


/* ----------------------------------------------------------------------------------*/
/* ------------------------------- Turn all IR LED off ------------------------------*/
void IR_LED_Off(){
  for (int i = 0; i <= 7; i++) {
    tlc.setPWM(IR_LED_Array[i],0);                        
  } 
  tlc.write();   
}


/* ----------------------------------------------------------------------------------*/
/* ------------------------------- Turn all IR LED on -------------------------------*/
void IR_LED_On(){
  for (int i = 0; i <= 7; i++) {
    tlc.setPWM(IR_LED_Array[i],LED_Power);                        
  } 
  tlc.write();   
}




/* ----------------------------------------------------------------------------------*/
/* -------------------------------  White LED Block 1 -------------------------------*/
void White_LED1_Off(){
  tlc.setPWM(White_LED_Array[0],0); 
  tlc.setPWM(White_LED_Array[2],0);                       
  tlc.write();   
}

void White_LED1_On(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
  }
  tlc.setPWM(White_LED_Array[0],aNumber/100*LED_Power); 
  tlc.setPWM(White_LED_Array[2],aNumber/100*LED_Power);                       
  tlc.write();   
}


/* ----------------------------------------------------------------------------------*/
/* -------------------------------  White LED Block 2 -------------------------------*/
void White_LED2_Off(){
  tlc.setPWM(White_LED_Array[1],0); 
  tlc.setPWM(White_LED_Array[3],0);                       
  tlc.write();   
}

void White_LED2_On(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
  }
  tlc.setPWM(White_LED_Array[1],aNumber/100*LED_Power); 
  tlc.setPWM(White_LED_Array[3],aNumber/100*LED_Power);                       
  tlc.write();   
}


/* ----------------------------------------------------------------------------------*/
/* -------------------------------  White LED Block 3 -------------------------------*/
void White_LED3_Off(){
  tlc.setPWM(White_LED_Array[4],0); 
  tlc.setPWM(White_LED_Array[6],0);                       
  tlc.write();   
}

void White_LED3_On(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
  }
  tlc.setPWM(White_LED_Array[4],aNumber/100*LED_Power); 
  tlc.setPWM(White_LED_Array[6],aNumber/100*LED_Power);                       
  tlc.write();   
}


/* ----------------------------------------------------------------------------------*/
/* -------------------------------  White LED Block 4 -------------------------------*/
void White_LED4_Off(){
  tlc.setPWM(White_LED_Array[5],0); 
  tlc.setPWM(White_LED_Array[7],0);                       
  tlc.write();   
}

void White_LED4_On(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
  }
  tlc.setPWM(White_LED_Array[5],aNumber/100*LED_Power); 
  tlc.setPWM(White_LED_Array[7],aNumber/100*LED_Power);                       
  tlc.write();   
}




/* ----------------------------------------------------------------------------------*/
/* ---------------------------------  IR LED Block 1 --------------------------------*/
void IR_LED1_Off(){
  tlc.setPWM(IR_LED_Array[0],0); 
  tlc.setPWM(IR_LED_Array[2],0);                       
  tlc.write();   
}

void IR_LED1_On(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
  }
  tlc.setPWM(IR_LED_Array[0],aNumber/100*LED_Power); 
  tlc.setPWM(IR_LED_Array[2],aNumber/100*LED_Power);                       
  tlc.write();   
}



/* ----------------------------------------------------------------------------------*/
/* ---------------------------------  IR LED Block 2 --------------------------------*/
void IR_LED2_Off(){
  tlc.setPWM(IR_LED_Array[1],0); 
  tlc.setPWM(IR_LED_Array[3],0);                       
  tlc.write();   
}

void IR_LED2_On(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
  }
  tlc.setPWM(IR_LED_Array[1],aNumber/100*LED_Power); 
  tlc.setPWM(IR_LED_Array[3],aNumber/100*LED_Power);                       
  tlc.write();   
}



/* ----------------------------------------------------------------------------------*/
/* ---------------------------------  IR LED Block 3 --------------------------------*/
void IR_LED3_Off(){
  tlc.setPWM(IR_LED_Array[4],0); 
  tlc.setPWM(IR_LED_Array[6],0);                       
  tlc.write();   
}

void IR_LED3_On(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
  }
  tlc.setPWM(IR_LED_Array[4],aNumber/100*LED_Power); 
  tlc.setPWM(IR_LED_Array[6],aNumber/100*LED_Power);                       
  tlc.write();   
}



/* ----------------------------------------------------------------------------------*/
/* ---------------------------------  IR LED Block 4 --------------------------------*/
void IR_LED4_Off(){
  tlc.setPWM(IR_LED_Array[5],0); 
  tlc.setPWM(IR_LED_Array[7],0);                       
  tlc.write();   
}

void IR_LED4_On(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
  }
  tlc.setPWM(IR_LED_Array[5],aNumber/100*LED_Power); 
  tlc.setPWM(IR_LED_Array[7],aNumber/100*LED_Power);                       
  tlc.write();   
}






void SCmdAddCommand(){
  SCmd.addCommand("O10", Opto_LED1_Off);
  SCmd.addCommand("O1", Opto_LED1_On);
  SCmd.addCommand("T1", Opto_LED1_Test);

  SCmd.addCommand("O20", Opto_LED2_Off);
  SCmd.addCommand("O2", Opto_LED2_On);
  SCmd.addCommand("T2", Opto_LED2_Test);

  SCmd.addCommand("O30", Opto_LED3_Off);
  SCmd.addCommand("O3", Opto_LED3_On);
  SCmd.addCommand("T3", Opto_LED3_Test);

  SCmd.addCommand("O40", Opto_LED4_Off);
  SCmd.addCommand("O4", Opto_LED4_On);
  SCmd.addCommand("T4", Opto_LED4_Test);



  SCmd.addCommand("W0", White_LED_Off);
  SCmd.addCommand("W", White_LED_On);

  SCmd.addCommand("W10", White_LED1_Off);
  SCmd.addCommand("W1", White_LED1_On);

  SCmd.addCommand("W20", White_LED2_Off);
  SCmd.addCommand("W2", White_LED2_On);

  SCmd.addCommand("W30", White_LED3_Off);
  SCmd.addCommand("W3", White_LED3_On);

  SCmd.addCommand("W40", White_LED4_Off);
  SCmd.addCommand("W4", White_LED4_On);



  SCmd.addCommand("R0", IR_LED_Off);
  SCmd.addCommand("R", IR_LED_On);

  SCmd.addCommand("R10", IR_LED1_Off);
  SCmd.addCommand("R1", IR_LED1_On);

  SCmd.addCommand("R20", IR_LED2_Off);
  SCmd.addCommand("R2", IR_LED2_On);

  SCmd.addCommand("R30", IR_LED3_Off);
  SCmd.addCommand("R3", IR_LED3_On);

  SCmd.addCommand("R40", IR_LED4_Off);
  SCmd.addCommand("R4", IR_LED4_On);
}